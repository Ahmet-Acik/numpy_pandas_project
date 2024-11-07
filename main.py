import numpy as np
import pandas as pd

# NumPy example
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)

# Pandas example
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Alice', 'Jane', 'Robert', 'Tom', 'Megan', 'Joe', 'Mike'],
        'Age': [28, 24, 35, 32, 27, 30, 29, 33, 31, 34, 30]}
df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)