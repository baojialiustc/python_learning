import numpy as np
class Xclass:
    pass

def func_1(instance_list, instance_tuple, instance_dict, num, instance_created_class, instance_array):
    instance_list[0] += 1
    # instance_tuple[0] = 'changed'
    instance_dict[0] = 'changed'
    local_array = np.zeros([3, 3])
    local_array = instance_array
    local_array[0] += 100
    num += 1
    x.num += 1

def compound_func(y):
    y[0] += 1
    def inner_func(z):
        z[1] += 1
    inner_func(y)

x = Xclass()
list_1 = [1 for i in range(3)]
tuple_1 = (1, 1)
dict_1 = {0:1, 1:1}
int_num = 10
x.num = 10
array = np.arange(1,10)
func_1(list_1, tuple_1, dict_1, x.num, x, array)
print(list_1)
print(tuple_1)
print(dict_1)
print(x.num)
print(array)
# test nested function
compound_func(list_1)
print(list_1)