
"""
给定一个字符串 s = "hello python, hello world"，统计每个字符出现的次数（忽略空格和标点，只考虑字母），并返回一个字典。
要求： 忽略大小写（如 'H' 和 'h' 视为同一个字符）。
示例输出： {'h':2, 'e':2, 'l':5, 'o':4, 'p':1, 'y':1, 't':1, 'n':1, 'w':1, 'r':1, 'd':1}
"""

"""s = "hello python, Hello world"
char_count={}
for char in s:
    if char.isalpha():
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] +=1
        else:
            char_count[lower_char] =1
print(char_count)


from collections import Counter

filtered_char = [char_is.lower() for char_is in s if char_is.isalpha()]
count_dict = dict(Counter(filtered_char))

print(count_dict)"""

"""题目2：列表去重并保持顺序
编写一个函数 unique_preserve(lst)，接收一个列表，返回去除重复元素后的新列表，且元素顺序保持不变。
示例： unique_preserve([3,1,2,1,3,4]) → [3,1,2,4]"""

"""def unique_preserve(lst):
    seen = set()
    reslt =[]
    for item in lst:
        if item not in seen:
            seen.add(item)
            reslt.append(item)
    return reslt
"""

"""
题目3：深拷贝与浅拷贝
已知 original = [[1,2], [3,4]]，分别用浅拷贝和深拷贝得到 copy1 和 copy2，
然后修改 copy1[0][0] = 99，copy2[0][0] = 88。请写出修改后 original、copy1、copy2 的值，并解释原因。
"""
from copy import deepcopy
original = [[1,2], [3,4]]
copy1 = original[:]
copy2 = deepcopy(original)
copy1[0][0] = 99
copy2[0][0] =88

# print(original) #[[99,2],[3,4]]
# print(copy1) #[[99,2],[3,4]]
# print(copy2) #[[88,2], [3,4]]


"""
题目1：编写装饰器 retry
编写一个装饰器 retry(max_attempts=3)，当被装饰的函数抛出异常时，自动重试最多 
max_attempts 次，每次重试前等待1秒。如果所有重试都失败，则抛出最后一次异常。
"""
"""import time
def retry(max_attempts):
    def dectory(func):
        def wrapper(*args,**kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    if i == max_attempts-1:
                        raise
                    time.sleep(1)
            return None
        return wrapper
    return dectory

@retry(2)
def random_test():
    import random
    if random.random()<0.5:
        raise ValueError("失败")
    return "成功"""


"""
题目2：设计一个 BankAccount 类
要求：属性：owner (字符串), balance (浮点数，默认0)
方法：deposit(amount)：存款，增加余额，打印新余额
withdraw(amount)：取款，如果余额不足则抛出 ValueError（异常信息 "余额不足"），否则减少余额并打印
__str__：返回 "账户持有人: xxx, 余额: xxx"
创建对象并进行存取操作，处理可能出现的异常。
"""

class BankAccount:
    def __init__(self,owner,balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount <0:
            print("余额必须为正")
        else:
            self.balance +=amount
        print(f"存款后余额为：{self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("余额不足")
        self.balance -=amount
        print(f"取款成功余额:{self.balance}")
    def __str__(self):
        return f"账户持有人: {self.owner}, 余额: {self.balance}"
if __name__ == '__main__':
    zhang = BankAccount("展示",10000)
    zhang.deposit(10000)
    zhang.withdraw(99999999)
    print(zhang.__str__())
