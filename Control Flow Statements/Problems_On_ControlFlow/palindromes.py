s=' '
temp=s.lower
s=s.strip()
s=s.replace(",","")
s=s.replace(":","")
s=s.replace(" ","")
s=s.lower()
z1=s
z2=s[::-1]

# print(s[::-1])

if z1==z2:
    print("palindrome")
else:
    print('not')
