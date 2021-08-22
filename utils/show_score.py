import cv2
import numpy as np
from .controller import press_key


CLASSES = ["up", "down", "left", "right", "big", "small", "other"]

def sc_show(img, clas_func, key_press=False):
    img24 = cv2.resize(img, (224, 224))
    layout = np.ones((256, 224, 3)) * 255
    if np.max(img) == 0:
        action = "None"
        final = [0.] * 7
    else:
        result = clas_func(img)
        # print(result)
        action = result[0]['category']
        press_key(action)  # 按键
        final = []
        for clas in CLASSES:
            for v in result:
                if v['category'] == clas:
                    # 未检出
                    if img is None:
                        v['score'] = 0.
                    final.append(v['score'])
                    break
    cv2.putText(img24, action, (0, 20),
                cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)
    for (i, score) in enumerate(final):
        # 构造标签文本
        text = "{}: {:.2f}%".format(CLASSES[i], score * 100)
        w = int(score * 300)
        cv2.rectangle(layout, (7, (i * 35) + 5),
                      (w, (i * 35) + 35), (130, 195, 175), -1)
        cv2.putText(layout, text, (10, (i * 35) + 23),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 0, 0), 2)
    cv2.imshow('Thesholded', np.vstack([
        img24.astype("uint8"), 
        layout.astype("uint8")]))