# Not really a global variable, but within a module, like from global_variable import a  
a = 5

def func_1():
    print(a)

def func_2():
    try:
        print(a)
        a = 10
    except UnboundLocalError:
        print("The variables defined in function is local variables")

def func_3():
    # The local variables with the same name will cover the global.
    a = 18
    print(a)

def func_4():
    global a

    a = 15
    print(a)

func_list = [func_1, func_2, func_3, func_4]

for func in func_list:
    func()