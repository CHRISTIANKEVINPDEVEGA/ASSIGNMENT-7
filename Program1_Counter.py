Raw_Sentence=input("gve any sentences or phrase: ")
processed_sentence = Raw_Sentence.lower()
vowel_count = 0
consonant_count= 0

for charac in processed_sentence:
    if charac =='a':
        vowel_count = vowel_count + 1
    if charac =='e':
        vowel_count = vowel_count + 1
    if charac =='i':
        vowel_count = vowel_count + 1
    if charac =='o':
        vowel_count = vowel_count + 1
    if charac =='u':
        vowel_count = vowel_count + 1
    

for charac in processed_sentence:
    if charac == 'b':
        consonant_count = consonant_count + 1
    if charac == 'c':
        consonant_count = consonant_count + 1        
    if charac == 'd':
        consonant_count = consonant_count + 1
    if charac == 'f':
        consonant_count = consonant_count + 1
    if charac == 'g':
        consonant_count = consonant_count + 1
    if charac == 'h':
        consonant_count = consonant_count + 1
    if charac == 'j':
        consonant_count = consonant_count + 1
    if charac == 'k':
        consonant_count = consonant_count + 1
    if charac == 'l':
        consonant_count = consonant_count + 1
    if charac == 'm':
        consonant_count = consonant_count + 1
    if charac == 'n':
        consonant_count = consonant_count + 1
    if charac == 'p':
        consonant_count = consonant_count + 1
    if charac == 'q':
        consonant_count = consonant_count + 1
    if charac == 'r':
        consonant_count = consonant_count + 1
    if charac == 's':
        consonant_count = consonant_count + 1
    if charac == 't':
        consonant_count = consonant_count + 1
    if charac == 'v':
        consonant_count = consonant_count + 1
    if charac == 'w':
        consonant_count = consonant_count + 1
    if charac == 'x':
        consonant_count = consonant_count + 1
    if charac == 'y':
        consonant_count = consonant_count + 1
    if charac == 'z':
        consonant_count = consonant_count + 1
    
print(f"Word count: {len(processed_sentence)}")
print(f"Vowel count: {vowel_count}")
print(f"Consonant count: {consonant_count}")