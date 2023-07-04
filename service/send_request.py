import requests
import json
import random
import string
from tqdm import tqdm


def generate_passenger():
    # Списки возможных значений для каждого параметра
    names = ["John", "Sarah", "Mike", "Anna", "Jacob", "Emma"]
    pclasses = [1, 2, 3]
    sexes = ["male", "female"]
    ages = list(range(1, 101))
    embarked_list = ["S", "C", "Q"]
    fares = [x for x in range(10, 500, 10)]
    sibsp_values = list(range(0, 9))
    parch_values = list(range(0, 7))
    tickets = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(1000)]

    # Выбираем случайное значение для каждого параметра
    passenger = {
        "Name": random.choice(names),
        "Pclass": random.choice(pclasses),
        "Sex": random.choice(sexes),
        "Age": random.choice(ages),
        "Embarked": random.choice(embarked_list),
        "Fare": random.choice(fares),
        "SibSp": random.choice(sibsp_values),
        "Parch": random.choice(parch_values),
        "Ticket": random.choice(tickets),
    }

    return passenger


url = 'http://127.0.0.1:8000/predict?passenger_id=1'

if __name__ == '__main__':

    for i in tqdm(range(0, 100)):
        # Генерируем случайные данные о пассажире
        passenger = generate_passenger()

        # Преобразуем данные в формат JSON
        passenger_data = json.dumps(passenger)

        # Выполняем POST-запрос
        response = requests.post(url, data=passenger_data, headers={'Content-Type': 'application/json'})

        # Проверяем статус ответа
        if response.status_code != 200:
            print('Request failed')
            print('Response:', response.text)
