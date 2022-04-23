def is_palindrome_iterative(word):
    """ Verifica de forma iterativa se a palavra é um palindromo,
    returna True ou False """
    if not word:
        return False
    try:
        return interative_palindrome(word)
    except (ValueError, TypeError):
        return False


def interative_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True
