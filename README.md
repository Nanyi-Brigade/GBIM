# GBIM

[![Python 3.6](https://img.shields.io/badge/Python-3.6+-red.svg)](https://www.python.org/downloads/release/python-360/) [![PaddleX](https://img.shields.io/badge/PaddleX-2.0.0rc4-red.svg)](LICENSE) [![License](https://img.shields.io/badge/License-Apache%202-red.svg)](LICENSE)

手势交互地图 GBIM(Gesture-Based Interaction map)，基于视觉深度神经网络的交互地图，通过电脑摄像头观察使用者的手势变化，进而控制地图进行简单的交互。网络使用PaddleX提供的轻量级模型PPYOLO Tiny以及MobileNet  V3 small，使得整个模型大小约10MB左右，即使在CPU下也能快速定位和识别手势。

## 手势

|                          手势                          |   交互   |                          手势                          |   交互   |                          手势                          |   交互   |
| :----------------------------------------------------: | :------: | :----------------------------------------------------: | :------: | :----------------------------------------------------: | :------: |
| ![](https://i.loli.net/2021/08/17/7oQ1LxGh4jF3tpY.jpg) | 向上滑动 | ![](https://i.loli.net/2021/08/17/VoHT1j65CblqvJO.jpg) | 向左滑动 | ![](https://i.loli.net/2021/08/17/RkrTGL59WYA4yXz.jpg) | 地图放大 |
|                        **手势**                        | **交互** |                        **手势**                        | **交互** |                        **手势**                        | **交互** |
| ![](https://i.loli.net/2021/08/17/AImBc5J1MihfTeY.jpg) | 向下滑动 | ![](https://i.loli.net/2021/08/17/pzRXCByJI7cLQx4.jpg) | 向右滑动 | ![](https://i.loli.net/2021/08/17/gLzVIXidaK62Dy7.jpg) | 地图缩小 |

## 进度安排

### 基础

- [x] 确认用于交互的手势。
- [x] 使用`det_acq.py`采集一些电脑摄像头拍摄的人手姿势数据。
- [x] 数据标注，训练手的目标检测模型
- [x] 捕获目标手，使用`clas_acq.py`获取手部图像进行标注，并用于训练手势分类模型。
- [x] 交互手势的检测与识别组合验证，使用`test.py`。
- [x] 打开百度地图网页版，进行模拟按键交互。
- [ ] 组合功能，验证基本功能。

### 进阶

- [ ] 将图像分类改为序列图像分类，提高手势识别的流畅度和准确度。
- [ ] 重新采集和标注数据，调参训练模型。
- [ ] 搭建可用于参数调节的地图。
- [ ] 界面整合，整理及美化。

## 数据集 & 模型

### 手势检测

- 数据集使用来自联想小新笔记本摄像头采集的数据，使用labelImg标注为VOC格式，共1011张。该数据集场景、环境和人物单一，仅作为测试使用，不提供数据集下载。数据组织参考PaddelX下的[PascalVOC](https://github.com/PaddlePaddle/PaddleX/blob/develop/docs/data/format/detection.md)数据组织方式。
- 模型使用超轻量级[PPYOLO Tiny](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.2/configs/ppyolo/README_cn.md)，模型大小小于4MB，随便训练了100轮后保留best_model作为测试模型，由于数据集和未调参训练的原因，当前默认识别效果**较差**。

### 手势分类

- 数据集使用来自联想小新笔记本摄像头采集的数据，通过手势检测模型提出出手图像，人工分为7类，分别为6种交互手势以及“其他”，共1102张。该数据集数量较少，手型及手势单一，仅作为测试使用，不提供数据集下载。数据组织形式如下：

```
dataset
	├-- Images
	|     ├-- up
	┆     ┆    └-- xxx.jpg
	|     └-- other
	┆          └-- xxx.jpg
	├-- labels.txt
	├-- train_list.txt
	└-- val_list.txt
```

- 模型使用超轻量级MobileNet  V3 small，模型大小小于7MB，由于数据量很小，随便训练了20轮后保留best_model作为测试模型，当前识别分类效果**较差**。

*模型文件上传使用LFS，下拉时注意需要安装LFS，参考[LFS文档](https://git-lfs.github.com/)。后续将重新采集和标注更加多样的大量数据集，并采用更好的调参方法获得更加准确的识别模型*

## 手势识别演示

![](https://user-images.githubusercontent.com/71769312/130256584-8ac11188-dadc-472b-994e-7e0b7ea2f88a.gif)

## 常见问题及解决

1. **Q: 拉项目时卡住不动**

   A：首先确认按照文档安装LFS。如果已经安装那极大可能是网络问题，可以等待一段时间，或先跳过LFS文件，再单独拉取，参考下面git代码：

   ```shell
   // 开启跳过无法clone的LFS文件
   git lfs install --skip-smudge 
   // clone当前项目
   git clone "current project" 
   // 进入当前项目，单独拉取LFS文件
   cd "current project" 
   git lfs pull 
   // 恢复LFS设置
   git lfs install --force
   ```

## 参考

1. [玩腻了小游戏？Paddle手势识别玩转游戏玩出新花样！](https://aistudio.baidu.com/aistudio/projectdetail/587082)
2. [https://github.com/PaddlePaddle/PaddleX](https://github.com/PaddlePaddle/PaddleX)

## 交流与反馈

Email：nanyibrigade@163.com
