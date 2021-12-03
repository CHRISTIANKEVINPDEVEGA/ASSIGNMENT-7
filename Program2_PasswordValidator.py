import re


def system():
   while True:
    user_password = input("Please input you new password: ")
    if (re.search(r"[a-z]",user_password)) is None:
       print("Invalid password, your password should contain atleast 1 alphabetic character in lowercase.")
    elif (re.search(r"[A-Z]",user_password)) is None:   
       print("Invalid password, your password should contain atleast 1 alphabetic character in uppercase.")       
    elif (re.search(r"[\d]",user_password)) is None:
       print("Invalid password, your password should contain atleast 1 number.")     
    elif (re.search(r"[!@#$%^&*()_+/-=]",user_password)) is None:
       print("Invalid password, your password should contain atleast 1 special character.")      
    elif (len(user_password) < 16 ):      
       print("Invalid password, your password should be greater than 15 chracters in length.")                                                       
    else:
       print("Valid password, you have successfully created your won password.")
       break
  
system()