# 正常登录
success = ("18684720553", "python")

# 登录失败-异常数据 用户名为空、密码为空、用户名格式不正确
cases = [
    {"user": "18684720553", "password": "", "check": "请输入密码"},
    {"user": "", "password": "python", "check": "请输入手机号"},
    {"user": "1868472055", "password": "", "check": "请输入正确的手机号"},
]
