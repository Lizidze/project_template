import pandas as pd


def read_from_console():
    """
    Зчитує текст із консолі та повертає його.

    Повернення:
        str: Введений користувачем текст.
    """
    text = input("Введіть текст: ")
    return text

def read_from_file(filepath):
    """
    Зчитує вміст файлу та повертає його у вигляді рядка.

    Аргументи:
        filepath (str): Шлях до файлу.

    Повернення:
        str: Вміст файлу.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def read_with_pandas(filepath):
    """
    Зчитує дані з файлу у DataFrame за допомогою pandas.

    Аргументи:
        filepath (str): Шлях до файлу.

    Повернення:
        pd.DataFrame: Табличні дані з файлу.
    """
    return pd.read_csv(filepath)