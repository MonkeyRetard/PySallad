# Made 2-28-23 Tuesday

# This file encrypts, decrypts, generates IDs, and Generates Seeds items
# The encryption works by taking the list of the valid letters, finding the current letter of the given String, 
# then getting the letter 5 places infront of the current String

# Imports
import random
import time

# This will encrypt the Data Given
class Sallad_Encryption:
    global valid_letters
    valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}:\"<>?,./;'[]+_=-\|`~"

    # Encrypts the given String
    def encrypt(string):
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
    def decrypt(string):
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
    
# This class can generate Seeds (WIP) and IDs
class Generate:
    global valid_letters, valid_numbers, valid_symbols
    valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid_numbers = "1234567890"
    valid_symbols = "!@#$%^&*(){}:\"<>?,./;'[]+_=-\|`~"

    # Generates an ID with the given "ud_length"
    def generate_id(id_length, has_letters=False, has_numbers=False, has_symbols=False):

        # Checks if the letters are booleans
        if type(has_letters) is not bool: raise TypeError(f'The Parameter "has_letters": {has_letters} is not a boolean'); # Raise a error if "has_letters" is not a boolean
        if type(has_numbers) is not bool: raise TypeError(f'The Parameter "has_numbers": {has_numbers} is not a boolean'); # Raise a error if "has_numbers" is not a boolean
        if type(has_symbols) is not bool: raise TypeError(f'The Parameter "has_symbols": {has_symbols} is not a boolean'); # Raise a error if "has_symbols" is not a boolean
        
        # Checks if all of the parameters are false | If they are all false it enables "has_letters"
        if (bool(has_letters) == False) and (bool(has_numbers) == False) and (bool(has_symbols) == False): has_letters = True;
        
        # This combines all the given items into one
        valid_items = ""
        if has_letters == True: valid_items += valid_letters;
        if has_numbers == True: valid_items += valid_numbers;
        if has_symbols == True: valid_items += valid_symbols;

        # This makes the Id
        output = ""
        while True:
            # Generates a random number
            random_number = random.randint(0, len(valid_items)-1)
            # Adds the random selected number to the output
            output += valid_items[random_number:random_number+1]

            # Checks if the length of the output is equaled to "id_length"
            if len(output) == id_length: break;

        # Returns the generated ID
        return output
        
print(Generate.generate_id(7))

#print(str(time.ctime(time.time())))