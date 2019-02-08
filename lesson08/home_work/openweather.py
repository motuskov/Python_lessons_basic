
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import datetime

import json
import requests
import re
import sqlite3


class City:
    def __init__(self, json_data=None, values=None):
        if json_data:
            data = json.loads(json_data)
            self.id = data["id"]
            self.name = data["name"]
            self.country = data["country"]
            self.weather_id = None
            self.temp = None
            self.date = None
        if values:
            for key, value in values.items():
                setattr(self, key, value)

    def get_weather(self, appid):
        url = f"http://api.openweathermap.org/data/2.5/weather?id={self.id}&units=metric&appid={appid}"
        response = requests.get(url)
        data = json.loads(response.content)
        self.weather_id = data["weather"][0]["id"]
        self.temp = data["main"]["temp"]
        self.date = datetime.date.today()

    def __str__(self):
        return f"{self.name:<20}{self.country if self.country else '':<5}" \
               f"{self.temp if self.temp else '':<10}{self.date if self.date else ''}"

    def write_to_db(self):
        try:
            with sqlite3.connect("cities.db") as conn:
                cur = conn.cursor()
                cur.execute(f"REPLACE INTO city "
                            f"VALUES({self.id}, '{self.name}', '{self.date:%Y%m%d}', {self.temp}, {self.weather_id});")
                return True
        except sqlite3.DatabaseError:
            return False

    @staticmethod
    def find_in_file(filename, pattern):
        with open(filename, "r", encoding="UTF-8") as f:
            data = f.read()
        cities = re.findall(r"\{\s+\"id\"\: \d+,\s+\"name\"\: \"\S*" + pattern +
                            r"\S*\",\s+\"country\"\: \"\S+\"," +
                            r"\s+\"coord\"\: \{\s+\"lon\"\: \S+,\s+\"lat\"\: \S+\s+\}\s+\}", data)
        return cities

    @staticmethod
    def init_db():
        try:
            with sqlite3.connect("cities.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='city';")
                if not cur.fetchone():
                    cur.execute("CREATE TABLE city"
                                "(id integer primary key, name varchar(255), "
                                "weather_date date, temp integer, weather_id integer);")
                    cur.commit()
                return True
        except sqlite3.DatabaseError:
            return False

    @staticmethod
    def read_from_db():
        try:
            with sqlite3.connect("cities.db") as conn:
                cur = conn.cursor()
                cities = []
                for record in cur.execute(f"SELECT * FROM city;"):
                    cities.append(City(values={"id": record[0], "name": record[1], "date": record[2],
                                       "temp": record[3], "weather_id": record[4], "country": None}))
                return cities
        except sqlite3.DatabaseError:
            return None


def print_menu():
    print()
    print("1 - Найти города по имени")
    print("2 - Узнать погоду в найденных городах")
    print("3 - Записать информацию в локальную БД")
    print("4 - Вывести информацию из локальной БД")
    print("q - Выход")


cities = []
while True:

    print_menu()

    action = input("Выберите действие: ")

    if action == "q":
        break
    elif action == "1":
        cityName = input("Введите часть названия города или название города целиком: ")
        cities_data = City.find_in_file("city.list.json", cityName)
        if len(cities_data) > 0:
            print("Найдены следующие города:")
            cities = []
            for city_data in cities_data:
                city = City(json_data=city_data)
                cities.append(city)
                print(city)
        else:
            print("Ничего не найдено.")
    elif action == "2":
        if len(cities) > 0:
            print("Погода в найденых городах:")
            with open("app.id", "r", encoding="UTF-8") as f:
                appId = f.read()
            if appId:
                for city in cities:
                    city.get_weather(appId)
                    print(city)
            else:
                print("Не удалось считать AppID.")
        else:
            print("В списке нет городов. Сначала выполните поиск городов.")
    elif action == "3":
        if not City.init_db():
            print("Инициализация БД завершилась с ошибкой.")
            continue
        for city in cities:
            if not city.write_to_db():
                print(f"Произошла ошибка при добавлении города '{city.name}' в БД.")
            else:
                print(f"Город '{city.name}' добавлен в БД.")
    elif action == "4":
        cities = City.read_from_db()
        if cities:
            print("Перечень городов в локальной БД:")
            for city in cities:
                print(city)
            cities.clear()
        else:
            print("В локальной БД нет данных.")
