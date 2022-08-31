def decorator(function):
    def wrapper(*arg, **kwargs):
        print("Wrapper")
        function(*arg, **kwargs)

    return wrapper


class MyClass:
    @decorator
    def method(self):
        print("My Class")


mc = MyClass()
mc.method()
