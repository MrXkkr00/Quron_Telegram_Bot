
message=input()
for i in range(len(message)-1):
    if message[i] == '-':
        sura = (message[:i])
        oyat = (message[i+1:])

print(sura)
print(oyat)
# print(oyat)
# a=input
# print(len(a))