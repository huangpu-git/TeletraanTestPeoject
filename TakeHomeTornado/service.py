# -*- coding: utf-8 -*-


import os
import pytesseract
from PIL import Image
from log import logger
from model import TakeHomeOcrModel


class UploadImgOcrService(object):
    """
    上传图片文件ocr解析 service
    """

    def __init__(self):
        cur_path = os.getcwd()
        self.img_path = cur_path + os.sep + 'img' + os.sep
        self.take_home_ocr_model = TakeHomeOcrModel()

    def save_upload_img(self, img_name, file_content):
        """
        保存上传的图片
        :param img_name:
        :param file_content:
        :return:
        """

        parse_result = None
        file_save_path = self.img_path + img_name
        try:
            with open(file_save_path, "wb") as f:
                f.write(file_content)
            # 解析图片
            parse_result = self.parse_img_ocr(img_name)
        except Exception as e:
            logger.error("write upload img file fail : {}".format(e))
        return parse_result

    def parse_img_ocr(self, img_name):
        """
        OCR解析图片
        :param img_name:
        :return:
        """
        result = {}
        text = []
        try:
            # pytesseract.pytesseract.tesseract_cmd = 'D:/software/tesseract_ocr/Tesseract-OCR/tesseract.exe'
            content = pytesseract.image_to_string(Image.open(self.img_path + img_name), lang='chi_sim')
            for letter in content.replace('\n', '').split(' '):
                text.append(letter)
            result['content'] = text

            # 将识别结果存入数据库
            self.take_home_ocr_model.insert_data(result)
        except Exception as e:
            logger.error("parse upload img file fail : {}".format(e))
        return result


if __name__ == '__main__':
    file_name = 'test.jpg'
    service = UploadImgOcrService()
    result = service.parse_img_ocr(file_name)
    print(result)
