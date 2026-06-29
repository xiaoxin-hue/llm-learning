import json
from student import Student
#创建学生对象
stu = Student("小明",15,"女")
#1.将对象属性转为字典，写入json文件
# ========== 第一部分：将学生对象数据转为字典，写入JSON文件保存 ==========
# 定义字典，存储学生的所有信息（json只能存基础数据，不能直接存自定义对象，所以转字典）
stu_dict={
    "name":stu.name,
    "age":stu.age,
    "gender":stu.gender,
    "school":Student.school,
}   
# 写入json
with open("student_data.json","w",encoding = "utf-8")as f:
    # 将字典stu_dict写入文件f
    # ensure_ascii=False：正常显示中文，不转义Unicode编码
    # indent=2：json内容缩进2空格，格式化显示，方便阅读
    json.dump(stu_dict,f,ensure_ascii=False,indent=2)
# 2.读取json文件,还原数据
with open("student_data.json","r",encoding="utf-8")as f:
    load_data = json.load(f)
print("从文件读取的学生信息：",load_data)
#根据读取的数据重建学生对象
new_stu = Student(load_data["name"], load_data["age"], load_data["gender"])
print(new_stu.show_info())