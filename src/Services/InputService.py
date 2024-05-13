import csv
from datetime import datetime


class InputService:
    def __init__(self, path: str):
        self.path = path

    def input(self) -> dict:
        with open(self.path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            data = {i: row for i, row in enumerate(reader)}

        return data
