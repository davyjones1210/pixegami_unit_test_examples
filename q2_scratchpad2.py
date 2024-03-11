import numpy as np

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

a = (1, 2, 3)
b = (4, 5, 6)

# print(cross(a, b))

# Creating a sample array with float values
test_obj = [1.23, 4.56, 7.89]
float_array = np.array(test_obj)

# Converting float_array to integers
int_array = float_array.astype(int)
x,y,z = a
test_array = np.array(a)
# print("Original Array:", float_array)
# print("Converted Array:", int_array)
print("Test array: ", test_array)
print("a: ", a)

print(type(test_array))

print(type(a))

#
# # x = np.array([1,2,3], dtype=np.int32)
# test_obj = [1,2,3]
# # y = x.astype(np.int32)
#
# vals = [3, np.int32(2), np.int64(1), np.float64(0)]
# new_vals = [(e, type(e), isinstance(e, (int, np.integer))) for e in vals]
#
#
# print(type(new_vals))
# print(new_vals)
#
# print(type(new_vals))
# print(new_vals)
# # print(type(test_obj))
# # print(test_obj)