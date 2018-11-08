from votingSchemes.AbstractScheme import AbstractScheme
import numpy as np


class Burda(AbstractScheme):

    @staticmethod
    def get_score(preferences, candidates):
        l = len(candidates)
        factor = np.array(list(range(5, 0, -1))).reshape(l, 1)
        return [((preferences == y).astype(int) * factor).sum() for y in candidates]

