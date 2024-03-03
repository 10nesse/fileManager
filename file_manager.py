import os
import shutil

# Получение текущего рабочего каталога
CURRENT_DIRECTORY = os.getcwd()

# Функция для создания папки
def create_folder(folder_name):
    try:
        os.mkdir(os.path.join(CURRENT_DIRECTORY, folder_name))
        print(f"Папка '{folder_name}' успешно создана.")
    except FileExistsError:
        print(f"Папка с именем '{folder_name}' уже существует.")

# Функция для удаления папки
def delete_folder(folder_name):
    try:
        os.rmdir(os.path.join(CURRENT_DIRECTORY, folder_name))
        print(f"Папка '{folder_name}' успешно удалена.")
    except FileNotFoundError:
        print(f"Папка '{folder_name}' не найдена.")
    except OSError as e:
        print(f"Ошибка при удалении папки '{folder_name}': {e}")

# Функция для перемещения в другую папку
def move_to_folder(folder_name):
    global CURRENT_DIRECTORY
    new_directory = os.path.join(CURRENT_DIRECTORY, folder_name)
    if os.path.isdir(new_directory):
        CURRENT_DIRECTORY = new_directory
        print(f"Перешли в папку '{folder_name}'.")
    else:
        print(f"Папка '{folder_name}' не существует.")

# Функция для выхода на уровень вверх
def move_up():
    global CURRENT_DIRECTORY
    parent_directory = os.path.dirname(CURRENT_DIRECTORY)
    if parent_directory != CURRENT_DIRECTORY:
        CURRENT_DIRECTORY = parent_directory
        print("Вернулись на уровень вверх.")
    else:
        print("Вы уже на верхнем уровне.")

# Функция для создания пустого файла
def create_file(file_name):
    file_path = os.path.join(CURRENT_DIRECTORY, file_name)
    try:
        with open(file_path, 'w'):
            pass
        print(f"Файл '{file_name}' успешно создан.")
    except OSError as e:
        print(f"Ошибка при создании файла '{file_name}': {e}")

# Функция для записи текста в файл
def write_to_file(file_name, text):
    file_path = os.path.join(CURRENT_DIRECTORY, file_name)
    try:
        with open(file_path, 'w') as f:
            f.write(text)
        print(f"Текст успешно записан в файл '{file_name}'.")
    except OSError as e:
        print(f"Ошибка при записи текста в файл '{file_name}': {e}")

# Функция для просмотра содержимого файла
def view_file(file_name):
    file_path = os.path.join(CURRENT_DIRECTORY, file_name)
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        print(f"Содержимое файла '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except IsADirectoryError:
        print(f"'{file_name}' является папкой, а не файлом.")
    except OSError as e:
        print(f"Ошибка при чтении файла '{file_name}': {e}")

# Функция для удаления файла
def delete_file(file_name):
    file_path = os.path.join(CURRENT_DIRECTORY, file_name)
    try:
        os.remove(file_path)
        print(f"Файл '{file_name}' успешно удален.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except IsADirectoryError:
        print(f"'{file_name}' является папкой, а не файлом.")
    except OSError as e:
        print(f"Ошибка при удалении файла '{file_name}': {e}")

# Функция для копирования файла
def copy_file(file_name, destination_folder):
    source_file_path = os.path.join(CURRENT_DIRECTORY, file_name)
    destination_folder_path = os.path.join(CURRENT_DIRECTORY, destination_folder)
    try:
        shutil.copy(source_file_path, destination_folder_path)
        print(f"Файл '{file_name}' успешно скопирован в папку '{destination_folder}'.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except IsADirectoryError:
        print(f"'{file_name}' является папкой, а не файлом.")
    except OSError as e:
        print(f"Ошибка при копировании файла '{file_name}': {e}")

# Функция для перемещения файла
def move_file(file_name, destination_folder):
    source_file_path = os.path.join(CURRENT_DIRECTORY, file_name)
    destination_folder_path = os.path.join(CURRENT_DIRECTORY, destination_folder)
    try:
        shutil.move(source_file_path, destination_folder_path)
        print(f"Файл '{file_name}' успешно перемещен в папку '{destination_folder}'.")
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except IsADirectoryError:
        print(f"'{file_name}' является папкой, а не файлом.")
    except OSError as e:
        print(f"Ошибка при перемещении файла '{file_name}': {e}")

# Функция для переименования файла
def rename_file(old_name, new_name):
    old_file_path = os.path.join(CURRENT_DIRECTORY, old_name)
    new_file_path = os.path.join(CURRENT_DIRECTORY, new_name)
    try:
        os.rename(old_file_path, new_file_path)
        print(f"Файл '{old_name}' успешно переименован в '{new_name}'.")
    except FileNotFoundError:
        print(f"Файл '{old_name}' не найден.")
    except IsADirectoryError:
        print(f"'{old_name}' является папкой, а не файлом.")
    except OSError as e:
        print(f"Ошибка при переименовании файла '{old_name}': {e}")

if __name__ == "__main__":
    # Пример использования функций
    create_folder("test_folder")
    move_to_folder("test_folder")
    create_file("test_file.txt")
    write_to_file("test_file.txt", "Hello, world!")
    view_file("test_file.txt")
    rename_file("test_file.txt", "renamed_file.txt")
    copy_file("renamed_file.txt", "backup_folder")
    move_file("renamed_file.txt", "new_folder")
    delete_file("renamed_file.txt")
    delete_folder("new_folder")
    move_up()
    delete_folder("test_folder")
