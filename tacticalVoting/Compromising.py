import numpy as np
from HappinessScore import HappinessScore as Hap

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
        hapScore = [0] * preferences.shape[0]
        outcomeList = [0] * preferences.shape[0]

        changed = []
        betterScore = False
        riskcount = 0

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
                print(preferences[x])
                preferences[x][i] = preferences[x][0]
                preferences[x][0] = first_pref
                newHappyness = Hap.get_scores(new_outcome, candidates, preferences.T)
                print(score, "original:",preferences[x], newHappyness[0][x], outcome, new_outcome)
                if newHappyness[0][x] > score:
                    riskcount = riskcount + 1
                    print(x, " location")
                    changed = changed + [x]
                    hapScore[x] = newHappyness[0][x]
                    score = newHappyness[0][x]
                    newPref[x] = prefTemp
                    outcomeList[x] = new_outcome
                    betterScore = True

        if betterScore:
            for x in changed:
                #print(riskcount/len(preferences))
                print("Voter", x+1, "has a happyness score of", hapScore[x], "and uses the preference", newPref[x], "the new results are", outcomeList[x])



        return 0