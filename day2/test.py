#基础类练习
class Student:
    #类属性
    school = '实验中学'
    #构造方法
    def __init__(self,name,age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        #实例方法
    def show_info(self):
        return f"姓名：{self.name},年龄：{self.age},性别：{self.gender}"
    #类方法：操作属性,参数cls代表类本身
    @classmethod
    def modify_school(cls,new_name) :
        cls.school = new_name
    #静态方法：工具方法，不操作属性
    @staticmethod
    def check_age(age):
        return age >=12
    
#侧式运行
if __name__ == "main":
#创建实例
    stu1 = Student("张三", 13, "男")
    #调用实例方法
    print(stu1.show_info())
    #调用类方法
    Student.modify_school("新实验中学")
    print(Student.school)
    #调用静态方法
    print(Student.check_age(10))    