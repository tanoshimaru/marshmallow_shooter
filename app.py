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
    speed = 80
    left_pressed = request.form["left"] == "true"
    right_pressed = request.form["right"] == "true"
    forward_pressed = request.form["forward"] == "true"
    backward_pressed = request.form["backward"] == "true"

    if forward_pressed and backward_pressed:
        Motor.stop()

    elif forward_pressed:
        Motor.forward(speed)

    elif backward_pressed:
        Motor.backward(speed)

    elif left_pressed and right_pressed:
        Motor.straight(speed)

    elif left_pressed:
        Motor.turn_left(speed)

    elif right_pressed:
        Motor.turn_right(speed)

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
