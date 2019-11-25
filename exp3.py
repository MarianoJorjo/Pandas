import pandas as pd
cars = pd.read_csv("cars.csv")
z = cars.head()
y = cars.tail()
print(z)
print(y)