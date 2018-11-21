import numpy as np
from HappinessScore import HappinessScore as Hap
from tacticalVoting.Manipulation import Manipulation as Mani


class BulletVoting(object):
    debug_output = False

    @classmethod
    def get_voting(cls, outcome, candidates, preferences, happiness, voting_scheme):
        (m, n) = preferences.shape

        # get indices of dissatisfied voters
        indices_dissat = np.argwhere(happiness < m-1).flatten()

        # Debug output
        if cls.debug_output:
            print("\nOutcome")
            print(outcome)
            print("\nPreferences")
            print(preferences)
            print()

        manipulations = []

        # for each voter check if bullet voting increases happiness
        for voter in indices_dissat:
            prefs = preferences.copy()
            bullet_prefs = np.array([preferences[:, voter][0]] * m)

            # set everything to 0 except first position
            bullet_prefs[1:] = 0

            # insert bullet preferences in preference matrix
            prefs[:, voter] = bullet_prefs

            # get new score
            new_score = voting_scheme.get_scores(prefs, candidates)

            # calculate new happiness
            (new_happiness, new_happiness_sum) = Hap.get_scores(new_score, candidates, preferences)

            if cls.debug_output:
                print("Voter: {}".format(voter))
                print("Old happiness: {}".format(happiness[voter]))
                print("New happiness: {}".format(new_happiness[voter]))

            if new_happiness[voter] > happiness[voter]:
                manipulation = Mani("BulletVoting",
                                    voting_scheme.get_name(),
                                    voter,
                                    preferences,
                                    prefs[:, voter],
                                    happiness[voter],
                                    new_happiness[voter],
                                    new_happiness,
                                    outcome,
                                    new_score
                                    )
                manipulations.append(manipulation)

        return manipulations

