import RPi.GPIO as GPIO
import time

from mic import MIC
from pwm import PWM


def main():
    speed = 80
    while True:
        if Mic.get_vad():
            doa = Mic.get_doa()
            print(doa)
            if 10 <= doa <= 180:
                Motor.turn_left(speed)
            elif 180 < doa <= 350:
                Motor.turn_right(speed)
            else:
                Motor.stop()
            time.sleep(0.1)
        Motor.stop()
        time.sleep(0.3)


if __name__ == "__main__":
    Motor = PWM()
    Mic = MIC()
    try:
        main()
    except Exception as e:
        print(e)
    finally:
        del Motor
        del Mic
        GPIO.cleanup()
