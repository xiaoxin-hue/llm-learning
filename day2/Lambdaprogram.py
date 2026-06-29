from functools import reduce
#1.Lambda 表达式-匿名函数(无函数名的表达式)
square =lambda x:x**2
print(square(5))
#2.map - 对可迭代对象每一个元素应用函数
numbers = [1,2,3,4]
squared = list(map(lambda x : x**2,numbers))
print(squared)
#3.filter - 筛选符合条件的元素
evens = list(filter(lambda x : x%2==0,numbers))
print(evens)
#4. reduce - 累积计算（求和，求积）
sum_all  = reduce(lambda a,b:a+b,numbers)
print(sum_all)

#进阶：组合使用
#找出偶数平方后大于10的数
result = list(
    filter(lambda x: x>10,
           map(lambda x: x**2,
               filter(lambda x: x % 2 == 0, numbers)
              )
          )     
)
print(result)