import cv2
import time
import numpy as np
import os.path as ops
from .show_score import sc_show


class Camera(object):
    def __init__(self, 
                 c_mode=0, 
                 c_width=768, 
                 c_height=768,
                 update_func=None,
                 class_func=None,
                 key_press=False):
        # 0：电脑摄像头，1：外接摄像头
        if c_mode not in [0, 1]:
            raise ValueError("The c_mode must be 0 or 1!")
        self.cap = cv2.VideoCapture(c_mode)
        self.cap.set(3, c_width)  # 宽
        self.cap.set(4, c_height)  # 高
        self.update_func = update_func  # 图像显示方法
        self.class_func =class_func  # 图像分类
        self.key_press = key_press  # 键盘控制

    def get_img(self, save_path=None):
        while(self.cap.isOpened()):
            ret_flag, Vshow = self.cap.read()  # 是否正确，图像
            if not ret_flag:
                raise ValueError("Failed to get image")
            hand_img, vis_img = None, Vshow
            # 手势检测
            if self.update_func is not None:
                hand_img, vis_img = self.update_func(Vshow)
            # 手势分类
            if hand_img is not None:
                if self.class_func is not None:
                    sc_show(
                        hand_img, 
                        self.class_func, self.key_press)
            else:
                if self.class_func is not None:
                    sc_show(
                        np.zeros((224, 224, 3), dtype="uint8"), 
                        self.class_func, self.key_press)
            cv2.imshow('Capture', vis_img)
            # 保存
            if save_path is not None:
                img_path = ops.join(
                    save_path,
                    (str(time.time()).replace(".", "_") + ".jpg"))
                time.sleep(0.1)  # 每0.1秒获取一次
                if self.update_func is not None:
                    if hand_img is not None:
                        cv2.imwrite(img_path, hand_img)
                else:
                    cv2.imwrite(img_path, vis_img)
            # 按q退出
            usdown = cv2.waitKey(1)
            # print(usdown)
            if usdown == 113:  # q
                break
        self.cap.release()
        cv2.destroyAllWindows()