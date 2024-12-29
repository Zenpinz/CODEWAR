# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

#solution:
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


#2solution:
def alphabet_position(text):
    if type(text)==str:
        text=text.lower()
        result=''
        for i in text:
            if i.isalpha():
                if i.isalpha()==True:
                    result=result + '' + str(text.index(i)+1)
        return result.lstrip(' ')