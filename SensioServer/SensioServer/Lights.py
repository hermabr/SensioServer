from SensioServer.Light import Light


class Lights(object):
    """docstring for Lights"""

    def __init__(self):
        print("Warning: Did not initialize lights from the pickle object")
        #  print(
        #      "[ERROR] Initialized the light object?? This should not happen, since it should be built from pickle."
        #  )

        self._lights = []

        #  lights_list = [{"gid": "Wc1etgEntre-0-34","friendly": "Wc1etg","short_val": "41236","short_set": "41284"},{"gid": "EntreEntre-0-28","friendly": "Entre","short_val": "57187","short_set": "57235"},{"gid": "VaskeromVaskerom-0-24","friendly": "Vaskerom","short_val": "49291","short_set": "49339"},{"gid": "Kjokken1Kj\u00f8kken-0-21","friendly": "Kjokken1","short_val": "45290","short_set": "45338"},{"gid": "Kj\u00f8kkenKj\u00f8kken-0-22","friendly": "Kj\u00f8kken","short_val": "47975","short_set": "48023"},{"gid": "Kj\u00f8kkenskapKj\u00f8kken-0-23","friendly": "Kj\u00f8kkenskap","short_val": "55871","short_set": "55919"},{"gid": "StueStue-0-26","friendly": "Stue","short_val": "54555","short_set": "54603"},{"gid": "StueStue-0-25","friendly": "Stue","short_val": "58503","short_set": "58551"},{"gid": "TaktrappTrapp-0-30","friendly": "Taktrapp","short_val": "50607","short_set": "50655"},{"gid": "TrappveggTrapp-0-29","friendly": "Trappvegg","short_val": "53239","short_set": "53287"},{"gid": "Bad kjellerBad kjeller-0-38","friendly": "Bad kjeller","short_val": "37182","short_set": "37230"},{"gid": "TrimromTrimrom-0-32","friendly": "Trimrom","short_val": "43974","short_set": "44022"},{"gid": "KjellerstueKjellerstue-0-27","friendly": "Kjellerstue","short_val": "51923","short_set": "51971"},{"gid": "ArthurArthur-0-39","friendly": "Arthur","short_val": "33128","short_set": "33176"},{"gid": "HermannHerman-0-40","friendly": "Hermann","short_val": "34497","short_set": "34545"},{"gid": "SovLauritzLauritz-0-33","friendly": "SovLauritz","short_val": "42605","short_set": "42653"},{"gid": "M.badlysHovedsov-0-36","friendly": "M.badlys","short_val": "39867","short_set": "39915"},{"gid": "MastersovHovedsov-0-31","friendly": "Mastersov","short_val": "46659","short_set": "46707"},{"gid": "Utelys inngangUtelys-0-35","friendly": "Utelys inngang","short_val": "38498","short_set": "38546"}]
        #
        #  for light_dict in lights_list:
        #      light_object = Light(light_dict['friendly'], light_dict['short_val'], light_dict['short_set'], light_dict['gid'])
        #      self.add_light(light_object)

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
