from Preference import Preference as Pref
from Candidate import Candidate as Can
from votingSchemes.PluralityVote import PluralityVote as PL
from votingSchemes.Burda import Burda as BU
import numpy


def main():
    # candidates
    a = Can('a')
    b = Can('b')
    c = Can('c')
    d = Can('d')
    e = Can('e')

    preferences = numpy.array([[a, b, c, d, e], [b, a, d, e, c], [e, d, b, c, a], [b, d, e, c, a]])

    #print(pref)
    #print(PL.get_score(prefs))
    #print(BU.get_score(prefs))


if __name__ == '__main__':
    main()