#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : paulinelee
# @Time     : 2024/5/25 19:09
# @File     : define_class.py
# @Project  : pytest_00

"""通过定义两个类：一个类用来定义数据，另一个类用来管理数据
"""


class Bk:
    def __init__(self, bk_id, bk_name, bk_price, bk_summary):
        self.__bd_book_id = bk_id
        self.__bd_book_name = bk_name
        self.__bd_book_price = bk_price
        self.__bd_book_summary = bk_summary

    def __str__(self):
        return (f"id{self.__bd_book_id}的书{self.__bd_book_name}的价格{self.__bd_book_price},简介是{self.__bd_book_summary}")
        # return "123"

    def set_bk_id(self, bk_id):
        self.__bd_book_id = bk_id

    def get_bk_id(self):
        return self.__bd_book_id

    def set_bk_name(self, bk_name):
        self.__bd_book_name = bk_name

    def get_bk_name(self):
        return self.__bd_book_name

    def set_bk_price(self, bk_price):
        self.__bd_book_price = bk_price

    def get_bk_price(self):
        return self.__bd_book_price

    def set_bk_summary(self, bk_summary):
        self.__bd_book_summary = bk_summary

    def get_bk_summary(self):
        return self.__bd_book_summary


class BookManagement:
    def __init__(self):
        self.__books = []

    def __menu(self):
        """打印所有可以输入的序号"""
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
        select_op = input("请输入1-8中你想要的数字")
        return select_op

    def __get_book_id_input(self):
        bk_id = input("请输入book id: ")
        return bk_id

    def __get_book_name_input(self):
        bk_name = input("请输入book name: ")
        return bk_name

    def __get_book_price_input(self):
        bk_price = input("请输入book price: ")
        return bk_price

    def __get_book_summary_input(self):
        bk_summary = input("请输入book summary: ")
        return bk_summary

    # def __save_data(self):
    #     with open('../data/params.csv', 'w') as f:

    def __add_book(self, book_id, book_name, book_price, book_summary):
        for book in self.__books:
            if book.get_bk_id() == book_id:
                print(f"{book_id}存在")
                return "添加失败"
        else:
            book = Bk(bk_id=book_id, bk_name=book_name, bk_price=book_price, bk_summary=book_summary)
            self.__books.append(book)
            print("添加成功")
            return "添加成功"

    def __modify_book_by_book_id(self, book_id):
        for book in self.__books:
            if book.get_bk_id() == book_id:
                print("你查询的书存在，现在可以开始修改了")
                book_name = self.__get_book_name_input()
                book_price = self.__get_book_price_input()
                book_summary = self.__get_book_summary_input()
                book.set_bk_name(book_name)
                book.set_bk_price(book_price)
                book.set_bk_summary(book_summary)
                return "修改成功"
            else:
                print(f"查询不到当前的书{book_id}")

    # def

    def __get_all_books(self):
        for book in self.__books:
            print(book)

    def manager(self):
        """管理方法"""
        while True:
            select_op = self.__menu()
            if len(select_op) == 1 and select_op in "12345678" and select_op.isdigit():
                if select_op == "1":
                    book_id = self.__get_book_id_input()
                    book_name = self.__get_book_name_input()
                    book_price = self.__get_book_price_input()
                    book_summary = self.__get_book_summary_input()
                    self.__add_book(book_id, book_name, book_price, book_summary)

                elif select_op == "2":
                    book_id = self.__get_book_id_input()
                    self.__modify_book_by_book_id(book_id)
                elif select_op == "3":
                    pass
                elif select_op == "4":
                    pass
                elif select_op == "5":
                    pass
                elif select_op == "6":
                    pass
                elif select_op == "7":
                    self.__get_all_books()
                else:
                    print("什么函数都不用执行，直接退出")
                    break

            else:
                print("输入的数字不在可选范围内")


if __name__ == '__main__':
    b = BookManagement()
    b.manager()
