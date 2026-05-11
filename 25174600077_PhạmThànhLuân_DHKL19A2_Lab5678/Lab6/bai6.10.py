import numpy as np

A = np.array([[1, 2], [3, 4]])

if np.linalg.det(A) != 0:
    print(np.linalg.inv(A))
else:
    print("Không khả nghịch")