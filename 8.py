sentence = input("Enter a sentence: ")

i = 0
vowel = 0
consonant = 0 

for char in sentence:
    if char in 'aeiou' or char in 'aeiou':
        vowel+=1
        i+=1
    elif sentence[i] == ' ':
        continue
    else:
        consonant+=1
        i+=1    

print(f'Your sentence had {vowel} vowel alphabets and {consonant} consonant alphabets.')
