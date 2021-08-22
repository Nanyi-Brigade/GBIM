import cv2
import time
import os.path as ops
from .show_score import sc_show


class Camera(object):
    def __init__(self, 
                 c_mode=0, 
                 c_width=768, 
                 c_height=768,
                 updata_func=None,
                 save_func=None,
                 class_func=None,
                 key_press=False):
        # 0：电脑摄像头，1：外接摄像头
        if c_mode not in [0, 1]:
            raise ValueError("The c_mode must be 0 or 1!")
        self.cap = cv2.VideoCapture(c_mode)
        self.cap.set(3, c_width)  # 宽
        self.cap.set(4, c_height)  # 高
        self.updata_func = updata_func  # 图像显示方法
        self.save_func = save_func  # 图像保存方法
        self.class_func =class_func  # 图像分类
        self.key_press = key_press  # 键盘控制

    def get_img(self, save_path=None):
        while(self.cap.isOpened()):
            ret_flag, Vshow = self.cap.read()  # 是否正确，图像
            if not ret_flag:
                raise ValueError("Failed to get image")
            # 保存
            if save_path is not None:
                img_path = ops.join(
                    save_path,
                    (str(time.time()).replace(".", "_") + ".jpg"))
                time.sleep(0.1)  # 每0.1秒获取一次
                if self.save_func is not None:
                    Vsave = self.save_func(Vshow)
                else:
                    Vsave = Vshow
                if Vsave is not None:
                    cv2.imwrite(img_path, Vsave)
            # 显示
            Wshow = Vshow.copy()
            if self.updata_func is not None:
                Wshow = self.updata_func(Wshow)
                if Wshow is None:
                    Wshow = Vshow.copy()
                else:
                    # 手势分类
                    if self.class_func is not None:
                        sc_show(
                            self.save_func(Vshow), 
                            self.class_func, self.key_press)
            cv2.imshow('Capture', Wshow)
            # 按q退出
            usdown = cv2.waitKey(1)
            # print(usdown)
            if usdown == 113:  # q
                break
        self.cap.release()
        cv2.destroyAllWindows()