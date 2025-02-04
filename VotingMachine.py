from votingSchemes.PluralityVote import PluralityVote as PluVo
from votingSchemes.Borda import Burda as Burda
from votingSchemes.AntiPlurality import AntiPlurality as AntiPluVo
from votingSchemes.VotingForTwo import VotingForTwo as VoFoTwo
from tacticalVoting.BulletVoting import BulletVoting as BuVo
from tacticalVoting.Compromising import Compromising as Com
from tacticalVoting.Bury import Bury as Bury

from HappinessScore import HappinessScore as Hap


class VotingMachine(object):

    voting_schemes = [PluVo, Burda, AntiPluVo, VoFoTwo]
    strategies = [BuVo, Com, Bury]
    outcomes = {}
    happinesses = {}

    def __init__(self, preferences, candidates):
        self.preferences = preferences
        self.candidates = candidates

    def get_manipulations(self):
        manipulations = []

        # get manipulations for each voting scheme
        for _, vs in enumerate(self.voting_schemes):

            outcome = vs.get_scores(self.preferences, self.candidates)
            (happiness, happiness_sum) = Hap.get_scores(outcome, self.candidates, self.preferences)

            # apply each strategy and find manipulations
            for _, strategy in enumerate(self.strategies):

                new_manipulations = strategy.get_voting(outcome, self.candidates, self.preferences, happiness, vs)
                manipulations.extend(new_manipulations)

            self.outcomes[vs.get_name()] = outcome
            self.happinesses[vs.get_name()] = happiness

        return manipulations
