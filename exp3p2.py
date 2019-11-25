import pandas as pd
cars = pd.read_csv("cars.csv")
n = 0
print("First 5 odd rows \n")
while n < 10:
    if n % 2 != 0:
        z = cars.loc[n,:]
        print(z, '\n')
        n = n+1
    if n % 2 == 0:    
        n = n+1   
print("Model Mazda RX4")        
y = cars[cars['Model']=='Mazda RX4']
print(y)

x = cars.iloc[[23],[2]]
print(" \n Camaro Z28 has: \n ", x)

x11 = cars.iloc[[1],[2]]
x12 = cars.iloc[[1],[10]]
print("\n Mazda RX4 WAG \n",x11,"\n", x12)

x21 = cars.iloc[[28],[2]]
x22 = cars.iloc[[28],[10]]
print("\n Ford Pantera L \n",x21,"\n", x22)

x31 = cars.iloc[[18],[2]]
x32 = cars.iloc[[18],[10]]
print("\n Honda Civic \n",x31,"\n", x32)

