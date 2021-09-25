import re
import random
import socket

def get_socket_information(all_informations, tag):
    get_informations = [x for x in all_informations if tag in str(x)]

    for info_byte_str in get_informations:
        info_str = info_byte_str.decode("utf-8")
        #  if info_str.split(" ")[0] == "SSN":
        #      set_light(s, value_id, set_id, random.randint(0,100))
        print(info_str)


def client_receive(s):
    value_id = '53239'
    set_id = '53287'

    while True:
        try:
            data = s.recv(1024)

            informations = re.findall(b"\x01(.*?)\x02", data)

            get_socket_information(informations, "_Val")
            get_socket_information(informations, "_SET")
        #  lights.update_light(info_str.split()[1], info_str.split()[6])

        except Exception as e:
            print(f"Exception crash at client receive {e}")

def set_light(s, value_id, set_id, value):
    s.sendall(bytes(f'set_value {value_id} {int(float(value))}new_state {set_id} 0', 'utf-8'))
    print("Light set")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.4", 10023))

    #  set_light(s, value_id, set_id, 0)
    client_receive(s)


if __name__ == "__main__":
    main()
