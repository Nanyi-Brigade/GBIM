import os
import os.path as ops

from path import init_path
root = init_path()

from handdet import HandDet
from utils import Camera


save_path = ops.join(root, "handclas/dataset")
if not ops.exists(save_path):
    os.mkdir(save_path)
hdet = HandDet(ops.join(root, "handdet/output/best_model"))
acq_camera = Camera(
    updata_func=hdet.get_vis,
    save_func=hdet.get_hand)
print("Start acquisition, press 'q' to exit.")
acq_camera.get_img(save_path)