#第三章
#3-1 and 3-2
'''names = ['xuecheng','lihong','xiaoming','baixue']
for i in range(4):
   # print(names[i])
    message = f'Hello! My friend {names[i]}'
    print(message)'''
#3-3
'''comucate = ['motorcycle','car','bus','bicycle','ship','plane']
for i in range(6):

    choice = f'I would like to own a {comucate[i]}'
    print(choice)'''
#ex01
'''motorcycle = []
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')

motorcycle.insert(0,'ducati')
print(motorcycle)
del motorcycle[1]
print(motorcycle)'''

#3-4
'''names = ['haining','huiyu','anjinle']
print(names)
not_come = names.pop(1)
print(names)
print(f'{not_come.title()} 不能参加聚会')
names.insert(1,'jiankang')
print(names)
print('找到了更大的餐桌！')
names.insert(0,'gaoxing')
names.insert(2,'haojiawen')
names.append('tianchuangeng')
print(names)
for i in range(6):
    print(f'欢迎 {names[i].title()} 参加聚会')
print('不好意思只能邀请两位了')
for i in range(3):
    first = names.pop(i)
    second = names.pop(2)
    third = names.pop(3)
    four = names.pop(1)
print(names)'''

#1-100的和
#方法一
'''sum = 0
for i in range(101):
    print(i)
    sum = sum + i
print(f'1~100的和为{sum}')'''

#方法二
'''sum  = 0
i = 1
while i < 101:
    sum = sum + i
    i += 1
print(f'1~100的和为{sum}')'''

#1~100之间偶数的和
'''i = 0
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum = sum + i
    else:
        continue
print(sum)'''

#九九乘法表
'''for i in range(10):
    print("\t")
    for j in range(1,i+1):
        result = i * j
        print("%d*%d=%d"%(i,j,i*j),end='\t')'''
#3-8
'''sencery = ['beijing','shanghai','tianjing','huaian','xuzhou']
print(sencery)
print(sorted(sencery))
print(sorted(sencery,reverse=True))
sencery.reverse()
print(sencery)
sencery.reverse()
print(sencery)
print(len(sencery))'''

#4-1
'''names = ['','','']
'''

'''str = 'chengdu'
print(str[0:-1])
print(str  +  '你好')
print('hello\nchengdu')
print(r'hello\npython')

names = '12344567'

print(names.isdigit())
'''
'''import random
offices = [[],[],[]]
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for temNames in offices:
    print('办公室%d的人数为：%d'%(i,len(temNames)))
    i += 1
    for name in temNames:
        print('%s'%name,end='')
    print('\n')
    print('-'*20)'''


