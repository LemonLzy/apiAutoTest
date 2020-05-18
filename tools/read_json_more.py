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
     3、预期格式为列表嵌套元祖[(url,mobile,code...)]，目前返回字典
     4、多个参数预期格式为列表嵌套元祖[(url,mobile,code...),(url,mobile,code...)]，目前返回字典
解决：1、封装
     2、使用参数替换静态写死的文件名
     3、读取字典内容，并添加到新的列表中
     4、可以利用字典中values方法读取所有值
"""


class ReadJson(object):

    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="UTF-8") as f:
            # 调用json.load方法加载文件流
            return json.load(f)


if __name__ == '__main__':
    # print(ReadJson("login.json").read_json())
    datas = ReadJson("login_more.json").read_json()
    arrs = []
    # 使用遍历获取所有values
    for data in datas.values():
        arrs.append((data.get("url"),
                    data.get("mobile"),
                    data.get("code"),
                    data.get("expect_result"),
                    data.get("status_code")))
    print(arrs)
