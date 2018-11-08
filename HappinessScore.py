import numpy as np


class HappinessScore(object):
    @staticmethod
    def get_scores(outcome, candidates, voter_pref):
        winner = candidates[np.argsort(outcome)[-1]]
        factor = np.array(range(len(candidates)-1, -1, -1)).reshape(len(candidates), 1)
        score = (voter_pref == winner).astype(int) * factor

        return np.amax(score, axis=0), score.sum()
