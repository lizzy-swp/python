mags=['hhh','ooo','eee']
for mag in mags:
    print(mag)
for value in range(1,5):#range()产生数字
    print(value)
number=list(range(1,6)) #list()创建列表
print(number)
drop=list(range(1,10,2))#2为渐进值
print(drop)
strees=[]
for value in range(1,6):
    strees.append(value**2)
print(strees)
strees=[value**2 for value in range(1,6)] #列表解析，代码合并
print(strees)
mun=[1,2,3,4,7,6,8,0,9,5]
print(min(mun))
print(max(mun))
print(sum(mun))
print(mun[0:3])#切片，截取列表的前三个
print(mun[ :3])
print(mun[2: ])
print(mun[-3: ])#切最后三个
yuanzu=(1,2,3) #元祖，元素不可修改的列表
print(yuanzu[0])
print(yuanzu[1])
print(yuanzu[2])




