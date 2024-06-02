# 1. 定义学生类 `Student`，学生信息包含：
#    - 编号: `sid`
#    - 姓名: `name`
#    - 年龄: `age`
#    - 性别: `gender`
#
# 1. 实现构造方法及对象描述方法
#    - `__init__` : 初始化方法，接收对应参数初始化对象属性
#    - `__str__` ： 实现对象描述方法，输出学生信息

class Student:
    # 构造方法
    def __init__(self, sid, name, age, gender):
        self.__sid = sid
        self.__name = name
        self.__age = age
        self.__gender = gender

    #   存取器方法
    def setSid(self, sid):
        self.__sid = sid

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print("年龄不是数字")

    def setGender(self, gender):
        self.__gender = gender

    # 取方法
    def getSid(self):
        return self.__sid

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    # 对象描述方法,返回且只能返回一个字符串类型的数字
    def __str__(self):
        return f"【学号：{self.__sid}  --  姓名：{self.__name} --  年龄：{self.__age}  --  性别：{self.__gender}】"

#
# 1. 定义管理类 `StudentManagement`，用来实现整体业务逻辑。
#    - 使用列表做为属性保存学生对象信息

class StudentManagement(object):
    def __init__(self):
        self.__students = []

# 1. 定义 `manager` 方法管理业务逻辑
#    - 对用户输入内容进行输入校验
#    - 根据用户输入内容选择不同功能执行

    def manager(self):
        while True:
            select_op = self.__menu()
            if select_op.isdigit() and len(select_op) == 1 and select_op in "12345678":
                if select_op == "1":
                    # 添加学生
                    sid = self.__getSid()
                    name = self.__getName()
                    age = self.__getAge()
                    gender = self.__getGender()
                    self.addStudent(sid, name, age, gender)
                elif select_op == "2":
                    sid = self.__getSid()
                    self.modifyStudentByID(sid)
                elif select_op == "3":
                    sid = self.__getSid()
                    self.deleteStudentByID(sid)
                elif select_op == "4":
                    name = self.__getName()
                    self.deleteStudentByName(name)
                elif select_op == "5":
                    pass
                elif select_op == "6":
                    pass
                elif select_op == "7":
                    self.__show()
                else:
                    break
            else:
                print("输入的功能ID无效，请重新输入")

#
# 1. 实现菜单方法 `__menu`，输出下列菜单信息，并返回用户输入的编号
#
    # ```python
    # print("*****************************")
    # print("*      学生管理系统           *")
    # print("* 1. 添加新学生信息           *")
    # print("* 2. 通过学号修改学生信息      *")
    # print("* 3. 通过学号删除学生信息      *")
    # print("* 4. 通过姓名删除学生信息      *")
    # print("* 5. 通过学号查询学生信息      *")
    # print("* 6. 通过姓名查询学生信息      *")
    # print("* 7. 显示所有学生信息         *")
    # print("* 8. 退出系统                *")
    # print("*****************************")
#     ```

    def __menu(self):
        print("*****************************")
        print("*      学生管理系统           *")
        print("* 1. 添加新学生信息           *")
        print("* 2. 通过学号修改学生信息      *")
        print("* 3. 通过学号删除学生信息      *")
        print("* 4. 通过姓名删除学生信息      *")
        print("* 5. 通过学号查询学生信息      *")
        print("* 6. 通过姓名查询学生信息      *")
        print("* 7. 显示所有学生信息         *")
        print("* 8. 退出系统                *")
        print("*****************************")
        select_op = input("请输入一个功能ID：")
        return select_op

# 1. 因程序中需要多次对编号及姓名进行输入，故抽取方法获取对应的数据。
#    - 获取编号方法 `__getSid`, 输入编号并返回（字符串类型）`eg. s01`
#    - 获取姓名方法 `__getName`, 输入姓名并返回（字符串类型）
#    - 获取姓名方法 `__getAge`, 输入年龄并返回（整型）
#    - 获取姓名方法 `__getGender`, 输入性别并返回（字符串类型）

    def __getSid(self):
        return input("请输入ID:")

    def __getName(self):
        return input("请输入姓名：")

    def __getAge(self):
        while True:
            age = input("请输入年龄:")
            if age.isdigit():
                age = int(age)
                return age
            else:
                print("输入的年龄不合法")

    def __getGender(self):
        return input("请输入性别：")



#
# 1. 实现添加学生方法 `addStudent`
#    - 方法参数为 `编号`，`姓名`，`年龄`，`性别`四个参数
#    - 输出添加操作的结果提示信息
#    - 返回对应结果信息
#    - 要求编号不可重复。

    def addStudent(self, sid, name, age, gender):
        # 通过 ID 判断学号是否重复，
        # 不重复
            # 通过参数构建一个学生对象
        # 重复
            # 提示返回

        for item in self.__students:
            if item.getSid() == sid:
                print(f"学号 {sid} 已存在，不能添加学生信息")
                return "添加失败"
        else:
            stu = Student(sid, name, age, gender)
            self.__students.append(stu)
            print("添加成功")
            return "添加成功"


#
# 1. 实现通过编号修改学生信息方法 `modifyStudentByID`
#    - 参数为 `学号`
#    - 如果学生存在，则进行修改，不存在输出提示信息
#    - 返回是否修改成功
    def modifyStudentByID(self, sid):
        for item in self.__students:
            if item.getSid() == sid:
                # 修改数据
                name = self.__getName()
                age = self.__getAge()
                gender = self.__getGender()
                item.setName(name)
                item.setAge(age)
                item.setGender(gender)
                return "修改成功"
        else:
            print(f"学号 {sid} 不存在，不能修改学生信息")
            return "修改失败"


# 1. 实现通过学号删除学生方法 `deleteStudentByID`
#    - 参数为 `学号`
#    - 如果学生存在，则进行删除并输出提示信息，不存在则仅输出提示
#    - 返回是否删除成功

    def deleteStudentByID(self, sid):
        for item in self.__students:
            if item.getSid() == sid:
                self.__students.remove(item)
                print(f"学号 {sid} 的学生信息删除成功")
                return "删除成功"
        else:
            print(f"学号 {sid} 不存在，不能删除学生信息")
            return "删除失败"

#
# 1. 实现通过姓名删除学生方法 `deleteStudentByName`
#    - 参数为 `姓名`
#    - 如果学生存在，则进行删除（同名学生全部删除）并输出提示信息，不存在则仅输出提示
#    - 返回是否删除成功

    def deleteStudentByName(self, name):
        del_item = []
        for item in self.__students:
            if item.getName() == name:
                del_item.append(item)

        if len(del_item) != 0:
            for item in del_item:
                self.__students.remove(item)
            else:
                print(f"共删除 {len(del_item)} 个名为 {name} 的学生信息")
                del del_item
                return "删除成功"
        else:
            print(f"没有名字为 {name} 的学生信息，无法删除")
            return "删除失败"
#
# 1. 实现通过学号查询学生方法 `queryStudentByID`
#    - 参数为 `学号`
#    - 如果学生存在，则输出学生信息，不存在输出提示信息
#    - 返回是否查询成功
#
# 1. 实现通过姓名查询学生方法 `queryStudentByName`
#    - 参数为 `姓名`
#    - 如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示信息
#    - 返回是否查询成功
#
# 1. 实现显示所有学生信息方法 `__show`
#    - 输出所有学生信息
    def __show(self):
        for item in self.__students:
            print(item)


if __name__ == '__main__':
    StudentManagement().manager()
    # StudentManagement().addStudent("s01","a",22,"a")

