import os

# 操作系统
print(os.name)
# print(os.uname) windows不提供
# 环境变量
print(os.environ)
# 具体环境变量
print(os.environ.get('JAVA_HOME'))
# 文件目录
print(os.path.abspath('.'))
# 添加路径 不能创建不存在的目录
os.path.join('L:\gh', 'new')
# 创建文件夹 已经存在文件夹会报错
# os.mkdir('L:\gh\\new')
# 删除文件夹
# os.rmdir('L:\gh\\new')

# 不要求文件真实存在
print(os.path.split('L:\gh\\new'))
print(os.path.split('L:\gh\\new\\a.txt'))
print(os.path.splitext('L:\gh\\new'))
print(os.path.splitext('L:\gh\\new\\a.txt'))

# 重命名
# os.rename('L:\gh\\new', 'L:\gh\old')
# 删除文件
# os.remove('L:\gh\old')

print([ x for x in os.listdir('L:\po') if os.path])

