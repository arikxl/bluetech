numbers = []
for num in [1,3,5,7,9]:
    numbers.append(num**2)
print(numbers)


numbers =[num**2 for num in [1,3,5,7,9]]
print(numbers)



names =[('name','arik'),('age',38)]
d={}
for key, value in names:
    d[key] = value
print(d)

d = {key: value for key, value in names}
print(d)

d= dict(names)
print(d)