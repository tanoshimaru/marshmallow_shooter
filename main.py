from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import mic
import pwm
import time


app = Flask(__name__)
Mic = mic.MIC()
Motor = pwm.PWM()


def main():
    speed = 50
    
    while True:
        dao = Mic.get_dao()
        if 0 < dao:
            Motor.turn_left(speed)

        elif Mic.is_right():
            Motor.turn_right(speed)

        else:
            Motor.stop()
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        del Mic
        del Motor
