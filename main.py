def main():
    book_path = "bookbot/books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    letters_dictionary = get_letters_count(book_text)
    print(num_words)
    print (get_book_report(book_path, letters_dictionary, num_words))

def count_words(input_text):
    words_list = input_text.split()
    return len(words_list)

def get_book_text(input_book_path):
    with open("bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def get_letters_count(input_text):
    lower_case_text = input_text.lower()
    output_dictionary = {}
    for letter in lower_case_text:
        if letter in output_dictionary:
            output_dictionary[letter] += 1
        else:
            output_dictionary[letter] = 1
    return output_dictionary

def get_book_report(input_book_path, input_letters_dict, input_total_word_count):
    letters_string = []
    for letter in input_letters_dict:
        if letter.isalpha():
            letters_string.append(letter)

    letters_string.sort()
    letters_report_string = ""
    for letter in letters_string:
        letters_report_string += f"The letter {letter} was found {input_letters_dict[letter]} times. \n"
    
    output_string = (f"--- Begin report of {input_book_path} --- \n \n" +
                     f"There were {input_total_word_count} words found in the document. \n \n" +
                     letters_report_string +
                     "--- End report ---")
    
    return output_string
main()