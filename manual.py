import asyncio
import requests
import RPi.GPIO as GPIO
from sshkeyboard import listen_keyboard

from mic import MIC
from pwm import PWM
from servo import SERVO


url = "http://raspberrypi:3000/lightup"

async def press(key):
    if key == "w":
        Motor.straight(100)
        await asyncio.sleep(0.5)
    elif key == "s":
        Motor.back(100)
        await asyncio.sleep(0.3)
    elif key == "a":
        Motor.turn_left(80)
        await asyncio.sleep(0.3)
    elif key == "d":
        Motor.turn_right(80)
        await asyncio.sleep(0.1)
    elif key == "space":
        print("Marshmallow-Shoot!")
        Servo.servo_ctrl(0)
        try:
            response = requests.get(url)
            response.raise_for_status()
            print("Response:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error:", e)
    Motor.stop()


if __name__ == "__main__":
    Motor = PWM()
    Mic = MIC()
    Servo = SERVO()
    try:
        listen_keyboard(on_press=press)
    except Exception as e:
        print(e)
    finally:
        del Motor
        del Mic
        del Servo
        GPIO.cleanup()
