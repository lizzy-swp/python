def hanshu(): #定义函数
    print('hello')

hanshu() #调用函数


def hhh(a,b):
    print('hello,'+a.title()+b.upper())
hhh('lizzy','chaos')
hhh(a='lizzy',b='chaos')

def get(a1,a2):
    a3=a1+' '+a2
    return a3

b3=get('b1','b2')
print(b3)

def pizza(*toppings): #实参不管多少个都打印
    print(toppings)

pizza('aaa','bbb','ccc')
pizza('aaa','bbb')

def build(frist,last,**uer):
    p={}
    p['first_name']=frist
    p['last_name']=last
    for key,value in uer.items():
        p[key]=value 
    return p 
 
mm=build('aaa','bbb',l='ccc',n='ddd')
print(mm)