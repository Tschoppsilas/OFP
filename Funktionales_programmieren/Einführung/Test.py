def add_topping(func):
    def wrapper():
        print("Adding topping")
        func()
    return wrapper

@add_topping
def Ice_Cream():
    print("You got your ice cream!")

@add_topping
def Frozen_Yoghurt():
    print("You got your frozen yoghurt!")

@add_topping
def Waffle():
    print("You got your waffle!")

Ice_Cream()
Frozen_Yoghurt()
Waffle()

