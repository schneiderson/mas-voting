from Candidate import Candidate as Can
from votingSchemes.PluralityVote import PluralityVote as PL
from votingSchemes.Burda import Burda as BU
from votingSchemes.AntiPlurality import AntiPlurality as AP
from votingSchemes.VotingForTwo import VotingForTwo as VT
from HappinessScore import HappinessScore as Hap
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
        [b, a, d, e, c],
        [e, d, b, c, a],
        [b, d, e, c, a]
    ]).T

    outcome = VT.get_scores(preferences, candidates)

    print(Hap.get_scores(outcome, candidates, preferences))


if __name__ == '__main__':
    main()
