#!/usr/bin/python

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temperatures = (36.5, 37, 37.5, 38, 39)

F = map(fahrenheit, temperatures)
C = map(celsius, temperatures)


temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)
#[36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]

### Following is same function as from line#1-line#18
print("use lambda for mapping")

C_array = [39.2, 36.5, 37.3, 38, 37.8] 
F_list = list(map(lambda x: (float(9)/5)*x + 32, C_array))
## lambdafunc = lambda x: (float(9)/5)*x + 32
## mapfunc = map(lambdafunc, Carray)
## F_list = list(mapfunc)
print(F_list)


