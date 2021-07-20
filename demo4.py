#4-1
'''pizzas = ['New York Style','Chicago Style','California Style','Pan Pizza']
for pizza in pizzas:
    print(f'I like {pizza}.')
print('I really like pizza!')'''
#4-2
'''animals = ['panda','cat','dog']
for animal in animals:
    print(f'A {animal} would make a great pet.')
print('Any of these animals would make a great pet!')'''

#homework
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("------  商品列表  ------")
for product in products:
    for produce in product:
        #for i in range(0,7):
             #if i % 2 == 0:
        print(f'{produce}\t',end="")
        print("\n")
