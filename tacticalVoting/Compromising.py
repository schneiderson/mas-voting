import numpy as np
from HappinessScore import HappinessScore as Hap
from votingSchemes.Burda import Burda as BU


class Compromising:
    @staticmethod
    def get_scores(outcome, candidates, preferences, happiness):
        happy = happiness[0]
        winner = max(happy)
        location = np.where(np.array([(winner != y).astype(int) for y in happy]) == 1)
        index = [(winner == y).astype(int) for y in happy].index(1)
        can = preferences.T[index][0]
        preferences = preferences.T
        newPref = [0] * len(preferences)
        hapScore = [0] * len(preferences)
        outcomeList = [0] * len(preferences)
        changed = [0] * len(location)
        betterScore = False

        for x in location[0]:
            newPref[x] = preferences[0].tolist()
            winner_index = (preferences[x].tolist()).index(can)
            first_pref = preferences[x][0]
            hapScore[x] = Hap.get_scores(outcome, candidates, preferences.T)[0][x]
            outcomeList[x] = outcome
            for i in range(1, winner_index):
                if i == winner_index:
                    continue
                preferences[x][0] = preferences[x][i]
                preferences[x][i] = first_pref
                new_outcome = BU.get_scores(preferences.T, candidates)
                prefTemp = preferences[x].tolist()

                preferences[x][i] = preferences[x][0]
                preferences[x][0] = first_pref
                newHappyness = Hap.get_scores(new_outcome, candidates, preferences.T)

                if newHappyness[0][x] > hapScore[x]:
                    changed = changed + location[0][x]
                    hapScore[x] = newHappyness[0][x]
                    newPref[x] = prefTemp
                    outcomeList[x] = new_outcome
                    betterScore = True


        if betterScore:
            for x in changed:
                print("Voter", x+1, "has a happyness score of", hapScore[x], "and uses the preference", newPref[x], "the new results are", outcomeList[x])



        return 0