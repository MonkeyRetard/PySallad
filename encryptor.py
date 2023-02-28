# Made 2-28-23 Tuesday

# This file encrypts and decrypts Sallad encrypted items
# The encryption works by taking the list of the valid letters, finding the current letter of the given String, 
# then getting the letter 5 places infront of the current String

# This will encrypt the Data Given
class Sallad_Encryption:
    global valid_letters
    valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}:\"<>?,./;'[]+_=-\|`~"

    # Encrypts the given String
    def encryption(string):
        new_data = ""
        for new in range(len(str(string))):
            for letter in range(len(valid_letters)):
                #print(valid_letters[letter:letter+1])
                # This checks if it needs to start at the beginning
                if str(string)[new:new+1] == valid_letters[letter:letter+1]:
                    #print(f'new: {str(string)[new:new+1]} | letter: {valid_letters[letter+5:letter+6]}')
                    if letter+5 < len(valid_letters):
                        # If the list does not have to start at the beginning of "valid_letters"
                        new_data += valid_letters[letter+5:letter+6]
                    else:
                        # If the given letter does have to start at the beginning of "valid_letters"
                        index = letter - len(valid_letters)
                        new_data += valid_letters[index+5:index+6]     
        return new_data     

    # Decrypts the given String
    def decryption( string):
        new_data = ""
        for new in range(len(str(string))):
            for letter in range(len(valid_letters)):
                #print(valid_letters[letter:letter+1])
                # This checks if it needs to start at the beginning
                if str(string)[new:new+1] == valid_letters[letter:letter+1]:
                    #print(f'new: {str(string)[new:new+1]} | letter: {valid_letters[letter-5:letter-4]}')
                    if letter-5 < len(valid_letters):
                        # If the list does not have to start at the end of "valid_letters"
                        new_data += valid_letters[letter-5:letter-4]
                    else:
                        # If the given letter does have to start at the end of "valid_letters"
                        index = len(valid_letters) - letter
                        new_data += valid_letters[index-5:index-4]   
        return new_data 