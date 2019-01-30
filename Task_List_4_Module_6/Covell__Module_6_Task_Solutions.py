# Write a Python program to perform the following tasks:

# Receive a filename from the user,
# open the text file for reading, and
# read the file.
# Count the sentences in the text file.
# Count the number of words in the text file.
# Print these two values with appropriate labels as a result of running the program.

# Here is Task 1

print("\nThis will count the number of sentences in the source file.\n\n")

import sys

file = open("source_File.txt")
contents = file.read()

def split_a_sentence(contents):
    import re
    sentenceEnds = re.compile('[.!?]')
    sentenceSplit = sentenceEnds.split(contents)
    return sentenceSplit
  
if __name__ == '__main__':  
    sentenceCount = 0
    sentences = split_a_sentence(contents)
    for s in sentences:
         sentenceCount += 1
         print (s.strip())
    print("There are " + str(sentenceCount) + " sentences.")


file.close


# Here is Task 2

print("\nThis will read the source file and print how many words are in it.\n")

file2 = open("source_File.txt")
contents2 = file2.read()
words2 = contents2.split()

count = 0

for word in words2:
    print(word)
    count += 1
   
print("\nThe source file has " + str(count) + " words. \n")

file2.close

     





 
