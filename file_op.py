# 文件操作

# 文本读(r) 文本覆盖写(w) 二进制读(rb) 二进制写(wb) 追加写(a)

# 读写文件, 需要显示关闭文件, 用 with 语句可以省略 close() 调用
with open('test.txt', 'r', encoding='utf8') as f:
    print(f.read())

    # 读到空行, 返回的是换行符, 读到文件末尾返回的是空字符串
    f.readline()