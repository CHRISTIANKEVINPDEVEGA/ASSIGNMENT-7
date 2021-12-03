Raw_Sentence=input("Input a number of words, sentence, or phrase, and the program will count its elements: ")
word_count = Raw_Sentence.split()
processed_sentence = Raw_Sentence.lower()
vowel_count = 0
consonant_count= 0

for charac in processed_sentence:
    if charac in 'aeiou':
        vowel_count = vowel_count + 1   

for charac in processed_sentence:
    if charac in 'bcdfghjklmnpqrstvwxyz':
        consonant_count = consonant_count + 1
    

print(f"Word Count:{len(word_count)}")    
print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")