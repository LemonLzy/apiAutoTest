import json

# 打开json文件获取文件流
# with open("../data/login.json", "r", encoding="UTF-8") as f:
#     # 调用json.load方法加载文件流
#     data = json.load(f)
#     print("获取的数据为:", data)

# def read_json():
#     with open("../data/login.json", "r", encoding="UTF-8") as f:
#         # 调用json.load方法加载文件流
#         return json.load(f)
"""
问题：1、未经过封装，无法在其他模块内调用使用 
     2、数据存储文件有好几个，如果写死文件名，在读取别的文件时无法使用
解决：1、封装
     2、使用参数替换静态写死的文件名
"""


class ReadJson(object):

    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="UTF-8") as f:
            # 调用json.load方法加载文件流
            return json.load(f)


if __name__ == '__main__':
    print(ReadJson("login.json").read_json())
