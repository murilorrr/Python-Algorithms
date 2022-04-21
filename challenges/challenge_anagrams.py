def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    second_string = second_string.lower()

    if diferrent_lengths(first_string, second_string):
        return False

    for letter_in_first in first_string.lower():
        if letter_in_first not in second_string:
            return False
        second_string = second_string.replace(letter_in_first, "")
    return True


def diferrent_lengths(word_A, word_B):
    """ verifica se as palavras tem tamanhos diferentes """
    if len(word_A) != len(word_B):
        return True
    return False
