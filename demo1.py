'''num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != j)and(j != k)and(k != i):
                print(i,j,k)
                num += 1
print(num)'''

'''profit=int(input('Show me the money: '))
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit<=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)'''

'''profit = int(input('show me the money: '))
bonus = 0
a = 100000
b = 200000
c = 300000
d = 400000
f = 600000
g = 1000000

if profit <= a:
    bonus = profit * 0.1
    print(bonus)
elif (profit > a)and(profit <= b):
    bonus = (profit-a) * 0.075 + a * 0.1
    print(bonus)
elif (profit > b)and(profit <= d):
    bonus = (profit-b) * 0.05 + a * 0.1 + b * 0.075
    print(bonus)
elif (profit > a)and(profit <= b):
    bonus = (profit-a) * 0.075 + a * 0.1
    print(bonus)'''


'''a = input("请输入：")
b = a + 100
print(b)'''

'''if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")'''

#成绩等级
'''score = int(input('请输入成绩：'))
if score > 90 and score <=100:
   print("本次考试，等级为A")
elif score >= 80 and score < 90:
    print("本次考试，等级为B")
elif score >= 70 and score < 80:
    print("本次考试，等级为C")
elif score >= 60 and score < 70:
    print("本次考试，等级为D")
else:
    print("本次考试，等级为E")'''
#随机数
'''import random 
computer = random.randint(0,2)
print(computer)'''

#石头剪刀布
'''import random
user = int(input("请出石头(0)、剪刀(1)、布(2): "))
if user == 0:
    print('你的输入为：石头(0)')
elif user == 1:
    print('你的输入为：剪刀(1)')
elif user == 2:
    print('你的输入为：布(2)')
computer = random.randint(0,2)
print('随机生成数字为：',computer)
if user ==0:
    if computer == 0:
        print('平手哦')
    elif computer == 1:
        print('不错哦，你赢了！')
    elif computer == 2:
        print('哈哈，你输了！')
if user ==1:
    if computer == 0:
        print('哈哈，你输了！')
    elif computer == 1:
        print('平手哦')
    elif computer == 2:
        print('不错哦，你赢了！')
if user ==2:
    if computer == 0:
        print('不错哦，你赢了！')
    elif computer == 1:
        print('哈哈，你输了！')
    elif computer == 2:
        print('平手哦')'''

'''for i in range(5):
    print(i)'''
'''for i in range(0,12,3):
    print(i)'''

'''name = 'chengdu'
for x in name:
    #print(x)
    print(x,end = "\t")'''

'''a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])'''

'''i = 0
while i < 5:
    print("当前是第%d次执行循环"%i)
    i += 1'''

#完全平方数
'''n=0
while (n+1)**2-n*n<=168:
    n+=1
print(n+1)
for i in range((n+1)**2):
    if i**0.5==int(i**0.5) and (i+168)**0.5==int((i+168)**0.5):
        print(i-100)'''

name = "ada ovelace"
print(name.title())
print(name.upper())
print(name.lower())