#1.写入文件
with open('test.txt', 'w',encoding='utf-8') as f:
    f.write("Hello, World!\n")
    f.write("第二行内容")
#2.读取文件
with open('test.txt', 'r',encoding='utf-8') as f:
    content = f.read()
    print("文件内容：", content)
#3.逐行读取
with open("test.txt",'r',encoding='utf-8')as f:
    for line in f:
        print("行：",line.strip())  # strip()去除行末的换行符
#4.追加写入
with open('test.txt', 'a',encoding='utf-8') as f:
    f.write("\n这是追加的内容。")
#5.使用with语句自动关闭文件
with open('test.txt', 'r',encoding='utf-8') as f:
    content = f.read()
    print("更新后的文件内容：", content)