name=input('shuru:')
print(name)

age=input('how old are you! ')
age=int(age)
if age>=18:
    print('you are a big baby')

prompt='\ntell me something!'
prompt+='\nenter "quit" to end the prompt: '
mes=''
while mes !='quit':
    mes=input(prompt)
    if mes!='quit':
        print(mes)
