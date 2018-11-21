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

    num_voters = preferences.shape[1]
    num_candidates = preferences.shape[0]

    voting_machine = VoMa(preferences, candidates)
    manipulations = voting_machine.get_manipulations()

    mani_per_vs = {}

    for m in manipulations:
        # print(m.strategy + ": " + m.voting_scheme + ", Voter " + str(m.voter))
        if mani_per_vs.keys().__contains__(m.voting_scheme):
            mani_per_vs[m.voting_scheme] += 1
        else:
            mani_per_vs[m.voting_scheme] = 1


    num_all_mani = len(manipulations)

    print("overall manipulations: {}".format(num_all_mani))
    for mani, test in enumerate(mani_per_vs.keys()):
        print("------------")
        print("manipulations for {}: {}".format(test, mani_per_vs[test]))
        print("score: {}".format(mani_per_vs[test]/num_voters))




if __name__ == '__main__':
    main()
