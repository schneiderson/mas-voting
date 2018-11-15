import numpy as np
from HappinessScore import HappinessScore as Hap
import copy


class Bury(object):
    def __init__(self, outcome, candidates, preferences, scheme):
        self.outcome = outcome
        self.scheme = scheme
        self.candidates = candidates
        self.preferences = preferences
        self.winner = candidates[np.argsort(outcome)[-1]]
        self.happiness = Hap.get_scores(outcome, candidates, preferences)

    def run_possibilities(self, preferences):
        unhappy_voters = np.where(((self.preferences == self.winner).astype(int)).argmax(axis=0) > 0)
        possible_strategies = {}

        for voter_id in unhappy_voters[0].tolist():
            possible_strategies = {**self.possible_combinations(preferences, voter_id), **possible_strategies}

        return possible_strategies

    def alter_pref(self, pref):
        indices = np.where(pref == self.winner)
        pref = np.append(pref, pref[indices])
        pref = np.delete(pref, indices)
        return [pref]

    def possible_combinations(self, preferences, voter_id):
        temp_pref = copy.deepcopy(preferences)
        pref = preferences[:, voter_id]
        indices = np.where(pref == self.winner)[0][0]
        before = preferences[:, voter_id][:indices + 1]
        after = preferences[:, voter_id][indices + 1:]
        possible_strategies = dict()
        possible_strategies[voter_id] = []

        for c in before:
            idx = np.where(pref == c)[0][0]
            temp_list = np.concatenate((np.delete(before, idx), after))
            count = len(pref) - idx - 1
            index = 0

            while count > 0:
                # print(voter_id, count, pref, c, np.insert(temp_list, len(pref) - index - 1, c))
                temp_pref[:, voter_id] = np.insert(temp_list, len(pref) - index - 1, c)
                outcome = self.get_outcome(temp_pref)
                new_happiness = self.get_new_happiness(outcome, voter_id)

                if new_happiness > self.happiness[0][voter_id]:
                    temp_dict = {
                        "new_pref": np.insert(temp_list, count, c),
                        "happiness": new_happiness,
                        "old_happiness": self.happiness[0][voter_id]
                    }

                    possible_strategies.get(voter_id).append(temp_dict)
                    count -= 1
                    index += 1
                    continue
                else:
                    break
        return possible_strategies

    def get_outcome(self, preferences):
        return self.scheme.get_scores(preferences, self.candidates)

    def get_new_happiness(self, outcome, voter_id):
        return Hap.get_scores(outcome, self.candidates, self.preferences)[0][voter_id]
