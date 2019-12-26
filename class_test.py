
class CallableAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a + self.b


if __name__ == '__main__':
    # tensorflow use call function
    # python need to use __call__ function to turn class into callable one
    add = CallableAdd(2, 3)
    print(add())