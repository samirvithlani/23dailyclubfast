cityData = {"Ahmedabad":{"Mon":[10,20],"Tue":[10,15]},"Mumbai":{"Mon":[20,22],"Tue":[20,25]}}
tempList =[]
tempadd = 0
cityadd = 0


for i,j in cityData.items():
    for p,q in j.items():
        print(i)
        #print(p,q)
        for t in q:
            tempadd = (tempadd + t) /2
        tempList.append(tempadd)
        tempadd = 0
    
        
                  
            
        

#print(tempList)   
print(cityData)

                     
