from io import StringIO

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World')
print(f.getvalue())

f = StringIO('Hello\nWorld')
while True:
    s = f.readline()
    if s == '':
        break
    print(s)
    # print(s.strip()) #去除空格


from io import BytesIO

f = BytesIO()
f.write('测试'.encode('UTF-8'))
print(f.getvalue())
print(f.getvalue().decode('UTF-8'))
print(f.getvalue().decode('GBK'))