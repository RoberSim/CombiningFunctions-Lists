#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Variable			Type			Purpose
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                     
# User_Input                                    String                 holds string TO BE encrypted
# Encrypt_Out                                 String                 holds string THAT IS encrypted
# CharList1                                      List                    first list to index characters
# CharList2                                      List                    second list to transform characters           

CharList1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','1','2','3','4','5','6','7','8','9','0']
CharList2 = ['4','R','5','G','Z','3','2','D','A','E','X','Y','U','I','6','W','7','O','V','8','F','Q','L','0','J','.','H','9','C','B','N','S','P','M','1','T','K']


def main():
    strMenuOption = ""
    while strMenuOption != "X":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("                 Encryption/Decryption Program                              ")
        print()
        print("                     Desire to Encrypt: Enter 1                                   ")
        print("                     Desire to Decrypt: Enter 2                                   ")
        print("                     Desire to Exit:       Enter X                                  ")
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

        strMenuOption = input("Please enter your choice:  ").upper()
        if strMenuOption == "1":
            Encrypt()

        elif strMenuOption == "2":
            Decrypt()
    else:
        exit()
        

def Encrypt():
    User_Input = input("Please enter a phrase you want encrypted:  ").upper()
    print(User_Input)
    User_Words = list(User_Input.split(""))
    for i in range(len(User_Words)):
        User_Words[i] = User_Words.strip()
        
                   
                              



# Display Encryption


#def Decrypt():
#    A


      



# Display Decryption


main()

