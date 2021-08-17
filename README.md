# GBIM

[![Python 3.6](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/) [![PaddleX](https://img.shields.io/badge/PaddleX-2.0.0rc4-blue.svg)](LICENSE) [![License](https://img.shields.io/badge/License-Apache%202-blue.svg)](LICENSE)

手势交互地图 GBIM(Gesture-Based Interaction map)。可通过电脑摄像头观察使用者的手势变化，进而简单控制地图的交互。

## 手势

|                          手势                          |   交互   |                          手势                          |   交互   |                          手势                          |   交互   |
| :----------------------------------------------------: | :------: | :----------------------------------------------------: | :------: | :----------------------------------------------------: | :------: |
| ![](https://i.loli.net/2021/08/17/7oQ1LxGh4jF3tpY.jpg) | 向上滑动 | ![](https://i.loli.net/2021/08/17/VoHT1j65CblqvJO.jpg) | 向左滑动 | ![](https://i.loli.net/2021/08/17/RkrTGL59WYA4yXz.jpg) | 地图放大 |
|                        **手势**                        | **交互** |                        **手势**                        | **交互** |                        **手势**                        | **交互** |
| ![](https://i.loli.net/2021/08/17/AImBc5J1MihfTeY.jpg) | 向下滑动 | ![](https://i.loli.net/2021/08/17/pzRXCByJI7cLQx4.jpg) | 向右滑动 | ![](https://i.loli.net/2021/08/17/gLzVIXidaK62Dy7.jpg) | 地图缩小 |

## 进度安排

- [x] 确认用于交互的手势序列。
- [x] 确认`camera.py`的正确性，使用`acquisition.py`采集一些电脑摄像头拍摄的数据（采集多种手势，包括交互的与其他的）。
- [x] 数据标注，训练手的目标检测模型【待测试】。
- [ ] 捕获目标手，取相同序列数组成数据集进行标注，训练手势分类模型。
- [ ] 交互手势的检测与识别组合验证。
- [ ] 搭建可用于参数调节的简单web地图。
- [ ] 组合功能。

## 数据集

我们使用来自联想小新笔记本摄像头采集的数据，使用labelImg标注为VOC格式，共1011张。场景、环境和人物单一，仅作为测试使用，不提供数据集下载。数据组织参考PaddelX下的[PascalVOC](https://github.com/PaddlePaddle/PaddleX/blob/develop/docs/data/format/detection.md)数据组织方式。

## 模型

使用超轻量级[PPYOLO Tiny](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.2/configs/ppyolo/README_cn.md)，模型大小小于4MB，随便训练了100轮后保留best_model作为测试模型。模型文件上传使用[LFS](https://git-lfs.github.com/)。

## 交流与反馈

Email：nanyibrigade@163.com
