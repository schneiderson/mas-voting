from votingSchemes.AbstractScheme import AbstractScheme
import numpy as np


class Burda(AbstractScheme):

    @staticmethod
    def get_name():
        return "Borda"

    @staticmethod
    def get_scores(preferences, candidates):
        length = len(candidates)
        voting_vector = np.array(list(range(length-1, -1, -1))).reshape(length, 1)

        return [((preferences == y).astype(int) * voting_vector).sum() for y in candidates]

