# import os.path as ops
# from path import init_path
# root = init_path()

from handdet import HandDet
from handclas import HandClas
from utils import Camera


# 手识别的测试
hdet = HandDet("handdet/output/best_model")
hclas = HandClas("handclas/output/best_model")
test_camera = Camera(
    updata_func=hdet.get_vis,
    save_func=hdet.get_hand,
    class_func=hclas.get_clas)
print("Start acquisition, press 'q' to exit.")
test_camera.get_img()