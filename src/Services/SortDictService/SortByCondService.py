from src.Services.SortDictService.AbstractSortDictService import AbstractSortDictService


class SortByCondService(AbstractSortDictService):
    def __init__(self, dictionary, sortByCond):
        super().__init__(dictionary)
        self._sort_by_cond = sortByCond

    @staticmethod
    def is_higher(dictRow: int, num: int):
        return dictRow > num

    def sort(self):
        return sorted([(date, value) for date, value in self.dictionary.items() if
                       SortByCondService.is_higher(int(value['№']), self._sort_by_cond)],
                      key=lambda x: x[0])
