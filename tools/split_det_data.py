import os
import os.path as ops
import random
from tqdm import tqdm

from path import init_path
root = init_path()


jpeg_folder = (ops.join(root, "handdet/dataset/JPEGImages"))
train_txt = (ops.join(root, "handdet/dataset/train_list.txt"))
val_txt = (ops.join(root, "handdet/dataset/val_list.txt"))

with open(train_txt, "w") as tf:
    with open(val_txt, "w") as vf:
        names = os.listdir(jpeg_folder)
        random.shuffle(names)
        for idx, name in tqdm(enumerate(names)):
            jpeg_path = ops.join(jpeg_folder.split("/")[-1], name)
            xml_path = jpeg_path.replace("JPEGImages", "Annotations").replace(".jpg", ".xml")
            if idx % 10 == 0:
                vf.write(jpeg_path + " " + xml_path + "\n")
            else:
                tf.write(jpeg_path + " " + xml_path + "\n")