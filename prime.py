n = int(input("input n for prime :"))

prime_list = [2,3]

temp = prime_list[-1]

while(temp<=n):
    temp+=2
    for i in prime_list:
        if(temp%i==0):
            break
    else:
        prime_list.append(temp)


print(prime_list)
