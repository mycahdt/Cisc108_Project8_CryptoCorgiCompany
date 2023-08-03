"""
# Crypto Corgi Company
Build some simple functions that encrypt, decrypt, and hash text
for cryptography purposes.
Date: Spring 2020
Course: CISC108
School: University of Delaware

# When You Are Done
When you pass all tests, remember to clean and document your code.
But we will be reviewing your documentation and code quality!
Yes, you have to unit test all your functions.
"""

from cisc108 import assert_equal


def text_toInts(text: str) -> [int]:
    '''
    Consumes 'text' and produces a list of integers based
    upon the ASCII value of each character in the text.
    
    Args:
        text (str): The given string of text.
    Returns:
        [int]: The list of integers which are the ASCII values
            of the given text. 
    '''
    integerList = []
    for letter in text:
        integerList.append(ord(letter))
    return integerList

def rotate_OneInt(original: int, rotation: int) -> int:
    '''
    Consumes an 'original' int value and a 'rotation' int value,
    which are used to rotate the original integer in order to produce
    a new integer value.
    
    Args:
        original (int): The original integer value.
        rotation (int): The amount that the integer value will be rotated.
    Returns:
        int: The new integer that is produced when the original integer is rotated. 
    '''
    return (original + rotation - 32) % 94 + 32

def rotate_AllInts(integerList: [int], rotation: int) -> [int]:
    '''
    Consumes an 'integerList' and a 'rotation' int value,
    and rotates all of the integer values in integerList
    in order to produce a new list of integers.
    
    Args:
        integerList ([int]): The given list of integers.
        rotation (int): The amount that all of the integer values will be rotated. 
    Returns:
        [int]: The new list of integers that is produced when
            all of the values in integerList are rotated.  
    '''
    rotatedIntList = []
    for myInteger in integerList:
        rotatedIntList.append(rotate_OneInt(myInteger, rotation))
    return rotatedIntList

def insert126(rotatedIntList: [int]) -> [int]:
    '''
    Consumes a 'rotatedIntList' and produces an new
    list of integers that includes the number 126 after
    any integer less than 48.
    
    Args:
        rotatedIntList ([int]): The given list of rotated integers.
    Returns:
        [int]: The new list of integers that is produced when
            126 is added to the rotatedIntList.  
    '''
    finalIntList = []
    for myInteger in rotatedIntList:
        finalIntList.append(myInteger)
        if myInteger < 48:
            finalIntList.append(126)
    return finalIntList

def ints_toText(finalIntList: [int]) -> str:
    '''
    Consumes a 'finalIntList' and produces a string,
    by converting the list fo integers into strings,
    based upon each of their ASCII characters. 
    
    Args:
        finalIntList ([int]): The given list of integers.
    Returns:
        str: The string that is produced when the finalIntList
            is converted to a string.
    '''
    myString = ""
    for myInteger in finalIntList:
        myString = myString + chr(myInteger)
    return myString

def remove126(finalIntList: [int]) -> [int]:
    '''
    Consumes a 'finalIntList' and produces an new
    list of integers that does not include the number 126.
    
    Args:
        finalIntList ([int]): The given list of integers.
    Returns:
        [int]: The new list of integers that is produced when
            126 is removed from the original list.  
    ''' 
    myRemovedList = []
    for num in finalIntList:
        if num != 126:
            myRemovedList.append(num)
    return myRemovedList

# 1) Define encrypt_text
def encrypt_text(plainMessage: str, rotation_amount: int) -> str:
    '''
    Consumes a 'plainMessage' and a 'rotation_amount',
    and produces an excrypted string message. The plainMessage is
    converted to a list of its ASCII integer values, and then
    the list is rotated by rotation_amount of times, and then
    the value of 126 is inserted into the list, and then the list
    of integers is converted back into a string
    
    Args:
        plainMessage (str): The given string that the user wants to encrypt.
        rotation_amount: The amount that all of the integer values will be rotated. 
    Returns:
        str: The encrypted string message. 
    '''
    integerList = text_toInts(plainMessage)
    rotatedIntList = rotate_AllInts(integerList, rotation_amount)
    finalIntList = insert126(rotatedIntList)
    encryptedText = ints_toText(finalIntList)
    return encryptedText
    

