# student.py
class Student:
    school = "实验中学"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        return f"姓名：{self.name}，年龄：{self.age}，性别：{self.gender}"

    @classmethod
    def modify_school(cls, new_name):
        cls.school = new_name

    @staticmethod
    def check_age(age):
        return age >= 12