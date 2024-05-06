
# def check_vowels(word):
#     volwels = 'aeiouAEIOU'
#     for char in word:
#         if char in volwels:
#             return True

def check_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    
    return count        

            

file = open("fileDemo1.txt", "r")
word_list = []

for i in file:
    words = i.split()
    
    for x in words:
        if check_vowels(x) >2:
            word_list.append(x)


print(word_list)  
print(len(word_list))          
