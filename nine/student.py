#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/10 13:50
# @Author : MengHe
# @File : student.py
# @Software: PyCharm
from nine.human import Human


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        super(Student, self).__init__(name, age)


student = Student('aa', 'hehe', 11)
student.get_name()