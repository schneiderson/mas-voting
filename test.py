from VotingMachine import VotingMachine as VoMa
from Candidate import Candidate as Can
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
        [b, d, c, e, a],
        [d, a, b, c, e]
    ]).T

    voting_machine = VoMa(preferences, candidates)
    manipulations = voting_machine.get_manipulations()

    for m in manipulations:
        print(m.strategy + ": " + m.voting_scheme + ", Voter " + str(m.voter))


if __name__ == '__main__':
    main()
