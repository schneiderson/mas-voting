from votingSchemes.AbstractScheme import AbstractScheme
import numpy as np


class Burda(AbstractScheme):

    @staticmethod
    def get_score(preferences, candidates):
        return [((preferences == y).astype(int) * np.array([4, 3, 2, 1, 0]).reshape(5, 1)).sum() for y in candidates]

