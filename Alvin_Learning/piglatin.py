
"""
HW for Alvin:

Take a sentence and convert ever word to pig latin

Example:
--------

"I am a very well groomed zebra"

gives:

"Ie mae ae erye ellwe roomedge ebraze"
"""

# Solve the problem for this String:
english = "The death star will be rebuilt next year"


# This is how you split a string:
#stuff = "Here is an example sentence to split"
#stuff_list = stuff.split()  # This splits the sentence into a list by spaces by default.
#print(stuff_list)


# I can take part of a string out by indexing it's values:
#mystr = "blaaaaabulllaaa"
#newstr = mystr[2:5]
#print(newstr)


# I can add strings together to make a new string
#a = "pre"
#b = "historic"
#print(a + b)


# I can reverse a string in a for loop
#forward_string = "forward"
#backward_string = ''
#for l in range(len(forward_string)):
    #backward_string += forward_string[-1] k

#pig = "e"
#word = input()
#first = word[0]

#new = word + first + pig
#new_word = new[1:]
#print(new_word)


def main():
    words = str(input("Input Sentence:")).split()
    for word in words:
        print(word[1:] + word[0] + "e", end="chicken sauce")
    print ()

main()