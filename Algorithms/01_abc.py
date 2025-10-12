# 如果 a+b+c=1000 且 a^2+b^2=c^2 (a,b,c 为自然数)， 如何求出所有a,b,c,的可能组合

# 枚举法
# 思路：
# a = 0,
# b = 0,
# c = 0 --> c = 1 --> c = 2 ... c = 1000

import time
start_time = time.time()
for a in range(0, 101):
    for b in range(0, 101):
        for c in range(0, 101):
            if a+b+c == 100 and a**2 + b**2 == c**2:
                print("a, b, c: %d, %d, %d" % (a, b, c))
end_time = time.time()
print("time: %d" % (end_time - start_time))

# from using the debug key, we can learn that starting from the for loop of 'a' it goes down to b, c and to the if,
# and then jumps back to the c and repeats until c reach 100, and then it give 1 to the b value, and until b gets 1
# hundred a gets 1, and so on repeat, until a = 100 and b = 100 and c = 100, then the program will stop.

# 算法是独立存在的一种解决问题的方法的思想
# 算法， 体现的是思想，而不是语言， 用什么语言无所谓，但思想必须要学到位

"""
算法五大特性：

输入： 算法具有0给或多个输入
输出： 算法至少有1个或多个输出
有穷性： 算法在有限的步骤之后会自动结束而不会无限循环，并且每一个步骤可以在可接受的时间内完成
确定性： 算法中的每一不都是有确定含义，不会出现二义性 
可行性： 算法中的每一步都是可行的，也是就是说每一步都是能够执行有限的次数完成
"""

