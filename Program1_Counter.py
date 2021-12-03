def Input():
   Raw_Sentence=input("Input a number of words, sentence, or phrase, and the program will count its elements:\n ")
   processed_sentence = Raw_Sentence.lower() 
   return processed_sentence

def vowel_count(sentence):
   vowel_count = 0
   for charac in sentence:
    if charac in 'aeiou':
        vowel_count = vowel_count + 1
   print(f"Vowel count: {vowel_count}")

def consonant_counter(sentence):
   consonant_count= 0
   for charac in sentence:
     if charac in 'bcdfghjklmnpqrstvwxyz':
        consonant_count = consonant_count + 1
   print(f"Consonant count: {consonant_count}")

def word_counter(sentence):
   word_count = sentence.split()
   print(f"Word Count:{len(word_count)}")    

sentence = Input()
word_counter(sentence)
vowel_count(sentence) 
consonant_counter(sentence)
