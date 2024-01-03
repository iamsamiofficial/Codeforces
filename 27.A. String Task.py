s = input()
s = s.lower()
final = ''
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i== 'o' or i == 'u' or i == 'y':
        continue
    else:
        final+= "."+i
print(final)