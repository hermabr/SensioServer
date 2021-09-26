import os
import re
import socket
import traceback

from SensioServer.Light import Light
from SensioServer.Lights import Lights
from SensioServer import save_lights

lights = {}


def update_lights(lights, name, value_id, set_id):
    if value_id not in lights:
        lights[value_id] = {
            "name": f"{name}-{len(lights)}",
            "val": value_id,
            "set": set_id,
        }
    elif set_id:
        lights[value_id]["set"] = set_id


def print_table(lights, row_names):
    os.system("clear")
    longest_items = [len(str(len(lights))) + 2] + [len(name) + 2 for name in row_names]
    for row in lights.values():
        for i, item in enumerate(row.values()):
            longest_items[i + 1] = max(longest_items[i + 1], len(item))

    format_row = "".join(["{:>" + str(length + 2) + "}" for length in longest_items])

    print(format_row.format("", *row_names))
    for i, row in enumerate(lights.values()):
        print(format_row.format(i, *row.values()))


def client_receive(s):
    set_id = ""

    while True:
        try:
            data = s.recv(1024)

            informations = re.findall(b"\x01(.*?)\x02", data)

            if informations:
                info_str = str(informations[0])
                long_name = info_str.split()[2]
                nicer_name = long_name[4:-4]

                action_id = info_str.split()[1]

                if "_SET" in info_str:
                    set_id = action_id
                elif "_Val" in info_str:
                    print(action_id)
                    update_lights(lights, nicer_name, action_id, set_id)
                    set_id = ""

                print_table(lights, ["Name", "Val", "Set"])

        except KeyboardInterrupt:
            if not any([light["set"] for light in lights.values()]):
                os.system("clear")
                input("You have not collected add the set ids. Press enter to continue")
            elif input("Do you want to write and quit? (Y/n) ").lower() in ["y", ""]:
                lights_object = Lights()
                for light in lights.values():
                    light = Light(light["val"], light["set"], light["name"])

                    lights_object.add_light(light)
                save_lights(lights_object)
                break

            print_table(lights, ["Name", "Val", "Set"])
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            print(f"Exception crash at client receive {e}")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.4", 10023))

    client_receive(s)

    s.close()


if __name__ == "__main__":
    main()
