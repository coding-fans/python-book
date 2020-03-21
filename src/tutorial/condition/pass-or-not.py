# -*- encoding=utf8 -*-

# 提示用户输入分数，获取用户输入内容，并保存到变量 data
data = input('请输入分数：')

# 将用户输入分数从字符串转成整数数值，并保存到变量 score
score = int(data)

# 判断分数是否大于等于60
if score >= 60:
    print('成绩及格！')
else:
    print('成绩不及格！')
