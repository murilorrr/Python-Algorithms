def is_palindrome_recursive(word, low_index, high_index):
    """ Verifica se uma palavra é palíndroma """
    try:
        if word == '':
            return False
        equal_letters = word[low_index] == word[high_index]
        if equal_letters is not True:
            return False
        if low_index >= high_index:
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except IndexError:
        return False
