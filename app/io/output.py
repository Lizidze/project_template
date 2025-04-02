ef print_to_console(text):
    """
    Виводить текст у консоль.

    Аргументи:
        text (str): Текст для виводу у консоль.
    """
    print(text)

def write_to_file(filepath, text):
    """
    Записує текст у файл.

    Аргументи:
        filepath (str): Шлях до файлу.
        text (str): Текст, який потрібно записати.
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(text)