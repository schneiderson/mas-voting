from votingSchemes.AbstractScheme import AbstractScheme


class Burda(AbstractScheme):

    @staticmethod
    def get_score(preferences):
        m = len(preferences[0].get_preferences())
        score = {}
        for i, pref in enumerate(preferences):
            for j, c in enumerate(pref.get_preferences()):
                if c in score:
                    score[c] += m-j
                else:
                    score[c] = m-j

        return score
