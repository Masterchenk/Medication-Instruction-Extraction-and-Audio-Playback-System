import os
from paddleocr import PaddleOCR



os.environ['KMP_DUPLICATE_LIB_OK']='True'

# 初始化OCR模型
ocr = PaddleOCR(use_angle_cls=True, use_gpu=True, lang="ch")  # 使用中文识别
def extract_text_from_images(img_path):

    result = ocr.ocr(img_path, cls=True)  # 对图片进行OCR识别
    text_result = ""
    for idx in range(len(result)):
        res = result[idx]
        # for line in res:
        text_with_confidence = res[1]  # 文本和置信度元组
        text = text_with_confidence[0]  # 提取识别出的文本
        text_result += text + "\n"

    return text_result
