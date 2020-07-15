import string #import library strings
def letters_file_line(n): #define funtion
   with open("words1.txt", "w") as f: #open the file
       alphabet = string.ascii_uppercase #will upper the letter
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)] #read all letter of alphabet
       f.writelines(letters) #writte the letters
letters_file_line(3)#end of code