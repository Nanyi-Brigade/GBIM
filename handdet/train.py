import paddlex as pdx
from paddlex import transforms as T


train_transforms = T.Compose([
    T.MixupImage(mixup_epoch=-1), T.RandomDistort(),
    T.RandomExpand(im_padding_value=[123.675, 116.28, 103.53]), T.RandomCrop(),
    T.RandomHorizontalFlip(), T.BatchRandomResize(
        target_sizes=[192, 224, 256, 288, 320, 352, 384, 416, 448, 480, 512],
        interp='RANDOM'), T.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
eval_transforms = T.Compose([
    T.Resize(
        target_size=320, interp='CUBIC'), T.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

train_dataset = pdx.datasets.VOCDetection(
    data_dir='handdet/dataset',
    file_list='handdet/dataset/train_list.txt',
    label_list='handdet/dataset/labels.txt',
    transforms=train_transforms,
    shuffle=True)
eval_dataset = pdx.datasets.VOCDetection(
    data_dir='handdet/dataset',
    file_list='handdet/dataset/val_list.txt',
    label_list='handdet/dataset/labels.txt',
    transforms=eval_transforms)

num_classes = len(train_dataset.labels)
model = pdx.det.PPYOLOTiny(num_classes=num_classes)
model.train(
    num_epochs=1000,
    train_dataset=train_dataset,
    train_batch_size=16,
    eval_dataset=eval_dataset,
    pretrain_weights='COCO',
    learning_rate=0.005,
    warmup_steps=1000,
    warmup_start_lr=0.0,
    lr_decay_epochs=[130, 540],
    lr_decay_gamma=.5,
    save_interval_epochs=5,
    save_dir='handdet/output',
    use_vdl=True)