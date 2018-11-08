from votingSchemes.AbstractScheme import AbstractScheme
import numpy as np


class VotingForTwo(AbstractScheme):
    @staticmethod
    def get_scores(preferences, candidates):
        voting_vector = [0] * (len(candidates))
        voting_vector[0] = 1
        voting_vector[1] = 1
        voting_vector = np.array(voting_vector).reshape(len(candidates), 1)

        return [((preferences == y).astype(int) * voting_vector).sum() for y in candidates]
