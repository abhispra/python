'''
Created on 18-Jan-2015

@author: abhispra
'''
import random

class subCipher:
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    keyTable = {}
    def __init__(self):
        for val in self.alpha:
            pos = random.randint(0, len(self.values) - 1)
            key = self.values[pos]
            self.keyTable[val] = self.alpha[key]
            self.values.remove(key) 
        print (self.keyTable)
        
    def encrypt(self, message):
        encryptedMsg = ""
        for char in message:
            try:
                char = str.lower(char)
                encryptedMsg += self.keyTable[char]
            except:
                print "Only alphabets allowed in message"
                break
        return encryptedMsg
    
    def decrypt(self, encryptedMsg):
        decryptedMsg = ""
        found = 0
        for char in encryptedMsg:
            for key in self.keyTable:
                if self.keyTable[key] == char:
                    decryptedMsg += key
                    found = 1
                    break
            if found == 0:
                raise Exception("Invalid character in message")
            else:
                found = 0
        return decryptedMsg
    
message = raw_input("Enter the message to be encrypted: ")
cipher = subCipher()
encryptedMsg = cipher.encrypt(message)
print encryptedMsg
print cipher.decrypt(encryptedMsg)