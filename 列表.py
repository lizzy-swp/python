hhh=["aaa","bbb","ccc"]
print(hhh)
print(hhh[0])
hhh[0]="ddd"
print(hhh)
hhh.append("eee") #在末尾添加
print(hhh)
hhh.insert(1,"fff") #插入元素
print(hhh)
del hhh[1] #删除元素
print(hhh)
print(hhh.pop()) #删除最后一个元素并调用它
print(hhh.pop(0)) #删除第一个元素并调用它
print(hhh)
hhh.remove("bbb") #删除值bbb
print(hhh)
cars=["bmw","benz","audi","subar","ooo"]
cars.sort() #对元素按字母顺序永久排序
print(cars)
cars.sort(reverse=True) #按字母倒叙永久排列
print(cars)
print(sorted(cars)) #按字母顺序临时的排列
print(cars)
cars.reverse() #倒序
print(cars)
print(len(cars)) #序列长度