from Candidate import Candidate as Can
from votingSchemes.PluralityVote import PluralityVote as PL
from votingSchemes.Burda import Burda as BU
from votingSchemes.AntiPlurality import AntiPlurality as AP
from votingSchemes.VotingForTwo import VotingForTwo as VT
from HappinessScore import HappinessScore as Hap
from tacticalVoting.BulletVoting import BulletVoting as BV

import numpy

def main():
    # candidates
    a = Can('A')
    b = Can('B')
    c = Can('C')
    d = Can('D')
    e = Can('E')
    candidates = [a, b, c, d, e]
    preferences = numpy.array([
        [a, b, c, d, e],
        [a, b, c, d, e],
        [b, a, d, e, c],
        [d, a, b, e, c],
        [d, a, b, e, c],
        [d, a, b, e, c],
        [e, d, b, c, a],
        [e, d, b, c, a],
        [e, d, b, c, a],
        [b, d, e, c, a]
    ]).T

    outcome = BU.get_scores(preferences, candidates)

    happiness, happiness_sum = Hap.get_scores(outcome, candidates, preferences)


    bla = BV.get_voting(outcome, candidates, preferences, happiness, BU)


if __name__ == '__main__':
    main()
