import os
import os.path as ops
import random
from tqdm import tqdm

from path import init_path
root = init_path()


jpeg_folder = (ops.join(root, "handclas/dataset/Images"))
train_txt = (ops.join(root, "handclas/dataset/train_list.txt"))
val_txt = (ops.join(root, "handclas/dataset/val_list.txt"))

with open(train_txt, "w") as tf:
    with open(val_txt, "w") as vf:
        data_list = []
        classes = os.listdir(jpeg_folder)
        for clas in classes:
            clas_folder = ops.join(jpeg_folder, clas)
            names = os.listdir(clas_folder)
            for name in names:
                jpeg_path = ops.join(jpeg_folder.split("/")[-1], name)
                data_list.append((jpeg_path + "" + str(clas) + "\n"))
        random.shuffle(data_list)
        for idx, data in tqdm(enumerate(data_list)):
            if idx % 10 == 0:
                vf.write(data)
            else:
                tf.write(data)