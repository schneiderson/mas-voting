from Preference import Preference as Pref
from Candidate import Candidate as Can
from votingSchemes.PluralityVote import PluralityVote as PL
from votingSchemes.Burda import Burda as BU
import numpy


def get_matrix(prefs):
    candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    output = []

    for row in prefs.T.tolist():
        temp = []
        for index, _ in enumerate(row):
            temp.append(row.index(Can(candidates[index])) + 1)
        output.append(temp)
    return numpy.array(output).T


def main():
    # candidates
    a = Can('A')
    b = Can('B')
    c = Can('C')
    d = Can('D')
    e = Can('E')

    preferences = numpy.array([
        [a, b, c, d, e],
        [b, a, d, e, c],
        [e, d, b, c, a],
        [b, d, e, c, a]
    ]).T
    print(get_matrix(preferences))


if __name__ == '__main__':
    main()
