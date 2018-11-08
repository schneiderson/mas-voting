from votingSchemes.PluralityVote import PluralityVote as PL
from votingSchemes.Burda import Burda as BU
from votingSchemes.AntiPlurality import AntiPlurality as AP
from votingSchemes.VotingForTwo import VotingForTwo as VT
import numpy as np
from HappinessScore import HappinessScore as Hap


class Bury(object):
    def __init__(self, outcome, scheme, candidates, preferences):
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
            temp_pref = preferences
            alternative_prefs = self.alter_pref(self.preferences[:, voter_id])

            for pref in alternative_prefs:
                temp_pref[:, voter_id] = pref
                outcome = self.get_outcome(temp_pref)
                new_happiness = self.get_new_happiness(outcome, voter_id)

                if new_happiness > self.happiness[0][voter_id]:
                    temp_dict = {
                        "pref": temp_pref,
                        "happiness": new_happiness
                    }

                    if possible_strategies.get(voter_id):
                        possible_strategies[voter_id] = possible_strategies[voter_id].append(temp_dict)
                    else:
                        possible_strategies[voter_id] = [temp_dict]
        return possible_strategies

    def alter_pref(self, pref):
        indices = np.where(pref == self.winner)
        pref = np.append(pref, pref[indices])
        pref = np.delete(pref, indices)

        return [pref]

    def get_outcome(self, preferences):
        if self.scheme == "BU":
            return self.get_borda(preferences)

        if self.scheme == "AP":
            return self.get_anti_plurality(preferences)

        if self.scheme == "VT":
            return self.get_voting_for_two(preferences)

        if self.scheme == "PL":
            return self.get_plurality(preferences)

        return self.get_borda(preferences)

    def get_borda(self, preferences):
        return BU.get_scores(preferences, self.candidates)

    def get_plurality(self, preferences):
        return PL.get_scores(preferences, self.candidates)

    def get_voting_for_two(self, preferences):
        return VT.get_scores(preferences, self.candidates)

    def get_anti_plurality(self, preferences):
        return AP.get_scores(preferences, self.candidates)

    def get_new_winner(self, temp_pref):
        return self.candidates[np.argsort(BU.get_scores(temp_pref, self.candidates))[-1]]

    def get_new_happiness(self, outcome, voter_id):
        return Hap.get_scores(outcome, self.candidates, self.preferences)[0][voter_id]
