"""
完成登录业务层实现
"""

import unittest
from api.api_login import ApiLogin


class TestLogin(unittest.TestCase):
    def test_login(self):
        url = "http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        mobile = "15717328898"
        code = "150052"

        login = ApiLogin().api_post_login(url, mobile, code)
        print("查看响应结果：", login.json())
        self.assertEqual("OK", login.json()['message'])
        self.assertEqual(201, login.status_code)


if __name__ == '__main__':
    unittest.main()


"""
获取验证码：http://ttapi.research.itcast.cn/app/v1_0/sms/codes/15717328898
token：eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODkzODg0MjMsInVzZXJfaWQiOjEyNjA1ODIzMzE5NjY1NTQxMTIsInJlZnJlc2giOmZhbHNlfQ.L8OdfH29Mtp3GjPzzMye5AnYSyvkT2HXczn_8LxgBjA
"""
