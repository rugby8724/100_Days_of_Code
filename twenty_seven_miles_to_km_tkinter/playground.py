def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)


# add(7, 5, 77, 24, 13, 14)

def calculate(n, **kwargs):

    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)



# calculate(2, add=3, multiply=7)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make='Ford', model='Mustang')
print(my_car.model)