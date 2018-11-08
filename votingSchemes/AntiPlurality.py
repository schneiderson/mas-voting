from votingSchemes.AbstractScheme import AbstractScheme
import numpy as np


class AntiPlurality(AbstractScheme):
    @staticmethod
    def get_scores(preferences, candidates):
        voting_vector = [1] * (len(preferences[0]) + 1)
        voting_vector[-1] = 0
        voting_vector = np.array(voting_vector).reshape(len(preferences[0]) + 1, 1)

        return [((preferences == y).astype(int) * voting_vector).sum() for y in candidates]
