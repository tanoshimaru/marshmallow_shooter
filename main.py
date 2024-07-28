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
        try:
            if mic.get_vad():
                dao = Mic.get_dao()
                print(dao)
                if 10 < dao <= 180:
                    Motor.turn_right(speed)
                    print("turn right")
                elif 180 < dao < 350:
                    Motor.turn_left(speed)
                    print("turn left")
                else:
                    Motor.stop()
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        del Mic
        del Motor
