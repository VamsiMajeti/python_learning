import numpy as np

array1 = np.arange(1, 20)
print(array1)
print(f"Sum of the array: {np.sum(array1)}")
print(f"Mean of the array: {np.mean(array1)}")
print(f"Max of the array: {np.max(array1)}")
print(f"Min of the array: {np.min(array1)}")

array2 = np.zeros(10)
array2[:] = 5
print(f"Array2 replaced with 5s: {array2}")

array3 = np.linspace(0, 50, 5)
print(array3)

array4 = np.random.randint(10, 100, 8)
print(array4)
print(f"Only even numbers from array4: {array4[array4 % 2 == 0]}")