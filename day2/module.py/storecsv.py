import csv
from student import Student
stu = Student("小红",14,"女")
#写入csv
with open("student_data.csv","w",encoding="utf-8",newline="")as f:
    writer = csv.writer(f)
    #写入表头
    writer.writerow(["姓名","年龄","性别","学校"])
    #写入数据
    writer.writerow([stu.name,stu.age,stu.gender,Student.school])
#读取csv
with open("student_data.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for row  in reader:
        print(row)

                     
                     
    
                     