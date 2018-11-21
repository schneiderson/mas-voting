import pickle
from random import shuffle
from Candidate import Candidate as Can
import copy

candidates = []
preferences = []

for i in range(10):
    candidates.append(Can(str(i)))

with open('candidates.pck', 'wb') as candidates_file:
    pickle.dump(candidates, candidates_file)

print("Candidates: ")
print(candidates)
print("Preferences: ")

for i in range(10):
    shuffle(candidates)
    temp_pref = copy.deepcopy(candidates)
    print(temp_pref)
    preferences.append(temp_pref)

with open('preferences.pck', 'wb') as pref_file:
    pickle.dump(preferences, pref_file)
