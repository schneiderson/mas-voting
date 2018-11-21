import numpy as np
from HappinessScore import HappinessScore as Hap
import copy
from tacticalVoting.Manipulation import Manipulation as Mani


class Bury(object):
    @staticmethod
    def get_voting(outcome, candidates, preferences, happiness, scheme):
        manipulations = []
        # get winner
        winner = candidates[np.argsort(outcome)[-1]]
        unhappy_voters = np.where(((preferences == winner).astype(int)).argmax(axis=0) > 0)

        # for each voter who didnt get their first preference
        for voter_id in unhappy_voters[0].tolist():
            manipulations = manipulations + Bury.possible_combinations(winner,
                                                                       candidates,
                                                                       preferences,
                                                                       voter_id,
                                                                       scheme,
                                                                       happiness,
                                                                       outcome)
        return manipulations

    @staticmethod
    def possible_combinations(winner, candidates, preferences, voter_id, scheme, happiness, original_outcome):
        temp_pref = copy.deepcopy(preferences)
        pref = preferences[:, voter_id]

        # split pref array into two parts, above the winner and below the winner.
        indices = np.where(pref == winner)[0][0]
        before = preferences[:, voter_id][:indices + 1]
        after = preferences[:, voter_id][indices + 1:]

        manipulations = []

        # for each candidate that can be buried
        for c in before:
            idx = np.where(pref == c)[0][0]
            temp_list = np.concatenate((np.delete(before, idx), after))

            # check how many lower positions it can be inserted at
            count = len(pref) - idx - 1
            # starts from last
            index = 0

            while count > 0:
                strategic_pref = np.insert(temp_list, len(pref) - index - 1, c)
                temp_pref[:, voter_id] = strategic_pref
                outcome = scheme.get_scores(temp_pref, candidates)
                new_happiness = Hap.get_scores(outcome, candidates, preferences)[0]

                # if the happiness is not better than the next iterations wont make it any better
                if new_happiness[voter_id] > happiness[voter_id]:
                    manipulation = Mani("Burying",
                                        scheme.get_name(),
                                        voter_id,
                                        pref,
                                        strategic_pref,
                                        happiness[voter_id],
                                        new_happiness[voter_id],
                                        new_happiness,
                                        original_outcome,
                                        outcome
                                        )
                    manipulations.append(manipulation)

                    count -= 1
                    index += 1
                    continue
                else:
                    break
        return manipulations
