#Write a function called single_letter_count. This function takes in two parameters (two strings).
# The first parameter should be a word and the second should be a letter.
# The function returns the number of times that letter appears in the word.
# The function should be case insensitive (does not matter if the input is lowercase or uppercase).
# If the letter is not found in the word, the function should return 0.


lettercount = 0
#count_of_letter = 0


def single_letter_count(wordlow, letterlow):

    #for ltr in wordlow:
      #  if ltr == letterlow:
        #    lettercount = lettercount + 1
    count_of_letter = int(wordlow.count (letterlow))
    if count_of_letter == 0:
        print("There are 0 instances of the letter ", letterlow, "in the word ", wordlow,".")
    elif count_of_letter == 1:
        print("There is 1 instance of ", letterlow, "in the word ", wordlow, ".")
    else:
        print("There are ", count_of_letter, "instances of the letter ", letterlow, "in the word ", wordlow,".")

word = input("Please enter a word: ")
wordlow = (word.lower())


letter = input ("What letter would you like to look for within the word? ")
letterlow = (letter.lower())

single_letter_count (wordlow, letterlow)


