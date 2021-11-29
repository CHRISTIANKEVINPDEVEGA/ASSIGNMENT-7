import re
pattern=re.compile(r'')
while True:
 password=input("Input your password: ")
 if (len(password) < 6):
    print("invalid")
 elif re.search(r'[!@#$%&]',password) is None:
    print("invalid")
 elif re.search(r'\d',password) is None:
    print("invalid")
 elif re.search(r'[A-Z]',password) is None:
    print ("invalid")
 elif re.match(r'[a-z A-Z \d !@#$%&]{15}',password):
    pattern=re.compile(r'[a-z A-Z \d !@#$%&]{6}',password)
    result=pattern.match(password)
    print('valid')
    break
else:
    print('try again')