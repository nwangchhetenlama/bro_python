#indexing =accesing elements of sequence using [](indexing operator)

#[start:end:step]

credit="1234-5678-9012-3456"
"""print(credit[0])
print(credit[4])
print(credit[2:4])#end exclusive

print(credit[5:])
print(credit[-3])
"""
#for step
#print(credit[::4])
"""last_digits=credit[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")
#reverse
reverse=credit[::-1]
print(reverse)"""
#format specifier={value:flag} format value based on what flag inserted

price1,price2,price3=233234.3232,-324.2,321.34
print(f"the price1 is {price1:.2f}")
print(f"the price2 is {price2:.2f}")
print(f"the price3 is {price3:.2f}")

print(f"the price1 is {price1:10}")
print(f"the price2 is {price2:10}")
print(f"the price3 is {price3:10}")

print(f"the price1 is {price1:010}")
print(f"the price2 is {price2:010}")
print(f"the price3 is {price3:010}")

print(f"the price1 is {price1:010}")
print(f"the price2 is {price2:010}")
print(f"the price3 is {price3:010}")

print(f"the price1 is {price1:+}")
print(f"the price2 is {price2:+}")
print(f"the price3 is {price3:+}")
#<,>,^ for left,right and middle
#comma for comma 
print(f"the price1 is {price1:+,.2f}")

