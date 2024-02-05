#0 1 1 2 3 5

no1 = 0
no2 = 1
ans = 0

print(no1 , "", no2, end=" ")

for i in range(1,8):
    #i =1,2
    #0 = 0 + 1 ans = 1
    #1 = 1 + 1 ans = 2
    #2 = 1 + 2 ans = 3
    #3 = 2 + 3 ans = 5
    ans = no1 + no2
    print(ans, end=" ")#0 1 1 2 3 5
    #no1 = 1
    #no1 = 1
    #no1 = 2
    no1 = no2   
    #no2 = 1
    #no2 =2
    #no2 = 3
    no2 = ans
    