import re
def complexity_check(text):
            regex=r'[!@#$%^&*()_+=;:<>?,./~`]'
            if not any(char.isupper() for char in text ):
                print("there must be atleat one uppercase chracter in your password")
                return
            
            if len([char for char in text  if char.isdigit()]) < 2:
                print("there must be atleast 2 digits in the password\n")
                return
            
            if not  re.search(regex,text):
                print("please add atleast one special chracters in the password")
                return
            
            if len(text)<8:
             print("your password is very weak,it needs be a combinattion of alphabets,chracters& symbols 1\n")
             return
         
            if (text.isalpha()):
                print("your password is weak but it needs be a combination of alphabets,chracters& symbols 2\n")
                return 
            
            if(text.isdigit()):
                print("plase maka combinations of text,numeraks and special chracters")
                return
    
    
            print("your password is Strong enough and meets all the requirmentsfor complexity\n")
            
                
                
                
                
                
                
                
                

text=str(input("enter your password to check the complexity\n"))
complexity_check(text)


