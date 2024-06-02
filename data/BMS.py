import os

# 定义一个全局变量，用来保存图书的信息，方法各个函数之间进行访问
books = []



# 菜单函数
def menu():
    print("****************************************")
    print("*				图书管理系统			 *")
    print("*  	    1. 添加新图书信息              *")
    print("* 	    2. 通过图书ID修改图书信息		 *")
    print("*		3. 通过图书ID删除图书信息		 *")
    print("*		4. 通过书名删除图书信息		 *")
    print("* 	    5. 通过图书ID查询图书信息          *")
    print("*		6. 通过书名查询图书信息          *")
    print("*		7. 显示所有图书信息             *")
    print("*		8. 退出系统			  		 *")
    print("****************************************")
    select_op = input("输入编号选择操作：")
    return select_op

# 加载文件
def load_data():
    print("数据从文件加载完毕！！")
    # 判断文件是否存在
    if os.path.exists("books.txt"):
        with open("books.txt", "r") as file:
            content = file.read()
            content = content.split("\n")
            content.remove("")
            for line in content:
                line = line.split("_")
                book = {}
                book["sid"] = line[0]
                book["name"] = line[1]
                book["price"] = int(line[2])
                book["summary"] = line[3]
                books.append(book)


# 保存文件
def save_data():
    print("将数据写入文件保存完毕！！")
    with open("books.txt", "w") as file:
        for book in books:
            # 使用 - 做为间隔符拼接所有的数据
            book = list(book.values())
            book = [str(el) for el in book]
            bookStr = "_".join(book) + '\n'
            file.write(bookStr)


# 获取图书ID
def getSid():
    sid = input("请输入图书ID:")
    return sid

# 获取书名
def getName():
    name = input("请输入图书书名：")
    return name

# 获取价格
def getPrice():
    while True:
        price = input("请输入图书价格：")
        if price.isdigit():
            return int(price)
        else:
            print("输入价格不合法，请输入数字")

# 获取简介
def getSummary():
    summary = input("请输入图书简介：")
    return summary

# 定义一个用来判断sid对应的数据是否存在的函数
def is_exist(sid):
    for s in books:
        if s["sid"] == sid:
            return s
    else:
        return None


# 添加图书
def addBook(sid, name, price, summary):
    # 如果sid不存在，添加新书，如果存在，提示失败
    result = is_exist(sid)
    if result:
        print("图书ID已存在，添加失败")
        return "添加失败"
    else:
        book = {"sid": sid, "name": name, "price": price, "summary": summary}
        books.append(book)
        print("添加图书信息成功")
        return '添加成功'

    # for s in books:
    #     if s["sid"] == sid:
    #         print("图书ID已存在，添加失败")
    #         return "添加失败"
    # else:
    #     book = {"sid": sid, "name": name, "price": price, "summary": summary}
    #     books.append(book)
    #     print("添加图书信息成功")
    #     return '添加成功'

# 通过图书ID修改图书信息
def modifyBookByID(sid):
    result = is_exist(sid)
    if result:
        name = getName()
        price = getPrice()
        summary = getSummary()
        result["name"] = name
        result["price"] = price
        result["summary"] = summary
        print("修改成功")
        return "修改成功"
    else:
        print(f'没有 {sid} 对应的图书信息')
        return "修改失败"
    # for s in books:
    #     if s["sid"] == sid:
    #         name = getName()
    #         price = getPrice()
    #         summary = getSummary()
    #         s["name"] = name
    #         s["price"] = price
    #         s["summary"] = summary
    #         print("修改成功")
    #         return "修改成功"
    # else:
    #     print(f'没有 {sid} 对应的图书信息')
    #     return "修改失败"

# 通过ID删除图书信息
def deleteBookByID(sid):
    for s in books:
        if s["sid"] == sid:
            books.remove(s)
            print("删除成功")
            return "删除成功"
    else:
        print(f'没有 {sid} 对应的图书信息')
        return "删除失败"

# 通过图书书名 删除所有符合的图书
def deleteBookByName(name):
    exist_s = []
    # 找出所有要删除的图书
    for s in books:
        if s['name'] == name:
            exist_s.append(s)

    # 开始删除
    if len(exist_s) > 0:
        for s in exist_s:
            books.remove(s)
            print(f"图书ID { s['sid'] } 的图书删除成功")
        else:
            print(f"成功删除 {len(exist_s)} 个图书")
            return "删除成功"
    else:
        print("图书不存在，无法删除")
        return "删除失败"

# 通过图书ID查询图书信息
def queryBookByID(sid):
    for s in books:
        if s["sid"] == sid:
            print(f"图书ID {sid} 的图书信息如下：")
            print(s)
            return "查询成功"
    else:
        print(f"图书ID {sid} 的图书不存在")
        return "查询失败"

# 通过书名查询图书信息
def queryBookByName(name):
    result = []
    for s in books:
        if s["name"] == name:
            result.append(s)

    if len(result) > 0:
        print(f"书名为 {name} 的图书共 {len(result)} 名，信息如下：")
        for s in result:
            print(s)
        return "查询成功"
    else:
        print(f"书名为 {name} 的图书不存在")
        return "查询失败"

# 显示所有图书信息
def show():
    print("所有图书信息如下：")
    for s in books:
        print(s)

# 管理函数
def bookManager():
    load_data()
    while True:
        select_op = menu()
        if len(select_op) == 1 and select_op in "12345678":
            if select_op == "1":
                sid = getSid()
                name = getName()
                price = getPrice()
                summary = getSummary()
                addBook(sid, name, price, summary)
            elif select_op =="2":
                sid = getSid()
                modifyBookByID(sid)
            elif select_op =="3":
                sid = getSid()
                deleteBookByID(sid)
            elif select_op =="4":
                name = getName()
                deleteBookByName(name)
            elif select_op =="5":
                sid = getSid()
                queryBookByID(sid)
            elif select_op =="6":
                name = getName()
                queryBookByName(name)
            elif select_op =="7":
                show()
            else:
                save_data()
                break

        else:
            print("输入的数据不合法，请输入在合法范围内的操作编号！！！")

# 程序入口
if __name__ == '__main__':
    bookManager()

    # book = {"sid": "b01", "name": "python", "price": 99, "summary": "Python Basic"}
    # # "_".join([str(val) for val in book.values()])
    # book = list(book.values())
    # book = [str(el) for el in book]
    # print(book)
    # print("-".join(book))

    # nums = [n*n for n in range(10)]
    # print(nums)



