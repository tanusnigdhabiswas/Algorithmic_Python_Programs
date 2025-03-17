# Python program to check a palindrome using "Two pointer Approach"

def check_palindrome(word):
    p1=0
    p2=len(word)-1
    while p1 < p2:
        if word[p1]==word[p2]:
            p1+=1
            p2-=1
            
        else:   
            return False
        
    print("It is a palindrome")
                
                
check_palindrome("madam")       
    