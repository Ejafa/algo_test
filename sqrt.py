a = input("input number to sqrt: ")

n = int(input("number of decimal: "))

output = ""

for i in range(1,n+1):
    p = int(a + ("00"*i))
    if(output == ""):
        x = 1
    else:
        x = int(output)*10
        
    while(p>=x*x):
        x+=1

    x-=1
    if(output == ""):
        output = str(x)
    else:
        output = output + str(x%10)
        
    #print(output[:-n]+'.'+output[-n:])

print(output[:-n]+'.'+output[-n:])
