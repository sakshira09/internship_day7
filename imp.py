import numpy as np
a = [1,2,3,4]
b = [5,6,7,8]
print(a+b)
[a[i]+b[i] for i in range(len(a))]
print(len(a))
a = np.array(a)
b = np.array(b)
print(a+b)
print(a*b)
print(a/b)
print(a**2)