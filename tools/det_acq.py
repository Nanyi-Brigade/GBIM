import os
import os.path as ops

from path import init_path
root = init_path()

from utils import Camera


save_path = ops.join(root, "handdet/dataset")
if not ops.exists(save_path):
    os.mkdir(save_path)
acq_camera = Camera()
print("Start acquisition, press 'q' to exit.")
# acq_camera.get_img(None)  # 测试
acq_camera.get_img(save_path)