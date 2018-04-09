# 覆盖写入文件
with open('./sql.sql', 'w', encoding='UTF-8') as ff:
    ff.write("# 01--> start Unsellable BIN sql")
    with open('./002_Unsellable_BIN', 'r') as f:
        while True:
            line = f.readline()
            ff.write(line)
            if not line:
                break
    ff.write("# 01--> end Unsellable BIN sql")

    # 读取后返回list
    # with open('./002_Unsellable_BIN', 'r', encoding='UTF-8') as f:
    #     print(f.readlines())

    print("03--> start RMA Sellable Tote sql")
    i = 0
    while i < 10000:
        i = i + 1
        if i < 10:
            s = "000"+str(i)
        elif i < 100:
            s = "00"+str(i)
        elif i < 1000:
            s = "0"+str(i)
        elif i < 10000:
            s = str(i)
        print("RMAG" + s)

    print("03--> end RMA Sellable Tote sql")

    print("04--> start RMA Unsellable Tote sql")
    i = 0
    while i < 100:
        i = i + 1
        if i < 10:
            s = "000"+str(i)
        elif i < 100:
            s = "00"+str(i)
        elif i < 1000:
            s = "0"+str(i)
        elif i < 10000:
            s = str(i)
        print("RMAN" + s)

    print("04--> end RMA Unsellable Tote sql")

    print("04--> start RMA Unsellable Tote sql")

    print("RMAN")

    print("04--> end RMA Unsellable Tote sql")

