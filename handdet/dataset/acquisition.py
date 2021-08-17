import os
import os.path as ops
from utils import Camera


save_path = "handdet/dataset/imgs"
if not ops.exists(save_path):
    os.mkdir(save_path)
acq_camera = Camera()
print("Start acquisition, press 'q' to exit.")
acq_camera.get_img(save_path)