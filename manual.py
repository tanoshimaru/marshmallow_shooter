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
        cmd = "straight"
    elif key == "s":
        cmd = "back"
    elif key == "a":
        cmd = "left"
    elif key == "d":
        cmd = "right"
    return cmd


def release(key):
    print(f"'{key}' released")
    cmd = "stop"
    return cmd


listen_keyboard(
    on_press=press,
    on_release=release,
)

def control():
    cmd = listen_keyboard(
        on_press=press,
        on_release=release,
    )
    if cmd:
        Motor.straight(100)
    elif cmd:
        Motor.back(100)
    elif cmd:
        Motor.turn_left(80)
    elif cmd:
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
