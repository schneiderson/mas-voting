import pickle
import random
from Candidate import Candidate as Can
import numpy

SIZE_CANDIDATES = 5
SIZE_VOTERS = 100
PROBABILISTIC_DISTRIBUTION = True

candidates = []
preferences = []

for i in range(SIZE_CANDIDATES):
    candidates.append(Can(str(i)))

print("Candidates: ")
print(candidates)
print("Preferences: ")

with open('data/candidates.pck', 'wb') as candidates_file:
    pickle.dump(candidates, candidates_file)

# 4 candidates will have higher chances of being in top choices for voters
sample = random.sample(candidates, 4)
weights = [0.35, 0.25, 0.20, 0.10]

# for selecting other candidates not from the sample
low_probability = (1.0 - sum(weights)) / (len(candidates) - len(weights))

# get an array for probabilistic weights of all the candidates
weights_candidates = [weights[sample.index(x)] if x in sample else low_probability for x in candidates]
file_name = 'preferences.pck'

for i in range(SIZE_VOTERS):
    if PROBABILISTIC_DISTRIBUTION:
        temp_pref = numpy.random.choice(candidates, len(candidates), p=weights_candidates, replace=False)
        file_name = 'preferences_prob.pck'
    else:
        temp_pref = numpy.random.choice(candidates, len(candidates), replace=False)

    preferences.append(temp_pref)
    print(temp_pref)

with open('data/' + file_name, 'wb') as pref_file:
    pickle.dump(preferences, pref_file)
