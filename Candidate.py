"""
Very simple candidate class
"""


class Candidate(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):

        return isinstance(other, Candidate) and self.name == other.name
