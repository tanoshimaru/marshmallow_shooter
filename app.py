from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from mic import MIC
from pwm import PWM


app = Flask(__name__)
Mic = MIC()
Motor = PWM()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/control", methods=["POST"])
def control():
    straight_pressed = request.form["straight"] == "true"
    back_pressed = request.form["back"] == "true"
    left_pressed = request.form["left"] == "true"
    right_pressed = request.form["right"] == "true"

    if straight_pressed:
        Motor.straight(100)

    elif back_pressed:
        Motor.back(100)

    elif left_pressed:
        Motor.turn_left(80)

    elif right_pressed:
        Motor.turn_right(80)

    else:
        Motor.stop()

    return "OK"


if __name__ == "__main__":
    try:
        app.run(debug=True, host="0.0.0.0", port=8000)
    except Exception as e:
        print(e)
        del Mic
        del Motor
