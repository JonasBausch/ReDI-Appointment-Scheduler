class Condition:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Condition):
            return NotImplemented

        return self.name == other.name