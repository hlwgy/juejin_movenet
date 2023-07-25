# 掘金文章配套代码
姿态估计

## 材料下载地址
https://pan.baidu.com/s/11CyuVcQ3u86C6Y9nAetQ2Q?pwd=8xe2 提取码: 8xe2 

## 文件说明

```
JueJin_MoveNet
  |--- python py代码
  |--- tflite模型文件
    |--- movenet_lightning.tflite 轻量级模型，它快
    |--- movenet_thunder.tflite 进准级别模型，它准
    |--- movenet_multipose.tflite 多人模型，最多支持6人检测
    |--- classifier.tflite 分类模型，这是一个瑜伽工作分类
    |--- labels.xt 分类模型的种类列表
    |--- posenet.tflite 上一代老前辈posnet，这一代叫movenet
  |--- tf_app-release.apk
  |--- ios源码
  |--- android源码（含模型）
```

- tflite模型文件：包含多种类型的movenet模型，可选择使用。
- python：包含python调用movenet的示例代码，也包含示例模型。
- ios源码：需要参照文档，将模型引入。
- android源码（含模型）：Android项目，已包含模型。
- tf_app-release.apk：可直接运行的Android示例程序。
