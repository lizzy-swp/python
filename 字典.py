alien_0={'color':'red','point':5}
print(alien_0['color'])
print(alien_0['point'])
alien_0['age']=26 #给字典添加元素
print(alien_0)
alien_0['age']=27 #修改字典元素值
print(alien_0)
del alien_0['point'] #删除元素键值对
print(alien_0)
aaa={'n1':'hhh','n2':'ooo','n3':'ggg','n4':'hhh'}#遍历键值对，顺序随意
for n,y in aaa.items():#items代表方法
    print(n.title()+'name is'+y.title())
for name in aaa.keys():#默认是遍历一个键，keys加不加都行，顺序随意
    print(name)
for nn in sorted(aaa.keys()): #按字母顺序遍历
    print(nn.title())
for hh in sorted(aaa.values()):#遍历值
    print(hh.upper())
for ww in set(sorted(aaa.values())): #不重复的值
    print(ww)
#字典可以和字典或列表嵌套使用