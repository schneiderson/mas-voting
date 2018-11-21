

class Manipulation(object):
    def __init__(self,
                 strategy="",
                 voting_scheme="",
                 voter=0,
                 original_preference=[],
                 strategic_preference=[],
                 original_voter_happiness=0,
                 strategic_voter_happiness=0,
                 strategic_overall_happiness=[],
                 original_outcome=[],
                 strategic_outcome=[]
                 ):
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
