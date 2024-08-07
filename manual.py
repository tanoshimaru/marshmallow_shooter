import RPi.GPIO as GPIO
import keyboard
from mic import MIC
from pwm import PWM


Mic = MIC()
Motor = PWM()


def control():
    if keyboard.is_pressed("w"):
        Motor.straight(100)
    elif keyboard.is_pressed("s"):
        Motor.back(100)
    elif keyboard.is_pressed("a"):
        Motor.turn_left(80)
    elif keyboard.is_pressed("d"):
        Motor.turn_right(80)
    else:
        Motor.stop()
    return "OK"


if __name__ == "__main__":
    try:
        while True:
            control()
    except KeyboardInterrupt:
        print("プログラムを終了します。")
    except Exception as e:
        print(e)
    finally:
        del Mic
        del Motor
        GPIO.cleanup()
