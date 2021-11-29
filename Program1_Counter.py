Raw_Sentence=input("gve any sentences or phrase: ")
processed_sentence = Raw_Sentence.lower()
vowel_count = 0
consonant_count= 0

for charac in processed_sentence:
    if charac =='a':
        vowel_count = vowel_count + 1
    elif charac =='e':
        vowel_count = vowel_count + 1
    elif charac =='i':
        vowel_count = vowel_count + 1
    elif charac =='o':
        vowel_count = vowel_count + 1
    elif charac =='u':
        vowel_count = vowel_count + 1
    

for charac in processed_sentence:
    if charac == 'b':
        consonant_count = consonant_count + 1
    elif charac == 'c':
        consonant_count = consonant_count + 1        
    elif charac == 'd':
        consonant_count = consonant_count + 1
    elif charac == 'f':
        consonant_count = consonant_count + 1
    elif charac == 'g':
        consonant_count = consonant_count + 1
    elif charac == 'h':
        consonant_count = consonant_count + 1
    elif charac == 'j':
        consonant_count = consonant_count + 1
    elif charac == 'k':
        consonant_count = consonant_count + 1
    elif charac == 'l':
        consonant_count = consonant_count + 1
    elif charac == 'm':
        consonant_count = consonant_count + 1
    elif charac == 'n':
        consonant_count = consonant_count + 1
    elif charac == 'p':
        consonant_count = consonant_count + 1
    elif charac == 'q':
        consonant_count = consonant_count + 1
    elif charac == 'r':
        consonant_count = consonant_count + 1
    elif charac == 's':
        consonant_count = consonant_count + 1
    elif charac == 't':
        consonant_count = consonant_count + 1
    elif charac == 'v':
        consonant_count = consonant_count + 1
    elif charac == 'w':
        consonant_count = consonant_count + 1
    elif charac == 'x':
        consonant_count = consonant_count + 1
    elif charac == 'y':
        consonant_count = consonant_count + 1
    elif charac == 'z':
        consonant_count = consonant_count + 1
    
print(f"Word count: {len(processed_sentence)}")
print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")