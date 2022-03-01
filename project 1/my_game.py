import numpy as np

def random_predict() -> int:
    """Угадываем рандомное число
           
    Returns:
        int: Число попыток
    """
    number = np.random.randint(1, 101)
    count = 0
    min = 1
    max = 101
    
    while True:
        count += 1
        predict_number = (min+max)//2 #предполагаемое число
        if number > predict_number:
            min = predict_number
        elif number < predict_number:
            max = predict_number
        else:
            # print(f"Компьютер угадал число за {count} попыток. Это число {predict_number}")
            break #Выход из цикла, если угадали
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict())

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
if __name__ == '__main__': #RUN   
    score_game(random_predict)
