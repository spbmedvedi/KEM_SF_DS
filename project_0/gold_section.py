import numpy as np

def gold_section_determ(number:int=1) -> int:
    """ Алгоритм угадывания числа через "золотое сечение" 
    
    Args:
        number(int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    
    number = np.random.randint(1, 101) # Загаданное число
    
    count = 0  # Счётчик попыток
    
    # Задаём переменную списка заданного целого диапазона чисел 
    whole = list(range(1,101))     
    
    # Организовываем цикл 
    while len(whole) > 7:
        count += 1
        predict_number = whole[int(len(whole)/1.7)] # Последнее число в большей части диапазона
        if predict_number > number:
            whole = list(range(whole[0], predict_number)) # Новым целым становиться большая часть
        elif predict_number < number:
             whole = list(range(predict_number +1, whole[-1] +1 )) # Новым целым становиться меньшая часть
        else:
            break # выход из цикла, если число угадано
        
    # Организовываем цикл  for по оставшейся части диапазона
    for predict_number in whole:
        count += 1
        if predict_number == number:
            break   # Конец алгоритма
    return count

def score_game(gold_section_determ) -> int:
    """За какое количество попыток в среднем из 1000 подходов определяет наш алгоритм

    Args:
        gold_section_determ ([type]): функция алгоритма определения

    Returns:
        int: среднее количество попыток
    """

    count_list = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_list.append(gold_section_determ(number))

    score = int(np.mean(count_list)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(gold_section_determ)