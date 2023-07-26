# %%
# cv2用于图片处理
import cv2
# 导入姿态估计模型
from movenet import Movenet
# 导入姿态分类模型
from classifier import Classifier

# 将检测结果画出来
def draw_result(person, input_image, c_name=""):
    # 分析检测结果
    bounding_box = person.bounding_box # 人物区域
    keypoints = person.keypoints # 17个点的位置
    # output_image = input_image.copy()
    output_image = input_image
    # 把人体圈出来
    if bounding_box is not None:
        start_point = bounding_box.start_point
        end_point = bounding_box.end_point
        cv2.rectangle(output_image, start_point, end_point, (255, 0, 0), 2)
    # 把识别的17个点画出来
    for i in range(len(keypoints)):
        cv2.circle(output_image, keypoints[i].coordinate, 2, (0, 0, 255), 8)

    cv2.imshow("output_image", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 姿势分类，此处以瑜伽动作为例
def pose_classifier(person):
    # 分类模型地址
    cls_model_path = 'tflite/classifier'
    cls_babels = 'tflite/labels.txt' # 分类label
    # 创建模型
    classifier = Classifier(cls_model_path, cls_babels)
    # 进行分类
    categories = classifier.classify_pose(person)
    class_name = categories[0].label
    return class_name
# %%
if __name__ == '__main__':
    # 读入测试图片
    input_image = cv2.imread('test.jpeg')
    # 构建模型
    pose_detector = Movenet('tflite/movenet_thunder')
    # 将图片交给模型检测
    person = pose_detector.detect(input_image)

     # 对检测结果进行瑜伽分类
    # class_name = pose_classifier(person)
    # print(class_name)
    # # 在图像上绘制文本
    # cv2.putText(input_image, class_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
    
    # 对检测结果进行绘制
    draw_result(person, input_image)
   
# %%
