from Preference import Preference as Pref
from Candidate import Candidate as Can
from votingSchemes.PluralityVote import PluralityVote as PL
from votingSchemes.Burda import Burda as BU

def main():

    # candidates
    a = Can('a')
    b = Can('b')
    c = Can('c')
    d = Can('d')
    e = Can('e')

    p1 = Pref([a, b, c, d, e])
    p2 = Pref([b, a, d, e, c])
    p3 = Pref([e, d, b, c, a])
    p4 = Pref([b, d, e, c, a])
    prefs = [p1, p2, p3, p4]

    print(prefs)
    print(PL.get_score(prefs))
    print(BU.get_score(prefs))


if __name__ == '__main__':
    main()