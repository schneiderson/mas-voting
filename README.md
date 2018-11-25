# mas-voting
multi agent voting

***

## Instructions
This code was written for python 3.
Please make sure to install the numpy library before running the code.

### Create Preferences
To generate preferences run:
`python GeneratePreferences.py`

You can set the number of candidates and voters in the configuration section of the GeneratePreferences file.
Further, you can also set weather or not a probability distribution is used to create the voter preferences.

### Run the tactical voting analyst
To get the possible manipulations for a certain preference matrix run:
`python TacticalVotingAnalyst.py`

In the head of the TacticalVotingAnalyst.py file you can set weather to load the preference matrix from file or use a manually entered voting matrix.
