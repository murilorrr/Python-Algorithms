def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    try:
        for i in range(len(word)):
            if word[i] != word[len(word) - i - 1]:
                return False
        return True
    except (TypeError, IndexError, ValueError):
        return False
