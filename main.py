import RPi.GPIO as GPIO
import time

from mic import MIC
from pwm import PWM


def main():
    while True:
        if Mic.get_vad():
            doa = Mic.get_doa()
            print(doa)
            if -180 <= doa <= -10:
                Motor.turn_right(80)
            elif 10 <= doa <= 180:
                Motor.turn_left(80)
            if 10 <= abs(doa) <= 50:
                time.sleep(0.1)
            elif 50 < abs(doa) <= 90:
                time.sleep(0.2)
            elif 90 < abs(doa) <= 180:
                time.sleep(0.3)
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
