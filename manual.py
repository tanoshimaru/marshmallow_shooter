import RPi.GPIO as GPIO
import keyboard
import time
from mic import MIC
from pwm import PWM


Mic = MIC()
Motor = PWM()


def control():
    if keyboard.is_pressed("w"):
        print("Pressed W and Straight")
        Motor.straight(100)
    elif keyboard.is_pressed("s"):
        print("Pressed S and Back")
        Motor.back(100)
    elif keyboard.is_pressed("a"):
        print("Pressed A and Left")
        Motor.turn_left(80)
    elif keyboard.is_pressed("d"):
        print("Pressed D and Right")
        Motor.turn_right(80)
    else:
        Motor.stop()
    time.sleep(0.1)


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
