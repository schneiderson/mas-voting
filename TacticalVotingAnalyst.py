from VotingMachine import VotingMachine as VoMa
from Candidate import Candidate as Can
import numpy
import pickle


def main():
    # -------------------------------------------------
    # ------ Candidate and Preference Creation --------
    # -------------------------------------------------

    manual_input = False

    if manual_input:
        # candidates
        a = Can('A')
        b = Can('B')
        c = Can('C')
        d = Can('D')
        e = Can('E')
        candidates = [a, b, c, d, e]

        # create preference matrix
        preferences = numpy.array([
            [a, e, c, d, b],
            [a, c, b, d, e],
            [c, b, d, e, a],
            [b, d, c, e, a],
            [b, d, c, e, a],
            [d, a, b, c, e]
        ]).T

    else:
        # load candidates and preferences from file
        with open('data/candidates.pck', 'rb') as pref_file:
            candidates = pickle.load(pref_file)

        with open('data/preferences_prob.pck', 'rb') as pref_file:
            preferences = numpy.array(pickle.load(pref_file)).T

    # ------------------------------------------------
    # ------ Run voting and get manipulations --------
    # ------------------------------------------------

    # create voting machine instance
    voting_machine = VoMa(preferences, candidates)
    # get manipulations from voting machine
    manipulations = voting_machine.get_manipulations()

    # ---------------------------
    # ------ OUTPUT CODE --------
    # ---------------------------

    # get number of voters and candidates
    num_voters = preferences.shape[1]
    num_candidates = preferences.shape[0]
    mani_per_vs = {}
    mani_happ_per_vs = {}

    debug_flag = True               # will print debug output if set to true
    manipulation_output = False     # will print list of manipulations if set to true

    if debug_flag:
        print("Original Preferences")
        print(preferences.T)
        print("Original Outcome")
        for _, vs in enumerate(voting_machine.outcomes):
            print(str(vs) + ': ' + str(voting_machine.outcomes[vs]))
        print("Original happiness")
        print(voting_machine.happinesses)
        print("-------")
        print("Original happiness sum")
        for _, vs in enumerate(voting_machine.happinesses.keys()):
            print(vs)
            print(sum(voting_machine.happinesses[vs]))

        if manipulation_output:
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
            mani_happ_per_vs[m.voting_scheme] += sum(m.strategic_overall_happiness)
        else:
            mani_per_vs[m.voting_scheme] = 1
            mani_happ_per_vs[m.voting_scheme] = sum(m.strategic_overall_happiness)

    num_all_mani = len(manipulations)

    # Print the results
    print("Manipulations overall: \n{}".format(num_all_mani))

    for mani, key in enumerate(mani_per_vs.keys()):
        print("------------")
        print(key)
        print("manipulations: {}".format(mani_per_vs[key]))
        print("score: {}".format(mani_per_vs[key] / num_voters))
        print("avg. happiness after manipulation:")
        print(mani_happ_per_vs[key] / mani_per_vs[key])


if __name__ == '__main__':
    main()
