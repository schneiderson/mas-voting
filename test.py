from Candidate import Candidate as Can
from votingSchemes.PluralityVote import PluralityVote as PL
from votingSchemes.Burda import Burda as BU
from votingSchemes.AntiPlurality import AntiPlurality as AP
from votingSchemes.VotingForTwo import VotingForTwo as VT
from HappinessScore import HappinessScore as Hap
from tacticalVoting.BulletVoting import BulletVoting as BV
from tacticalVoting.Compromising import Compromising as Com
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
        [a, e, c, d, b],
        [a, c, b, d, e],
        [c, b, d, e, a],
        [b, d, c, e, a],
        [d, a, b, c, e]
    ]).T

    outcome = BU.get_scores(preferences, candidates)

    happiness, happiness_sum = Hap.get_scores(outcome, candidates, preferences)

    outcome = BU.get_scores(preferences, candidates)
    happiness = Hap.get_scores(outcome, candidates, preferences)
    Com.get_scores(preferences, candidates, PL)


if __name__ == '__main__':
    main()
