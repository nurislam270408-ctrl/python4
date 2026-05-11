import os


class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def check_file(self):
        if os.path.exists(self.filepath):
            print(f"File '{self.filepath}' found.")
        else:
            print(f"File '{self.filepath}' not found.")
            raise FileNotFoundError(f"File '{self.filepath}' does not exist.")

    def create_output_folder(self, folder='output'):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder '{folder}' created.")
        else:
            print(f"Folder '{folder}' already exists.")
