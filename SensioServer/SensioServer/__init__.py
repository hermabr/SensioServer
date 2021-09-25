from SensioServer.Lights import Lights
from SensioServer.Light import Light
import jsonpickle


def init_lights():
    with open("SensioServer/Data/lights.json", "r") as lights_file:
        lights = jsonpickle.decode(lights_file.read())  # pickle.load(lights_file)

    return lights


def save_lights(lights, path="SensioServer/Data/lights.json"):
    with open(path, "w") as lights_file:
        json_object = jsonpickle.encode(lights)
        lights_file.write(json_object)
    print("Successfully saved light object")
