import os
import shutil
import configparser

class FileManager:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.working_directory = self.config['FileManager']['working_directory']
        if not os.path.exists(self.working_directory):
            os.makedirs(self.working_directory)

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.working_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.working_directory, folder_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        else:
            print("Папка не существует")

    def move_to_folder(self, folder_name):
        folder_path = os.path.join(self.working_directory, folder_name)
        if os.path.isdir(folder_path):
            self.working_directory = folder_path
            print("Перешли в папку:", self.working_directory)
        else:
            print("Папка не существует")

    def move_up(self):
        if self.working_directory != os.path.abspath('/'):
            self.working_directory = os.path.dirname(self.working_directory)
            print("Вернулись на уровень вверх:", self.working_directory)
        else:
            print("Вы уже в корневой папке")

    def create_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
        else:
            print("Файл уже существует")

    def write_to_file(self, file_name, text):
        file_path = os.path.join(self.working_directory, file_name)
        with open(file_path, 'w') as file:
            file.write(text)

    def read_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read()
        else:
            print("Файл не существует")

    def delete_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("Файл не существует")

    def copy_file(self, source_file, destination_folder):
        source_path = os.path.join(self.working_directory, source_file)
        destination_path = os.path.join(self.working_directory, destination_folder)
        if os.path.exists(source_path) and os.path.isdir(destination_path):
            shutil.copy(source_path, destination_path)
        else:
            print("Файл или папка недоступны")

    def move_file(self, source_file, destination_folder):
        source_path = os.path.join(self.working_directory, source_file)
        destination_path = os.path.join(self.working_directory, destination_folder)
        if os.path.exists(source_path) and os.path.isdir(destination_path):
            shutil.move(source_path, destination_path)
        else:
            print("Файл или папка недоступны")

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.working_directory, old_name)
        new_path = os.path.join(self.working_directory, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
        else:
            print("Файл не существует")

    def list_directory(self):
        return os.listdir(self.working_directory)

    def get_working_directory(self):
        return self.working_directory
