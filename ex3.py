def longest_word(filename):
    #define the funtion

    with open(filename, 'r') as infile: #open the file as infile
              words = infile.read().split() #variable
    max_len = len(max(words, key=len)) #max of letter and read it
    return [word for word in words if len(word) == max_len] #will return letter per letter

print(longest_word('test.txt')) #print the code letters