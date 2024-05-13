from src.Services.SortDictService.AbstractSortDictService import AbstractSortDictService
from src.main import data


class NumSortService(AbstractSortDictService):
    def sort(self):
        return sorted(self.dictionary.items(), key=lambda x: int(x[1]['№']))
