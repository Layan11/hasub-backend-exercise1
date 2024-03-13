
class Assert:
    def __init__(self, val):
        self.val = val

    def equal_to(self, compare_value):
        return self.val == compare_value

    def greater_than(self, compare_value):
        return self.val > compare_value

    def less_than(self, compare_value):
        return self.val < compare_value

    def in_list(self, list):
        if self.val in list:
            return True
        return False

    def key_in_dict(self, dict):
        for k in dict.keys():
            if k == self.val:
                return True
        return False

    def val_in_dict(self, dict):
        for v in dict.values():
            if v == self.val:
                return True
        return False
