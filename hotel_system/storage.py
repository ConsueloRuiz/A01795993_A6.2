import json
import os


class JsonStorage:
    def __init__(self, filepath):
        self.filepath = filepath
        self._ensure_file()

    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump([], file)

    def load(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error loading file {self.filepath}: {error}")
            return []

    def save(self, data):
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            print(f"Error saving file {self.filepath}: {error}")
