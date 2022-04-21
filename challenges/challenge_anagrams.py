def is_anagram(first_string, second_string):
    """ Algoritmos para encontrar anagramas com complexidade maxima O """
    first_string_ordened = ordened_lower_string(first_string)
    second_string_ordened = ordened_lower_string(second_string)

    return first_string_ordened == second_string_ordened


def ordened_lower_string(string):
    return "".join(merge_sort(string.lower()))


def diferrent_lengths(word_A, word_B):
    """ verifica se as palavras tem tamanhos diferentes """
    if len(word_A) != len(word_B):
        return True
    return False


def algoritmo_anagrama_complex_O_power_2(first_string, second_string):
    """ Algoritmos para encontrar anagramas com complexidade O² """
    second_string = second_string.lower()

    if diferrent_lengths(first_string, second_string):
        return False

    for letter_in_first in first_string.lower():
        if letter_in_first not in second_string:
            return False
        second_string = second_string.replace(letter_in_first, "")
    return True


def merge_sort(string):
    copia_string_array = list(string)
    array_of_letters = list(string)
    # caso base: se já atingiu a menor porção (1)
    if len(array_of_letters) <= 1:
        # retorne o array
        return array_of_letters
    # calculo do pivot: índice que indica onde o array será particionado
    # no caso, metade
    mid = len(array_of_letters) // 2
    # para cada metade do array
    # chama a função merge_sort de forma recursiva
    left, right = merge_sort(array_of_letters[:mid]), merge_sort(
        array_of_letters[mid:])
    # mistura as partes que foram divididas
    return merge(left, right, copia_string_array)


# função auxiliar que realiza a mistura dos dois arrays
def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    # enquanto nenhumas das partes é percorrida por completo
    while left_cursor < len(left) and right_cursor < len(right):

        # compare os dois itens das partes e insira no array de mistura o menor
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # a iteração acima irá inserir os elementos de forma ordenada

    # quando uma das partes termina, devemos garantir
    # que a outra sera totalmente inserida no array de mistura

    # itera sobre os elementos restantes na partição "esquerda"
    # inserindo-os no array de mistura
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # itera sobre os elementos restantes na partição "direita"
    # inserindo-os no array de mistura
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
