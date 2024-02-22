
class vote:
    def __init__(self, id, for_candidate):
        self.id = id
        self.for_candidate = for_candidate


class candidate:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class voter:
    def __init__(self, name, age, addr, vote):
        self.name = name
        self.age = age
        self.addr = addr
        self.vote = vote