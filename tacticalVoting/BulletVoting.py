import numpy as np
from HappinessScore import HappinessScore as Hap
from tacticalVoting.Manipulation import Manipulation as Mani


class BulletVoting(object):
    @staticmethod
    def get_voting(outcome, candidates, preferences, happiness, voting_scheme):
        (m, n) = preferences.shape

        # get indices of satisfied voters
        indices_sat = np.argwhere(happiness == m-1).flatten()
        # get indices of dissatisfied voters
        indices_dissat = np.setdiff1d(np.array(range(0, n)), indices_sat)

        # Debug output TODO: remove...
        print("\nOutcome")
        print(outcome)
        print("\nPreferences")
        print(preferences)
        print()

        manipulations = []

        for voter in indices_dissat:
            prefs = preferences.copy()
            bullet_prefs = np.array([preferences[:, voter][0]] * m)

            # set everything to 0 except first position
            bullet_prefs[1:] = 0

            prefs[:, voter] = bullet_prefs

            # get new score
            new_score = voting_scheme.get_scores(prefs, candidates)

            # calculate new happiness
            (new_happiness, new_happiness_sum) = Hap.get_scores(new_score, candidates, preferences)

            print("Voter: {}".format(voter))
            print("Old happiness: {}".format(happiness[voter]))
            print("New happiness: {}".format(new_happiness[voter]))

            if new_happiness[voter] > happiness[voter]:
                print("WARNING: Identified potential for bulletVoting for voter {}".format(voter))

                manipulation = Mani("BulletVoting",
                                    voting_scheme.get_name(),
                                    voter,
                                    preferences[voter],
                                    prefs[voter],
                                    happiness[voter],
                                    new_happiness[voter],
                                    outcome,
                                    new_score
                                    )
                manipulations.append(manipulation)

        return manipulations

