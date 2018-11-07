from votingSchemes.AbstractScheme import AbstractScheme


class PluralityVote(AbstractScheme):

    @staticmethod
    def get_score(preferences):
        score = {}
        for i, pref in enumerate(preferences):
            most_preferred = pref.get_preferences()[0]
            if most_preferred in score:
                score[most_preferred] += 1
            else:
                score[most_preferred] = 1

        return score

