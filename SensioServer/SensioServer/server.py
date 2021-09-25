from SensioServer import init_lights, save_lights

import socket
import re
import atexit
import threading
import time
import os

from flask import Flask, request

app = Flask(__name__)


def exit_handler():
    print("EXITED!")
    save_lights(lights)
    s.close()


def client_receive():
    while True:
        try:
            data = s.recv(1024)

            informations = re.findall(b"\x01(.*?)\x02", data)

            informations = [x for x in informations if "_Val" in str(x)]

            for info_byte_str in informations:
                info_str = info_byte_str.decode("utf-8")
                lights.update_light(info_str.split()[1], info_str.split()[6])

        except Exception as e:
            print(f"Exception crash at client receive {e}")


def client_send():
    while True:
        group_name = input("Group name: ")
        new_value = input("New value: ")
        lights.set_light(group_name, new_value, s)


@app.route("/get")
def get_light():
    group_name = request.args.get("group_name")
    if group_name is None:
        return "Could not get parameter group name", 400
    return {"value": lights.get_value(group_name)}, 200


@app.route("/getall")
def get_all_lights():
    return {"lights": lights.get_json()}, 200


@app.route("/getnames")
def get_names():
    return {"names": lights.get_all_names()}, 200


@app.route("/set")
def set_light():
    group_name = request.args.get("group_name")
    value = request.args.get("value")
    if group_name is None or value is None:
        return f"Could not get parameter group name {group_name} or value {value}", 400

    try:
        lights.set_light(group_name, value, s)
    except Exception as e:
        print("Error with setting light:", e)
        os._exit(1)
    # print("THIS IS NOT IMPLEMENTED!!")

    return {
        "status": "Success"
    }, 200  # f"THIS IS NOT IMPLEMENTED!! Setting light value for {group_name} to {value}"


def run():
    print("================= STARTING CLIENT =================\n")
    global s
    global lights

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.0.4", 10023))

    lights = init_lights()

    atexit.register(exit_handler)

    receive_thread = threading.Thread(target=client_receive)
    receive_thread.start()

    threading.Thread(target=app.run, kwargs=dict(host="0.0.0.0", port=6913)).start()


def start_flask_server():
    print(s)
    print("STARTING FLASK!")
    app.run(debug=True)


def run_flask():
    global lights
    lights = init_lights()
    app.run(debug=True)


if __name__ == "__main__":
    run()
