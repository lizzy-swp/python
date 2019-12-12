 import json #没有导模块所以不能运行 
 numbers=[2,3,4,5,6,7,8]
 filename='numebrs.josn'
 with open(filenaem,'w') as f_obj:
     json.dump(numbers,f_obj)