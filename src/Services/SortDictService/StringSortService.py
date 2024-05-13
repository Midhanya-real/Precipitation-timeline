from datetime import datetime

from src.Services.SortDictService.AbstractSortDictService import AbstractSortDictService


class StringSortService(AbstractSortDictService):
    def sort(self):
        return sorted(self.dictionary.items(),
                      key=lambda x: datetime.strptime(x[1]['дата и время'], '%d.%m.%Y %H:%M'))
