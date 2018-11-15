import numpy as np
from HappinessScore import HappinessScore as Hap
from tacticalVoting.Manipulation import Manipulation as Mani


class Compromising:
    @staticmethod
    def get_voting(outcome, candidates, preferences, happiness, voting_scheme):
        (m, n) = preferences.shape
        winner = candidates[np.argmax(outcome)]

        print(winner)

        print(preferences)

        # get indices of dissatisfied voters
        indices_dissat = np.argwhere(happiness < m-2).flatten()

        print(indices_dissat)

        print(winner)

        preferences = preferences.T
        newPref = [0] * preferences.shape[0]
        outcomeList = [0] * preferences.shape[0]
        manipulations = []


        for x in indices_dissat:
            newPref[x] = preferences[0].tolist()
            winner_index = (preferences[x].tolist()).index(winner)
            first_pref = preferences[x][0]
            score = Hap.get_scores(outcome, candidates, preferences.T)[0][x]
            outcomeList[x] = outcome
            print()
            for i in range(1, winner_index):
                if i == winner_index:
                    continue
                preferences[x][0] = preferences[x][i]
                preferences[x][i] = first_pref
                new_outcome = voting_scheme.get_scores(preferences.T, candidates)
                prefTemp = preferences[x].tolist()
                preferences[x][i] = preferences[x][0]
                preferences[x][0] = first_pref
                newHappyness = Hap.get_scores(new_outcome, candidates, preferences.T)
                print(score, newHappyness[0][x])
                if newHappyness[0][x] > score:
                    print("WARNING: Identified potential for bulletVoting for voter {}".format(x))

                    manipulation = Mani("BulletVoting",
                                        voting_scheme.get_name(),
                                        x,
                                        preferences[x],
                                        prefTemp,
                                        score,
                                        newHappyness[0][x],
                                        outcome,
                                        new_outcome
                                        )
                    manipulations.append(manipulation)
                    print(manipulation)


        return 0