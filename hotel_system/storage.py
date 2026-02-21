# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
#este modulo define la clase JsonStorage para
#gestionar el almacenamiento de datos en archivos JSON.
"""
import json
import os


class JsonStorage:
    """ Clase para gestionar el almacenamiento
    de datos en archivos JSON. """
    def __init__(self, filepath):
        """ Inicializa el almacenamiento
        con la ruta del archivo JSON. """
        self.filepath = filepath
        self._ensure_file()

    def _ensure_file(self):
        """ Asegura que el archivo JSON exista,
        creando uno vacio si no existe."""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump([], file)

    def load(self):
        """ Carga los datos desde el archivo JSON,
        devolviendo una lista de objetos. """
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as error:
            print(f"Error loading file {self.filepath}: {error}")
            return []

    def save(self, data):
        """ Guarda los datos en el archivo JSON,
        sobrescribiendo el contenido existente. """
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except IOError as error:
            print(f"Error saving file {self.filepath}: {error}")
