from flask import Flask, render_template, request, send_from_directory
import json
import RPi.GPIO as GPIO
import time
import mic
import pwm


app = Flask(__name__)
mic = mic.MIC()
Motor = pwm.PWM()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/control", methods=["POST"])
def control():
    speed = 50

    if direction == "Straight":
        Motor.straight(speed)

    elif direction == "Back":
        Motor.back(speed)

    elif direction == "Stop":
        # ここにモータの命令を追加
        Motor.stop()

    elif direction == "Turn_Left":
        Motor.turn_left(speed)

    elif direction == "Turn_Right":
        Motor.turn_right(speed)

    return "OK"


if __name__ == "__main__":
    try:
        # app.run(debug=True, host = "0.0.0.0", port=8000)
        app.run(debug=False, host="0.0.0.0", port=8000)
    except Exception as e:
        print(e)
        del Servo
        del Motor
