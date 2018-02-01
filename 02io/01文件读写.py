# 一次全部读取 try catch
try:
    f = open('./00read', 'r')
    print(f.read())
finally:
    if f:
        f.close()

print('--------------')

# 一次全部读取 with
with open('./00read', 'r') as f:
    print(f.read())

print('--------------')

# 按行读取
with open('./00read', 'r') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

# 读取后返回list
with open('./00read', 'r', encoding='UTF-8') as f:
    print(f.readlines())

# 按字节读取
with open('./00read', 'r', encoding='UTF-8', errors='ignore') as f:
    print(f.read(1))

# 读取图片
with open('./00image.png', 'rb') as f:
    print(f.read())

# 覆盖写入文件
with open('./00write', 'w', encoding='UTF-8') as f:
    f.write('to read 哈哈')

# 追加写入文件
with open('./00write', 'a', encoding='UTF-8') as f:
    f.write('to read 哈哈')

# 不是相同编码读取会乱码
with open('./00write', 'r', encoding='UTF-8') as f:
    print(f.read())

