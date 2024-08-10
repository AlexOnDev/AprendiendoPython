### Modules ###

import my_module

my_module.sumValue(5,3,4)
my_module.printValue("AAA")

from my_module import sumValue, printValue

sumValue(5,3, 4)
printValue("holaaa")

import math

print(math.pi)
print(math.trunc(math.pow(2, 8)))

from math import pi as PI_VALUE
print(PI_VALUE)
