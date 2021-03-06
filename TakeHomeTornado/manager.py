import tornado.ioloop
import tornado.web
import asyncio

from log import logger
from service import UploadImgOcrService


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class UploadImgHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST,GET,OPTIONS,PUT,DELETE')

    def get(self):
        self.write("upload_message")

    def post(self):
        logger.info("start upload img file ")
        result = None
        try:
            file = self.request.files.get('uploadFile', None)
            file_name = file[0].get("filename", '')
            file_content = file[0].get("body", '')
            service = UploadImgOcrService()
            result = service.save_upload_img(img_name=file_name, file_content=file_content)
            if not result:
                result = {"result": "parse None"}
        except Exception as e:
            logger.error("upload img file error: {}".format(e))
            result = {"result": "parse error"}

        finally:
            logger.info("parse upload img file result: {}".format(result))
            return self.write(result)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/upload_img", UploadImgHandler),
    ])


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = make_app()
    app.listen(8999)
    tornado.ioloop.IOLoop.current().start()
