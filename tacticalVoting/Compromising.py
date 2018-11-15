import numpy as np
from HappinessScore import HappinessScore as Hap
from tacticalVoting.Manipulation import Manipulation as Mani


class Compromising:
    @staticmethod
    def get_voting(outcome, candidates, preferences, happiness, voting_scheme):
        (m, n) = preferences.shape
        # get winner
        winner = candidates[np.argmax(outcome)]

        # get indices of dissatisfied voters
        # (exclude candidates for which winner is on personal pref. spot 1 or 2
        #  --> in those cases compromising isn't possible)
        indices_dissat = np.argwhere(happiness < m-2).flatten()

        # preferences
        preferences = preferences.T
        manipulations = []

        # loop over remaining dissatisfied voters and check if compromising leads to higher happiness
        for voter in indices_dissat:
            winner_index = (preferences[voter].tolist()).index(winner)
            first_pref = preferences[voter][0]

            for i in range(1, winner_index):
                new_preferences = preferences.copy()
                new_preferences[voter][0] = preferences[voter][i]
                new_preferences[voter][i] = first_pref
                new_outcome = voting_scheme.get_scores(new_preferences.T, candidates)

                (newHappiness, _) = Hap.get_scores(new_outcome, candidates, new_preferences.T)

                if newHappiness[voter] > happiness[voter]:

                    manipulation = Mani("Compromising",
                                        voting_scheme.get_name(),
                                        voter,
                                        preferences,
                                        new_preferences,
                                        happiness[voter],
                                        newHappiness[voter],
                                        outcome,
                                        new_outcome
                                        )
                    manipulations.append(manipulation)

        return manipulations
