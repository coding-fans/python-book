# -*- encoding=utf8 -*-

# 提示用户输入分数，获取用户输入内容，并保存到变量 data
data = input('请输入分数：')

# 将用户输入分数从字符串转成整数数值，并保存到变量 score
score = int(data)

if score >= 90:
    print('优秀')
elif score >= 70:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
