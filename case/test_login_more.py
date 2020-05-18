"""
完成登录业务层实现
"""

import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson


# 读取数据函数
def get_data():
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
    return arrs


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self, url, mobile, code, expect_result, status_code):
        # url = "http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        # mobile = "15717328898"
        # code = "150052"

        login = ApiLogin().api_post_login(url, mobile, code)
        print("查看响应结果：", login.json())
        self.assertEqual(expect_result, login.json()['message'])
        self.assertEqual(status_code, login.status_code)


if __name__ == '__main__':
    unittest.main()

"""
获取验证码：http://ttapi.research.itcast.cn/app/v1_0/sms/codes/15717328898
token：eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODkzODg0MjMsInVzZXJfaWQiOjEyNjA1ODIzMzE5NjY1NTQxMTIsInJlZnJlc2giOmZhbHNlfQ.L8OdfH29Mtp3GjPzzMye5AnYSyvkT2HXczn_8LxgBjA
"""
