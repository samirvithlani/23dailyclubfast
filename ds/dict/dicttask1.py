sales = {"monday":[100,200,300],"tuesday":[200,3000,400],"wednesday":[300,400,500],"thursday":[400,500,600],"friday":[500,600,700],"saturday":[600,700,800],"sunday":[700,800,900]}
# print(sales)
add =0
dailySales =[]

for i,j in sales.items():
    for k in j:
      add = add + k #100 + 200 + 300 =600
    dailySales.append(add)
    add = 0

#print(dailySales)

max = dailySales[0]
day = ""
for i in range(len(dailySales)):
    #600 > 600
    #1800 > 600
    #3600 > 1800
    if dailySales[i] > max:
        max = dailySales[i] #1800 #3600
        day = list(sales.keys())[i] #tuesday wednesday
        print(day)
        

print("Day with max sales is",day,"with sales of",max)    
    
    

    
    