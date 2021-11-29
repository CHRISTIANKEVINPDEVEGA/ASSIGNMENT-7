import re
pattern='[a-z A-Z 0-9 !@#$%&]'
while True:
 user_password=input('password: ')
 if len(user_password)<15:
     print("invalid user password")
 elif(re.search(pattern, user_password)): 
  print("valid password")
  break 
 else:
  print("invalid")  