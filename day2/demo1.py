#类的定义与使用
class Student:
    #类属性
    school= "第一中学"
    #构造方法
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #示例方法
    def introduce(self):
        return f"我是{self.name}，今年{self.age}岁了。"
    
    #类方法
    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school
    #静态方法
    @staticmethod
    def is_adult(age):
        return age >= 18
#创建对象
student1 = Student("小明", 16)
print(student1.introduce())  # 输出：我是小明，今年16岁了。
print(student1.school)  # 输出：第一中学
#调用类方法修改类属性
Student.change_school("第二中学")
print(student1.school)  # 输出：第二中学
#调用静态方法
print(Student.is_adult(16))  # 输出：False
print(Student.is_adult(18))  # 输出：True

