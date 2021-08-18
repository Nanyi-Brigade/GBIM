import os.path as ops

from path import init_path
root = init_path()

from handdet import HandDet
from utils import Camera


# 手识别的测试
hdet = HandDet(ops.join(root, "handdet/output/best_model"))
det_camera = Camera(updata_func=hdet.get_vis)
print("Start acquisition, press 'q' to exit.")
det_camera.get_img()