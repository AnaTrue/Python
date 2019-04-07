x = input("Введите число ")
i = 0
max = 0
while i<len(x):
    if int(x[1])>max:
        max = int(x[i])
    i+=1
  
print(max)