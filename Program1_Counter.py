def Input():
   Raw_Sentence=input("Input a number of words, sentence, or phrase, and the program will count its elements:\n ")
   processed_sentence = Raw_Sentence.lower() 
   return processed_sentence

def vowel_counter(V_sentence):
   vowel_count = 0
   for charac in V_sentence:
    if charac in 'aeiou':
        vowel_count = vowel_count + 1
   print(f"Vowel count: {vowel_count}")

def consonant_counter(C_sentence):
   consonant_count= 0
   for charac in C_sentence:
     if charac in 'bcdfghjklmnpqrstvwxyz':
        consonant_count = consonant_count + 1
   print(f"Consonant count: {consonant_count}")

def word_counter(W_sentence):
   word_count = W_sentence.split()
   print(f"Word Count:{len(word_count)}")    

SENTENCE = Input()
word_counter(SENTENCE)
vowel_counter(SENTENCE) 
consonant_counter(SENTENCE)
