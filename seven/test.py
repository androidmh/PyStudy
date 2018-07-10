print('hello world')

mood = False
if mood:
    print("life is short")
else:
    print('i use python')

ACCOUNT = 'mh'
PASSWORD = '123'

print('请输入账号')
user_account = input()
print('请输入密码')
user_password = input()
if (user_account == ACCOUNT) and (user_password == PASSWORD):
    print('登录成功')
else:
    print('登录失败')
