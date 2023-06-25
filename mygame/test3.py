import random
a = random.randint(1,100)
b = random.randint(1,100)
print('Q:', a, '+' ,b, '=?')

ans = int(input('答えは？'))
if a + b == ans:
    print('正解です！')
else:
    print('間違いです。答えは、', a+b,'です。')

