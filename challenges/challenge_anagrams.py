def is_anagram(first_string, second_string):
    """ Algoritmos para encontrar anagramas com complexidade maxima O """
    first_string_ordened = merge_sort(list(first_string.lower()))
    second_string_ordened = merge_sort(list(second_string.lower()))

    return first_string_ordened == second_string_ordened


def merge_sort(array):
    # caso base: se já atingiu a menor porção (1)
    if len(array) <= 1:
        # retorne o array
        return array
    # calculo do pivot: índice que indica onde o array será particionado
    # no caso, metade
    mid = len(array) // 2
    # para cada metade do array
    # chama a função merge_sort de forma recursiva
    left, right = merge_sort(array[:mid]), merge_sort(
        array[mid:])
    # mistura as partes que foram divididas
    return merge(left, right, array.copy())


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

# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/766d59bd-a04f-41a9-b41b-5fb37a2f2a3a/algoritmos-de-ordenacao/1adc1a6e-51c7-4065-ae2c-e5f8194e7578?use_case=side_bar
