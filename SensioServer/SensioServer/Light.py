class Light(object):
    """docstring for Light"""

    def __init__(self, value_id, set_id, group_name):
        self._value = -1
        self._value_id = value_id
        self._set_id = set_id
        self._group_name = group_name

    def update_value(self, value):
        self._value = int(float(value))
        print("Updated", self)

    def set_value(self, value, s):
        s.sendall(
            bytes(
                f"set_value {self.get_value_id()} {int(float(value))}new_state {self.get_set_id()} 0",
                "utf-8",
            )
        )
        print("Set", self, "to", value)

    def get_value(self):
        return self._value

    def get_value_id(self):
        return self._value_id

    def get_set_id(self):
        return self._set_id

    def get_group_name(self):
        return self._group_name

    def nice_short_name(self):
        # return self.get_group_name() + ": " + str(self.get_value())
        return f"<L: {self._value:>3} '{self._group_name}'>"

    def get_json(self):
        return {"group_name": self._group_name, "value": self._value}

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<L: {self._value:>3} '{self._group_name}'>"
