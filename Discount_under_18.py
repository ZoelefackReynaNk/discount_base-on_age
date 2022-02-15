data = {"100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40}

age = int(input("enter new discount age: "))

print("\n")
all = [ ]
under = [ ]
adult = [ ]
for value in data.values():
    all.append(value)
    if value < 18:
        under.append(value)
    else:
        adult.append(value)
print(f"all ={all}\n under = {under}\n adult= {adult}")
print("№_all = ",len(all), "\n №_under = ", len(under),"\n №_adult = ", len(adult))
print("\n")
new_under = [ ]
new_adult = [ ]
if age < 18:
    for value in all:
        if value < age:
            new_under.append(value)
        else:
            new_adult.append(value)
print(f"new_under = {new_under}\n№_NU = ", len(new_under))
print(f"new_adult = {new_adult}\n№_NA = ", len(new_adult))
print("\n\n")
initial_price = (len(under)*5 + len(adult)*20)
final_price = (len(new_under)*5 + len(new_adult)*20)
print(f"initial_price = {initial_price}\nfinal_price = {final_price}\n\n")
discount = ((final_price-initial_price)/initial_price)*100
dis = int(discount)
print(f"new discount is {dis}%")
