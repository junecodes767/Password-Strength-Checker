import re

def get_password():
    password = input("Please enter password:")
    return password
    
    
def validate_password():
      
    
    while True:
    # if password is less than 8
    #prompt user to add a password that is at least 8 digits
        password =get_password() 
        if len(password) < 8:
            print(f"Your Password: {password} needs to be over 8 digits.") 
            continue
            
    # If false these will be executed
        elif not re.search('[a-z]',password):
            print("Must have lower_case letters")
            continue
        elif not re.search('[A-Z]',password):
            print("Must have uppercase Letters")
            continue
        elif  not re.search('[0-9]',password):
            print("Must include digits.")
            continue
        elif not re.search('[!,@,#,$]',password):
            print("Must include special characters")
            continue
        good_password(password)
        break
                
    
     

def good_password(password):    
    if len(password) >= 16:
        print(f"This password: '{password}' includes uppercase and lowercase letters, digits, and has special characters. This is a good password.")
        get_improvements(password)
    else:
        print(f"To further improve, '{password}' should be at least 16 characters long.")
        
        while True:
            better_password = input("Please make the password 16 characters or more: ")
            
            if len(better_password) >= 16:
                print(f"Thank you! '{better_password}' is now a good password.")
                get_improvements(better_password)
                break  # Exit the loop once a valid password is provided


def get_improvements (password):
   while True:
        if re.search(r'qwerty', password):
            print("Please remove 'qwerty' from your password. It makes it weak.")
            password = input("Please make the necessary adjustments: ")
            continue
        if re.search(r'123', password):
            print("Numbers like '123' are too predictable. Please remove them.")
            password = input("Please make the necessary adjustments: ")
            continue
        if re.search(r'1qaz2wsx', password):
            print("Please avoid patterns like '1qaz2wsx'.")
            password = input("Please make the necessary adjustments: ")
            continue
        # If no issues are found, the password is strong.
        print(f"'{password}' is now a strong password!")
        return password
        
validate_password ()