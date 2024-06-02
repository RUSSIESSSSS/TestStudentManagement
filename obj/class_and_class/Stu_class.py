# !/usr/bin/env python3


# -*- coding: utf-8 -*-
# @Author   : paulinelee
# @Time     : 2024/5/28 09:22
# @File     : Stu_class.py
# @Project  : pytest_00

class Student:
    def __init__(self, student_id, student_name, student_age, student_gender):
        self.__std_id = student_id
        self.__std_name = student_name
        self.__std_age = student_age
        self.__std_gender = student_gender

    def __str__(self):
        return f"{self.__std_id}编号的{self.__std_name},性别是：{self.__std_gender},年龄是:{self.__std_age}"

    def set_std_id(self, std_id):
        self.__std_id = std_id

    def get_std_id(self):
        return self.__std_id

    def set_std_name(self, std_name):
        self.__std_name = std_name

    def get_std_name(self):
        return self.__std_name

    def set_std_age(self, std_age):
        self.__std_age = std_age

    def get_std_age(self):
        return self.__std_age

    def set_std_gender(self, std_gender):
        self.__std_gender = std_gender

    def get_std_gender(self):
        return self.__std_gender


class StudentManagement:
    def __init__(self):
        self.__students = []

    def __menu(self):
        print("*****************************")
        print("*      图书管理系统           *")
        print("* 1. 添加新图书信息           *")
        print("* 2. 通过图书ID修改图书信息      *")
        print("* 3. 通过图书ID删除图书信息      *")
        print("* 4. 通过书名删除图书信息      *")
        print("* 5. 通过图书ID查询图书信息      *")
        print("* 6. 通过书名查询图书信息      *")
        print("* 7. 显示所有图书信息         *")
        print("* 8. 退出系统                *")
        print("*****************************")
        select_op = input("请在1~8中选择一个数字并输入： ")
        return select_op

    def add_student(self, std_id, std_name, std_gender, std_age):
        """添加学生信息"""
        for student in self.__students:
            if student.get_std_id() == std_id:
                print("当前输入的学生信息存在，添加失败")
        else:
            std_instance = Student(student_id=std_id, student_gender=std_gender, student_name=std_name,
                                   student_age=std_age)
            self.__students.append(std_instance)
            print("学生信息添加成功")
            return "添加成功"

    def __get_std_id_input(self):
        """get std_id"""
        std_id = input("输入std_id")
        return std_id

    def __get_std_name_input(self):
        """get std_name"""
        std_name = input("输入std_name")
        return std_name

    def __get_std_gender_input(self):
        std_gender = input("输入std_gender")
        return std_gender

    def __get_std_age_input(self):
        std_age = input("输入std_age")
        return std_age

    def get_all_stds(self):
        for std in self.__students:
            print("以下就是所有std信息")
            print(std)
            return "返回了当前所有学生信息"

    def modify_student_info_by_id(self, std_id, std_name, std_gender, std_age):
        for std in self.__students:
            if std.get_std_id() == std_id:
                print("当前学生存在，可以进行修改")
                std_name = std_name
                std_gender = std_gender
                std_age = std_age
                std.set_std_name(std_name)
                std.set_std_age(std_age)
                std.set_std_gender(std_gender)
                return "修改成功"
        else:
            print("修改失败，请重新进入修改")
            return "修改失败"

    def del_student_info_by_id(self, std_id):
        """通过学生id删除学生信息"""
        del_stds = []
        for std in self.__students:
            if std.get_std_id() == std_id:
                print(f"已找到当前{std.get_std_id()}这个人，准备把找到的人全部放在待删除列表中")
                del_stds.append(std)

            for del_std in del_stds:
                self.__students.remove(del_std)
                print("删除成功")
                return "删除成功"

    def del_student_info_by_name(self, std_name):
        """通过学生姓名删除学生信息"""
        for std in self.__students:
            del_stds = []
            if std.get_std_name == std_name:
                del_stds.append(std)

            for del_std in del_stds:
                self.__students.remove(del_std)
                print("删除成功")
                return "删除成功"

    def get_stds_info_by_std_id(self, std_id):
        """通过学生id查询学生信息"""
        query_list = []
        for std in self.__students:
            if std.get_std_id == std_id:
                print("当前学生id存在，正在查询中")
                query_list.append(std)
                print(f"当前查询到的学生为：{query_list}")
                return "查询成功"
            else:
                print("当前输入的学生id不存在")
                return "查询失败"

    def get_stds_info_by_std_name(self, std_name):
        for std in self.__students:
            query_list = []
            if std.get_std_name == std_name:
                print("查询当前学生存在")
                query_list.append(std)
                print(f"当前查询到的学生为:{query_list}")
                return "查询成功"
            else:
                print("当前输入的学生id不存在")
                return "查询失败"

    def __load_data(self):
        """读取文件"""
        import os
        if os.path.exists('../../data/params.csv'):
            with open("../../data/params.csv", 'r') as f:
                content = f.read()
                content = content.split("\n")
                content.remove("")
                for line in content:
                    line = line.split('-')
                    std = {}
                    std["std_id"] = line[0]
                    std["std_name"] = line[1]
                    std["std_gender"] = line[2]
                    std["std_age"] = line[3]
                    self.__students.append(std)

    def __save_data(self):
        """存储数据到文本中"""
        with open("../../data/params.csv", 'r') as f:
            for std in self.__students:
                std = list(std.values)
                std = [str(e) for e in std]
                std_str = '-'.join(std) + '\n'
                f.write(std_str)

    def manager(self):
        while True:

            select_op = self.__menu()
            if len(select_op) > 0 and select_op in "12345678" and select_op.isdigit():
                if select_op == "1":
                    print("执行 【添加学生信息】")
                    std_id = self.__get_std_id_input()
                    std_name = self.__get_std_name_input()
                    std_gender = self.__get_std_gender_input()
                    std_age = self.__get_std_age_input()
                    self.add_student(std_id=std_id, std_name=std_name, std_gender=std_gender, std_age=std_age)
                elif select_op == "2":
                    print("执行 【通过学生ID修改学生信息】")
                    std_id = self.__get_std_id_input()
                    std_name = self.__get_std_name_input()
                    std_gender = self.__get_std_gender_input()
                    std_age = self.__get_std_age_input()
                    self.modify_student_info_by_id(std_id, std_name, std_gender, std_age)
                elif select_op == "3":
                    std_id = self.__get_std_id_input()
                    print("执行 【通过学生ID删除学生信息】")
                    self.del_student_info_by_id(std_id=std_id)
                elif select_op == "4":
                    std_name = self.__get_std_name_input()
                    print("执行 【通过学生姓名删除学生信息】")
                    self.del_student_info_by_name(std_name)
                elif select_op == "5":
                    print("执行 【通过学生ID查询学生信息】")
                    std_id = self.__get_std_id_input()
                    self.get_stds_info_by_std_id(std_id)
                elif select_op == "6":
                    print("执行 【通过学生姓名查询学生信息】")
                    std_name = self.__get_std_name_input()
                    self.get_stds_info_by_std_name(std_name)
                elif select_op == "7":
                    self.get_all_stds()
                else:
                    print("退出系统")
                    break
            else:
                print("输入不合法")


if __name__ == '__main__':
    StudentManagement().manager()
