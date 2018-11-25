import numpy as np


class HappinessScore(object):
    @staticmethod
    def get_scores(outcome, candidates, voter_pref):
        # sort the candidates
        outcome_reversed = np.array(outcome) * -1
        winner = candidates[np.argsort(outcome_reversed)[0]]

        # calculate the happiness score for each voter
        factor = np.array(range(len(candidates)-1, -1, -1)).reshape(len(candidates), 1)
        score = (voter_pref == winner).astype(int) * factor

        return np.amax(score, axis=0), score.sum()
