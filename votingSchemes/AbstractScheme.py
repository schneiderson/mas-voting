import abc


class AbstractScheme(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def get_score(self, preferences):
        pass
