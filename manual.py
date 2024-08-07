import RPi.GPIO as GPIO
import time
from sshkeyboard import listen_keyboard

from mic import MIC
from pwm import PWM


Mic = MIC()
Motor = PWM()

straight_pressed = False
back_pressed = False
left_pressed = False
right_pressed = False

def press(key):
    print(f"'{key}' pressed")
    if key == "w":
        straight_pressed = True
    elif key == "s":
        back_pressed = True
    elif key == "a":
        left_pressed = True
    elif key == "d":
        right_pressed = True


def release(key):
    print(f"'{key}' released")
    if key == "w":
        straight_pressed = False
    elif key == "s":
        back_pressed = False
    elif key == "a":
        left_pressed = False
    elif key == "d":
        right_pressed = False


listen_keyboard(
    on_press=press,
    on_release=release,
)

def control():
    if straight_pressed:
        Motor.straight(100)
    elif back_pressed:
        print("Pressed S and Back")
        Motor.back(100)
    elif left_pressed:
        print("Pressed A and Left")
        Motor.turn_left(80)
    elif right_pressed:
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
