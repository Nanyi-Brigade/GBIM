import paddlex as pdx
from paddlex import transforms as T


train_transforms = T.Compose(
    [T.RandomCrop(crop_size=224), T.RandomBlur(), T.RandomDistort(), T.Normalize()])
eval_transforms = T.Compose([
    T.ResizeByShort(short_size=256), T.CenterCrop(crop_size=224), T.Normalize()
])

train_dataset = pdx.datasets.ImageNet(
    data_dir='handclas/dataset',
    file_list='handclas/dataset/train_list.txt',
    label_list='handclas/dataset/labels.txt',
    transforms=train_transforms,
    shuffle=True)   
eval_dataset = pdx.datasets.ImageNet(
    data_dir='handclas/dataset',
    file_list='handclas/dataset/val_list.txt',
    label_list='handclas/dataset/labels.txt',
    transforms=eval_transforms)

num_classes = len(train_dataset.labels)
model = pdx.cls.MobileNetV3_small_ssld(num_classes=num_classes)
model.train(num_epochs=20,
            train_dataset=train_dataset,
            train_batch_size=32,
            eval_dataset=eval_dataset,
            lr_decay_epochs=[6, 8],
            save_interval_epochs=1,
            learning_rate=0.00625,
            save_dir='handclas/output',
            use_vdl=True)