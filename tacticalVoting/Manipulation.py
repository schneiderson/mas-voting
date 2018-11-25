"""
Class representing a single voter manipulation
"""


class Manipulation(object):
    def __init__(self,
                 strategy="",
                 voting_scheme="",
                 voter=0,
                 original_preference=None,
                 strategic_preference=None,
                 original_voter_happiness=0,
                 strategic_voter_happiness=0,
                 strategic_overall_happiness=None,
                 original_outcome=None,
                 strategic_outcome=None
                 ):
        if strategic_outcome is None:
            strategic_outcome = []
        if original_outcome is None:
            original_outcome = []
        if strategic_overall_happiness is None:
            strategic_overall_happiness = []
        if strategic_preference is None:
            strategic_preference = []
        if original_preference is None:
            original_preference = []

        self.strategy = strategy
        self.voting_scheme = voting_scheme
        self.voter = voter
        self.original_preference = original_preference
        self.strategic_preference = strategic_preference
        self.original_voter_happiness = original_voter_happiness
        self.strategic_voter_happiness = strategic_voter_happiness
        self.strategic_overall_happiness = strategic_overall_happiness
        self.original_outcome = original_outcome
        self.strategic_outcome = strategic_outcome