# 2) Define decrypt_text
def decrypt_text(encryptedMessage: str, rotation_amount: int) -> str:
    '''
    Consumes an 'encryptedMessage' and a 'rotation_amount',
    and produces a decryted string message. The encryptedMessage is
    converted to a list of its ASCII integer values, and then
    the value of 126 is removed from the list, and then the list
    is rotated backwards by rotation_amount of times, and then
    the list is converted back into a string. 
    
    Args:
        encryptedMessage (str): The given string that the user wants to decrypt.
        rotation_amount: The amount that all of the integer values will be rotated. 
    Returns:
        str: The decryted string message. 
    '''
    finalIntList = text_toInts(encryptedMessage)
    rotatedIntList = remove126(finalIntList)
    integerList = rotate_AllInts(rotatedIntList, -rotation_amount)
    decryptedText = ints_toText(integerList)
    return decryptedText




def transformInt(base: int, myInts: [int]) -> [int]:
    '''
    Consumes a base (integer) and myInts (list of integers),
    and uses these to transform the list of integers to
    produce a new list of integers. 
    
    Args:
        base (int): Integer values used to transform the each integer.
        myInts ([int]): The list of integers that will be transformed.
    Returns:
        [int]: The list of transformed integers. 
    '''
    myNewList = []
    count = 0
    for num in myInts:
        myNewList.append((count + base) ** num)
        count = count + 1
    return myNewList

def summate(myList: [int]) -> int:
    '''
    Consumes myList which are a list of integers,
    which are added all together to produce
    an integer that represents the sum. 
    
    Args:
        myList ([int]): The list of integers that will be added all together.
    Returns:
        int: The sum of all of the integers. 
    '''
    total = 0
    for num in myList:
        total = total + num
    return total
        
# 3) Define hash_text
def hash_text(text: str, base: int, hash_size: int) -> int:
    '''
    Consumes a 'text', a 'base' (integer), a 'hash_size',
    which are used in order to change the text into an
    integer that represents the hashed value. This is done
    by turing the string of text into a list of integers,
    and then transforming each integer, and then finding
    the total sum of the list of transformed integers, and
    then limiting the total value to hash_size.
    
    Args:
        text (str): The string of text that will be hashed.
        base (int): Integer values used to transform the each integer.
        hash_size (int): The integer value used for limiting the
            total value of the hashed value. 
    Returns:
        int: The integer which is the hashed value of the text. 
    '''
    myIntList = text_toInts(text)
    myTransformedList = transformInt(base, myIntList)
    totalSum = summate(myTransformedList)
    hashedValue = totalSum % hash_size
    return hashedValue
    

    

# 4) Define main
def main():
    """
    Main function that calls all the other functions and provides
    a crypto experience
    """
    # ...
    userInput = input("Type encrypt or decrypt:")
    if userInput == "encrypt":
        usersPlainTxt = input("Type your plaintext message:")
        encryptedMessage = encrypt_text(usersPlainTxt, 5)
        hashMessage = hash_text(encryptedMessage, 31, 1000000000)
        print(encryptedMessage)
        print(hashMessage)
    elif userInput == "decrypt":
        usersEncryptedTxt = input("Type you encrypted message:")
        decryptedMessage = decrypt_text(usersEncryptedTxt, 5)
        hashMessage = hash_text(decryptedMessage, 31, 1000000000)
        expectedHash = input("Type the expected hash:")
        if hashMessage != expectedHash:
            print("There was an error")
    else:
        print("Error: must type 'encrypt' or 'decrypt'")



assert_equal(text_toInts('Hello! $'), [72, 101, 108, 108, 111, 33, 32, 36])
assert_equal(rotate_OneInt(101, 3), 104)
assert_equal(rotate_AllInts([72, 101, 108, 108, 111, 33, 32, 36], 3), [75, 104, 111, 111, 114, 36, 35, 39])
assert_equal(insert126([75, 104, 111, 111, 114, 36, 35, 39]), [75, 104, 111, 111, 114, 36, 126, 35, 126, 39, 126])
assert_equal(ints_toText([75, 104, 111, 111, 114, 36, 126, 35, 126, 39, 126]), "Khoor$~#~'~")
assert_equal(remove126([75, 104, 111, 111, 114, 36, 126, 35, 126, 39, 126]), [75, 104, 111, 111, 114, 36, 35, 39])
assert_equal(encrypt_text('Hello! $', 3), "Khoor$~#~'~")
assert_equal(decrypt_text("Khoor$~#~'~", 3), 'Hello! $')
assert_equal(transformInt(31,[2, 3, 4]), [961, 32768, 1185921])
assert_equal(summate([5, 6, 7]), 18)
assert_equal(hash_text('CAT', 31, 1000000000), 146685664)




# The following lines of code are used to call the main function.
# Professional Python programmers always guard their main function call with
#   this IF statement, to make it easier for other users to call their code.
# For now, just leave this code alone, but recognize that it is how you are
#   calling your main function.
if __name__ == '__main__':
    main()



