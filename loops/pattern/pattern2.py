'''
 *
 * *
* * * 
'''
#0,1,2
for i in range(3):
  #0,3-i --> 0,12  
  #0,3-1 0,1 2
  #0,3-2 0,1
    for j in range(3-i): 
        print(" ", end="") 
    #0,1    
    # 
    for k in range(i+1): 
        print("* ", end="") 
                            
    print()