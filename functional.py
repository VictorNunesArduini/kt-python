import math


def inception_func(n):
    def func(x):
        return 11 * x
    return func(n)


print("inception: ", inception_func(2))


def lambda_func(n):
    return lambda a: a * n


my_func = lambda_func(2)
print("lambda: ", my_func(11))

array = [1, 2, 2, 4, 5]
new_array = list(map(math.sqrt, array))
print("map: ", new_array)

array2 = [1,2,3]
new_array2 = [math.sqrt(x) for x in array2]
print("lista de compreensão: ", new_array2)

print("set: ", set(array))
conjunto1 = set(array)
conjunto2 = set(array2)
print("união: ", conjunto1 | conjunto2)
print("diferença: ", conjunto1 - conjunto2)
print("interseção: ", conjunto1.intersection(conjunto2))
