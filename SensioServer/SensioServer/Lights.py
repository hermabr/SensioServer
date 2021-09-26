from SensioServer.Light import Light


class Lights(object):
    """docstring for Lights"""

    def __init__(self):
        print("Warning: Did not initialize lights from the pickle object")

        self._lights = []

    def add_light(self, light):
        self._lights.append(light)

    def get_light(self, group_name):
        for light in self._lights:
            if light.get_group_name() == group_name:
                return light
        print(f"Could not get light {group_name} by set id")
        return None

    def get_value(self, group_name):
        light = self.get_light(group_name)

        if light is None:
            print("BIG ERROR!!")
            return -1 / 2.55

        return light.get_value()

    def _find_light_by_val_id(self, value_id):
        for light in self._lights:
            if light.get_value_id() == value_id:
                return light
        print(f"Could not get light {value_id} by value id")
        return None

    def update_light(self, value_id, value):
        light = self._find_light_by_val_id(value_id)

        if light is None:
            print(f"Could not update light with value {value_id}")

        light.update_value(value)

    def set_light(self, group_name, value, s):
        light = self.get_light(group_name)

        light.set_value(value, s)

    def get_all_lights(self):
        return self._lights

    def get_json(self):
        return [light.get_json() for light in self._lights]

    def get_all_names(self):
        return [light.get_group_name() for light in self._lights]

    def __repr__(self):
        return f"{[light for light in self._lights]}"
