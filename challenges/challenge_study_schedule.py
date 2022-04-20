def study_schedule(permanence_period, target_time):
    """ Permanence_period é um array de tuplas, enquanto target_time é o
    horario a ser teste """

    try:
        casos_totais = 0
        for tupla in permanence_period:
            entrada_estudante = tupla[0]
            saida_estudante = tupla[1]
            if entrada_estudante <= target_time <= saida_estudante:
                casos_totais += 1
        return casos_totais
    except TypeError:
            return None
