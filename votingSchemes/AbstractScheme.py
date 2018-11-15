import abc


class AbstractScheme(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def get_name(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def get_scores(self, preferences, candidates):
        pass

