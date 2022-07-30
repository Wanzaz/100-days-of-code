def calculate(n, **kwargs): # type(kwargs) == dict
    print(kwargs)

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]

        # the advantage of get() is if the key doesn't exit it will return None instead of error
        self.model = kw.get("model") 
        self.color = kw.get("color") 
        self.seat = kw.get("seat")

my_car = Car(make="Nissan")
print(my_car.model) # == None
