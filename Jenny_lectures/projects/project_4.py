#ccaeser ciepher

alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encryption():
    str1=input("Enter the string: ").upper()
    n=int(input("Enter the shift number: "))
    c=0
    result=""
    for i in str1:
            if i in alphabet:
                j=alphabet.index(i)
                c=(j+n)%26
                result+=alphabet[c]
            else:
                result+=i    
    print(f"Encrypted:{result}")                


def decryption():
    str1=input("Enter the string: ").upper()
    n=int(input("Enter the shift number: "))
    c=0
    result=""
    for i in str1:
            if i in alphabet:
                j=alphabet.index(i)
                c=(j-n)%26
                result+=alphabet[c]
            else:
                result+=i    
    print(f"Decrypted:{result}")                
    

def processes():
    process=input("type encrypt for encryption and decrypt for decryption:\n")
    if process=='encrypt':
        encryption()
    else:
        decryption()    

for k in range(100):
    choice=input("Do you want continue yes or no: ")
    if choice=='yes':
         processes()
    else:
         break 
print("Thanks for coming")            


