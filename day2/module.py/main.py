# main.py
# 从 student 文件中导入 Student 类
from student import Student

# 正常创建对象、调用方法
stu = Student("赵六", 16, "男")
print(stu.show_info())

Student.modify_school("明德中学")
print("当前学校：", Student.school)
print(Student.check_age(17))