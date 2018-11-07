"""
Preference class
"""


class Preference(object):

    def __init__(self, preference_list):
        self.preferenceList = preference_list

    def get_preferences(self):
        return self.preferenceList

    def get_reverse_preferences(self):
        return self.preferenceList[::-1]

    def insert_by_id(self, index, obj):
        self.preferenceList.insert(index, obj)

    def insert_after(self, obj):
        for i, e in enumerate(self.preferenceList):
            if obj == e:
                self.preferenceList.insert(i + 1, obj)
                break

    def insert_before(self, obj):
        for i, e in enumerate(self.preferenceList):
            if obj == e:
                self.preferenceList.insert(i, obj)
                break
