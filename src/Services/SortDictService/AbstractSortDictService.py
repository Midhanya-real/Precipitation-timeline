from abc import abstractmethod


class AbstractSortDictService:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    @abstractmethod
    def sort(self):
        raise NotImplementedError("")
  