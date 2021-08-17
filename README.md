# GBIM

[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/) [![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](LICENSE)

手势交互地图 GBIM(Gesture-Based Interaction map)。可通过电脑摄像头观察使用者的手势变化，进而简单控制地图的交互。

## 手势

| 手势 | 交互     |
| ---- | -------- |
| ？   | 向上滑动 |
| ？   | 向下滑动 |
| ？   | 向左滑动 |
| ？   | 向右滑动 |
| ？   | 放大     |
| ？   | 缩小     |

## 进度安排

- [ ] 确认用于交互的手势序列。
- [x] 确认`camera.py`的正确性，使用`acquisition.py`采集一些电脑摄像头拍摄的数据（采集多种手势，包括交互的与其他的）。
- [ ] 数据标注，训练手的目标检测模型。
- [ ] 捕获目标手，取相同序列数组成数据集进行标注，训练手势分类模型。
- [ ] 交互手势的检测与识别组合验证。
- [ ] 搭建可用于参数调节的简单web地图。
- [ ] 组合功能。

## 交流与反馈

Email：nanyibrigade@163.com
