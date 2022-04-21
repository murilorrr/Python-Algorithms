def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    for letter_in_first in second_string:
        exist_letter = False
        for letter_in_second in range:
            if letter_in_first == letter_in_second:
                exist_letter = True
                second_string.remove(letter_in_second)
        if exist_letter is False:
            return False
    return True