# Function to count vowels in a word
def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

file = open("fileDemo1.txt", "r")
word_list = []
    
for line in file:
    words = line.split()
        
    for word in words:
        if count_vowels(word) > 2:  # Check if the word has more than 2 vowels
            word_list.append(word)

print(word_list)
