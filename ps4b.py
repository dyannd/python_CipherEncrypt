# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
import sys
import time
import random

### HELPER CODE ###
def printProgressBar(i,max,postText):
    n_bar =10 #size of progress bar
    j= i/max
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(n_bar * j):{n_bar}s}] {int(100 * j)}%  {postText}")
    sys.stdout.flush()
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text
        

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)
        

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        self.valid_words=load_words(WORDLIST_FILENAME)
        valid_words_copy=self.valid_words.copy()
        return valid_words_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        mapping={}
        alphabet_lower='abcdefghijklmnopqrstuvwxyz'
        alphabet_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #start mapping for lowercases:
        for index in range(len(alphabet_lower)):
            if index+shift<=25:
                mapping.update({alphabet_lower[index]:alphabet_lower[index+shift]})
            else: 
                mapping.update({alphabet_lower[index]:alphabet_lower[index+shift-26]})
        for index in range(len(alphabet_upper)):
            if index+shift<=25:
                mapping.update({alphabet_upper[index]:alphabet_upper[index+shift]})
            else: 
                mapping.update({alphabet_upper[index]:alphabet_upper[index+shift-26]})
        return mapping
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new=''
        for letter in (self.message_text):
            if letter in self.build_shift_dict(shift).keys():
              new=new+self.build_shift_dict(shift)[letter]
            else:
                new=new+letter
                
        return new
    


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self,text)
        self.shift=shift
        self.encryption_dict=Message.build_shift_dict(self,self.shift)
        self.message_text_encrypted=Message.apply_shift(self,self.shift)
        
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift 

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy() 

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.change_shift=shift
        self.shift=shift
        self.encryption_dict=Message.build_shift_dict(self,self.shift)
        self.message_text_encrypted=Message.apply_shift(self,self.shift)
        
        
# x=PlaintextMessage('Hello',4)
# x.change_shift(1)
# print(x.get_shift())
# print(x.get_encryption_dict())
# print(x.get_message_text_encrypted())


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)
        self.message_text=text
        self.valid_words=Message.get_valid_words(self)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #testing each shift value:
        # for i in self.message_text:
        #     print(i)
        valid_compare={}
        text_compare={}
        for shift in range(26): 
              
            printProgressBar(shift,25,'Loading ')
            time.sleep(0.05)  
            #print just for flexing
        
            text=''
            valid=0
            current_phrase=''
            # print('Shift ',shift)
            #cycle thru each letter in the string
            index=0
            for character in self.message_text:
                last_index=len(self.message_text)-1
                #isolate the word by identifying weird stuffs below:
                if character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and index!=last_index:
                    current_phrase=current_phrase+character
                    forming_word=Message(''+current_phrase)
                    
                elif character not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':      
                    decrypted=forming_word.apply_shift(26-shift-1)
                    if is_word(self.valid_words, decrypted) == True:
                        valid=valid+1
                    text=text+decrypted+character
                    current_phrase=''
                    forming_word=Message('')
                #case for last character being a text    
                elif character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' and index==last_index:
                    forming_word=Message(current_phrase+character)
                    decrypted=forming_word.apply_shift(26-shift-1)
                    # print(decrypted)
                    if is_word(self.valid_words, decrypted) == True:
                        valid=valid+1
                    text=text+decrypted
               
                index=index+1
            
            
            valid_compare[valid]=26-shift-1
            text_compare[text]=valid
        best_shift=max(valid_compare.values())
        chosen_text=max(text_compare.values())
        
        for i in text_compare.keys():
            if text_compare[i]==chosen_text:
                best_text=i
        return (best_shift,best_text)             
                        
  
if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    # plaintext = PlaintextMessage('hello', 2)
    # print('Expected Output: jgnnq')
    # print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    # ciphertext = CiphertextMessage('jgnnq ')
    # print('Expected Output:', (24, 'hello'))
    # print('Actual Output:', ciphertext.decrypt_message())
    # # # # print(ciphertext.message_text)
    decide=2
    while decide!=0 or decide!=1:
        decide=int(input('Enter the 1 if you want to encrypt or 0 if you want to decrypt: '))
        if decide==1:
            encrypt=str(input('Enter the message for encryption: '))
            encrypt_no=int(input('Enter decrypt code from 1 to 26: '))
            hidetext=PlaintextMessage(encrypt,encrypt_no)
            print(hidetext.get_message_text_encrypted())

        
        else:
            decrypt=str(input('Enter the message for decryption: '))
            encrypted=CiphertextMessage(decrypt)
            # print(encrypted.get_message_text())
            print(encrypted.decrypt_message())
        
    
    # story_string=CiphertextMessage(get_story_string())
    # # print(story_string.get_message_text())
    # print(story_string.decrypt_message())
 
    

