
def encrypt(plan,key): 
    new_char =''
    
    for char in  plan:
        r = range(91,97)
        if (ord(char)) == 32:
            new_char += char
        if (ord(char)) <65 or (ord(char)) > 122 or (ord(char)) in r:
            continue
        new_index = (ord(char))+(key % 26)
        if new_index < 123:
            if ord(char) < 91 and new_index < 91:
                new_char += chr(new_index)
            elif ord(char) < 91 and new_index > 90:
                new_char += chr((new_index%91)+65)  
            else:
                new_char += chr(new_index)
        else:
            new_char += chr((new_index%123)+97)
    return new_char  

def decrypt(encrypts,key):
   return encrypt(encrypts,-key)
     
     
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()     
     
import re 
    
def count_words(text):

    words = text.split()

    word_count = 0

    for candidate_word in words:
        word = re.sub(r'[^A-Za-z]+','', candidate_word)
        if word.lower() in word_list or word in name_list:
            word_count += 1

    return word_count

def crack(phrase): 
    for key in range(0,27):
        new_phrase = decrypt(phrase,key)
        word_count = count_words(new_phrase)
        percentage = int(word_count / len(phrase.split()) * 100)
        if percentage > 50:
            return(new_phrase)    
        
             
if __name__ == '__main__':
    print(encrypt('It was the best of times, it was the worst of times.',45))
    print(decrypt('do rvn wvy yvt ',177))
    # count_words(phrase)
    # print(crack('do rvn wvy yvt'))
    

    