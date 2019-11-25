import pandas as pd
cars = pd.read_csv("cars.csv")

print("First 5 rows of odd columns  \n")
n = cars.iloc[0:5,[1,3,5,7,9,11]]    
print(n)  
print("Model Mazda RX4")        
y = cars[cars['Model']=='Mazda RX4']
print(y)
x = cars.iloc[[23],[2]]
print(" \n Camaro Z28 has: \n ", x," \n")

z = cars.iloc[1,[2,10]]
print("Mazda RX4 WAG \n",z, "\n")

zz = cars.iloc[28,[2,10]]
print("Ford Pantera L \n", zz, "\n")

zzz = cars.iloc[18,[2,10]]
print("Honda Civic \n",zzz,"\n")


