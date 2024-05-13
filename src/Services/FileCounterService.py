import os


class FileCounterService:
    def __init__(self, directory):
        self.directory = directory

    def count_files(self):
        count = 0
        for _, _, files in os.walk(self.directory):
            count += len(files)
        return count
