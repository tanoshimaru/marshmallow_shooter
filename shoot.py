import RPi.GPIO as GPIO
from sshkeyboard import listen_keyboard

from servo import SERVO


def press(key):
    if key == "space":
        print("Marshmallow-Shoot!")
        Servo.servo_ctrl(0)
        exit()


if __name__ == "__main__":
    Servo = SERVO()
    try:
        listen_keyboard(on_press=press)
    except Exception as e:
        print(e)
    finally:
        del Servo
        GPIO.cleanup()
