"""
目标：实现登录接口对象封装
"""
import requests


class ApiLogin(object):
    def api_post_login(self, url, mobile, code):
        headers = {"Content-Type": "app;ication/json"}
        data = {"mobile": mobile, "code": code}
        post = requests.post(url, headers=headers, json=data)
        return post


"""
url、mobile、code：最后都需要从data数据文件中读取出来，做参数化使用，所以这里使用动态传参
"""
