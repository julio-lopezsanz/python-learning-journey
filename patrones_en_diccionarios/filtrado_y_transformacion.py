"""
Tienes este diccionario:

scores = {
    "Ana": 8,
    "Luis": 5,
    "Sofía": 9,
    "Pedro": 6
}


Quieres obtener un nuevo diccionario
solo con las personas que tienen score ≥ 7
y multiplicar su score por 10
"""

scores = {
    "Ana": 8,
    "Luis": 5,
    "Sofía": 9,
    "Pedro": 6
}

def winners_final_score(scores_dict):
    """
    Filtra a las personas que obtuvieron un puntaje mayor o igual a 7
    y multiplica su puntaje por 10
    """
    final_score = {}

    for name,score in scores_dict.items():
        if score >= 7:
            final_score[name] = score * 10

    return final_score
    #Solucion Pythonic:return {name: score * 10 for name, score in score_dict.items() if score >= 7}

print(winners_final_score(scores))
