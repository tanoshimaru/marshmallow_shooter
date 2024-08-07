import RPi.GPIO as GPIO
import time
from sshkeyboard import listen_keyboard

from mic import MIC
from pwm import PWM


Mic = MIC()
Motor = PWM()


def press(key):
    print(f"'{key}' pressed")
    if key == "w":
        Motor.straight(100)
    elif key == "s":
        Motor.back(100)
    elif key == "a":
        Motor.turn_left(80)
    elif key == "d":
        Motor.turn_right(80)


def release(key):
    print(f"'{key}' released")
    Motor.stop()


if __name__ == "__main__":
    try:
        cmd = listen_keyboard(
            on_press=press,
            on_release=release,
        )
    except KeyboardInterrupt:
        print("プログラムを終了します。")
    except Exception as e:
        print(e)
    finally:
        del Mic
        del Motor
        GPIO.cleanup()
