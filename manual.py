import asyncio
import RPi.GPIO as GPIO
from sshkeyboard import listen_keyboard

from pwm import PWM


async def press(key):
    if key == "w":
        Motor.straight(100)
        await asyncio.sleep(0.5)
    elif key == "s":
        Motor.back(100)
        await asyncio.sleep(0.3)
    elif key == "a":
        Motor.turn_left(80)
        await asyncio.sleep(0.1)
    elif key == "d":
        Motor.turn_right(80)
        await asyncio.sleep(0.1)
    Motor.stop()


if __name__ == "__main__":
    try:
        Motor = PWM()
        listen_keyboard(on_press=press)
    except KeyboardInterrupt:
        print("プログラムを終了します。")
    except Exception as e:
        print(e)
    finally:
        del Motor
        GPIO.cleanup()
