import os
dir_path = os.path.dirname(os.path.realpath(__file__)) +"/books/frankenstein.txt"
def main():
    with open(dir_path) as f:
        file_contents = f.read()
        number_words = len(file_contents.split())
        print(number_words)
def GetBookAsString():
    with open(dir_path) as f:
        file_contents = f.read()
        return file_contents
    return None
def CountCharacters(text):
    text = text.lower()
    character_dictionary = {}
    for letter in text:
        if letter in character_dictionary:
            character_dictionary[letter]+=1
        else:
            character_dictionary[letter] = 1
    return character_dictionary
dic = CountCharacters(GetBookAsString())

def Report(dic):
    print("--- Begin report of books/frankenstein.txt ---")
    for key in dic:
        print(f"The {key} character was found {dic[key]} times")
    print("--- End report ---")
Report(dic)