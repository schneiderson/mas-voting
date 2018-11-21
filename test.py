from VotingMachine import VotingMachine as VoMa
from Candidate import Candidate as Can
import numpy
import pickle


def main():
    # candidates
    # a = Can('A')
    # b = Can('B')
    # c = Can('C')
    # d = Can('D')
    # e = Can('E')

    with open('candidates.pck', 'rb') as pref_file:
        candidates = pickle.load(pref_file)

    with open('preferences.pck', 'rb') as pref_file:
        preferences = numpy.array(pickle.load(pref_file)).T

    print("Candidates")
    print(candidates)
    print("Preferences")
    print(preferences)

    num_voters = preferences.shape[1]
    num_candidates = preferences.shape[0]
    
    voting_machine = VoMa(preferences, candidates)
    manipulations = voting_machine.get_manipulations()

    mani_per_vs = {}

    debug_flag = True

    if debug_flag:
        print("Original Preferences")
        print(preferences.T)
        print("Original Outcome")
        print(voting_machine.outcomes)
        print("Original happiness")
        print(voting_machine.happinesses)
        print("-------")
        print("Original happiness sum")
        for _, vs in enumerate(voting_machine.happinesses.keys()):
            print(vs)
            print(sum(voting_machine.happinesses[vs]))

        print("\nManipulations:")
        for m in manipulations:
            print("----")
            print(m.strategy + ": " + m.voting_scheme + ", Voter " + str(m.voter))
            print("New voter preference")
            print(m.strategic_preference.T)
            print("New outcome")
            print(m.strategic_outcome)
            print("New Happiness: ")
            print(m.strategic_overall_happiness)
            print("New happiness sum")
            print(sum(m.strategic_overall_happiness))

            print("")


    for m in manipulations:
        if mani_per_vs.keys().__contains__(m.voting_scheme):
            mani_per_vs[m.voting_scheme] += 1
        else:
            mani_per_vs[m.voting_scheme] = 1

    num_all_mani = len(manipulations)


    # Print the results

    print("Manipulations overall: \n{}".format(num_all_mani))

    for mani, key in enumerate(mani_per_vs.keys()):
        print("------------")
        print(key)
        print("manipulations: {}".format(mani_per_vs[key]))
        print("score: {}".format(mani_per_vs[key]/num_voters))




if __name__ == '__main__':
    main()
