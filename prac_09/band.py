""""""


class Band():
    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        return f"{self.name} ({','.join([str(member) for member in self.members])})"

    def add(self, member):
        self.members.append(member)

    def play(self):
        return "\n".join([member.play() for member in self.members])
