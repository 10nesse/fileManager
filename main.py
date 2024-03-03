from file_manager import FileManager

def main():
    file_manager = FileManager('config.ini')

    print("Добро пожаловать в файловый менеджер!")

    while True:
        print("\nДоступные команды:")
        print("1. Список файлов и папок")
        print("2. Создать папку")
        print("3. Удалить папку")
        print("4. Перейти в папку")
        print("5. Выйти из папки")
        print("6. Создать файл")
        print("7. Записать текст в файл")
        print("8. Просмотреть содержимое файла")
        print("9. Удалить файл")
        print("10. Копировать файл")
        print("11. Переместить файл")
        print("12. Переименовать файл")
        print("13. Выйти из программы")

        choice = input("Введите номер команды: ")

        if choice == "1":
            print("Содержимое текущей директории:")
            print(file_manager.list_directory())

        elif choice == "2":
            folder_name = input("Введите имя новой папки: ")
            file_manager.create_folder(folder_name)
            print(f"Папка '{folder_name}' создана.")

        elif choice == "3":
            folder_name = input("Введите имя папки для удаления: ")
            file_manager.delete_folder(folder_name)
            print(f"Папка '{folder_name}' удалена.")

        elif choice == "4":
            folder_name = input("Введите имя папки для перехода: ")
            file_manager.move_to_folder(folder_name)
            print(f"Перешли в папку '{folder_name}'.")

        elif choice == "5":
            file_manager.move_to_parent_folder()
            print("Вернулись в родительскую папку.")

        elif choice == "6":
            file_name = input("Введите имя нового файла: ")
            file_manager.create_file(file_name)
            print(f"Файл '{file_name}' создан.")

        elif choice == "7":
            file_name = input("Введите имя файла для записи текста: ")
            text = input("Введите текст для записи в файл: ")
            file_manager.write_to_file(file_name, text)
            print(f"Текст успешно записан в файл '{file_name}'.")

        elif choice == "8":
            file_name = input("Введите имя файла для просмотра содержимого: ")
            content = file_manager.read_file(file_name)
            if content is not None:
                print(f"Содержимое файла '{file_name}':")
                print(content)

        elif choice == "9":
            file_name = input("Введите имя файла для удаления: ")
            file_manager.delete_file(file_name)
            print(f"Файл '{file_name}' удален.")

        elif choice == "10":
            source_file = input("Введите имя файла для копирования: ")
            destination_folder = input("Введите имя папки, в которую нужно скопировать файл: ")
            file_manager.copy_file(source_file, destination_folder)
            print(f"Файл '{source_file}' успешно скопирован в папку '{destination_folder}'.")

        elif choice == "11":
            source_file = input("Введите имя файла для перемещения: ")
            destination_folder = input("Введите имя папки, в которую нужно переместить файл: ")
            file_manager.move_file(source_file, destination_folder)
            print(f"Файл '{source_file}' успешно перемещен в папку '{destination_folder}'.")

        elif choice == "12":
            old_file_name = input("Введите текущее имя файла: ")
            new_file_name = input("Введите новое имя файла: ")
            file_manager.rename_file(old_file_name, new_file_name)
            print(f"Файл переименован с '{old_file_name}' на '{new_file_name}'.")

        elif choice == "13":
            print("До свидания!")
            break

        else:
            print("Некорректная команда. Пожалуйста, выберите номер из списка.")

if __name__ == "__main__":
    main()
