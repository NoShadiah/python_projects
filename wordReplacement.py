# Here am using the replace method to help the user replace a word from my statement.
def replace_word():
    str = 'Hallo there, hope you are doing great'
    print(str)
    word_to_replace = input("Enter the word to replace: ")
    word = input('Enter the new word: ')
    
    print(str.replace(word_to_replace, word))

replace_word()

# in this part, am prompting the user to input data and later incase of any chhange to be made, they can change
def replace_input():
    str = input('Enter a sentence that you can correct later: ')
    print(str)
    word_to_replace = input("Enter the word to replace: ")
    word = input('Enter the new word: ')
    
    print(str.replace(word_to_replace, word))

replace_input()
