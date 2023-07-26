## 掘金文章配套python代码
本仓库的文件结构说明
```
tflite 模型文件
  |--- movenet_lightning.tflite 轻量级模型，它快
  |--- movenet_thunder.tflite 精准级别模型，它准
  |--- classifier.tflite 分类模型，这是一个瑜伽动作的分类模型
  |--- labels.xt 分类模型的种类列表
data.py 数据定义
classifier.py 动作分类库
movenet.py 姿势预测类库
main.py 演示入口类，调用类库
test.jpeg 测试图片
```

类库支持：numpy、cv2
```
pip install numpy
pip install opencv-python
```

## 其他平台代码
https://pan.baidu.com/s/11CyuVcQ3u86C6Y9nAetQ2Q?pwd=8xe2 提取码: 8xe2 
```
JueJin_MoveNet
  |--- tflite模型文件
    |--- movenet_lightning.tflite 轻量级模型，它快
    |--- movenet_thunder.tflite 精准准级别模型，它准
    |--- movenet_multipose.tflite 多人模型，最多支持6人检测
    |--- classifier.tflite 分类模型，这是一个瑜伽工作分类
    |--- labels.xt 分类模型的种类列表
    |--- posenet.tflite 上一代老前辈posnet，这一代叫movenet
  |--- tf_app-release.apk
  |--- ios源码
  |--- android源码（含模型）
```

- tflite模型文件：包含多种类型的movenet模型，可选择使用。
- ios源码：需要参照文档，将模型引入。
- android源码（含模型）：Android项目，已包含模型。
- tf_app-release.apk：可直接运行的Android示例程序。
