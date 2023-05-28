import requests

class test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        """Создание случайной шутки"""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код :" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успех лул")
        else:
            print("Лох")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Chuck на месте")
        else:
            print("Chuck отсутствует")
       # check_info = check.get("categories")
       # print(check_info)
       # assert check_info == []
       # print("Категория верна")



random_joke = test_new_joke()
random_joke.test_create_new_random_joke()