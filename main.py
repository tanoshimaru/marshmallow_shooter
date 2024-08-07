import asyncio
import RPi.GPIO as GPIO
from mic import MIC
from pwm import PWM


def main():
    speed = 50
    while True:
        try:
            if Mic.get_vad():
                doa = Mic.get_doa()
                print(doa)
                if 5 <= doa <= 180:
                    Motor.turn_right(speed)
                elif 180 < doa <= 355:
                    Motor.turn_left(speed)
                else:
                    Motor.stop()
        except KeyboardInterrupt:
            break


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
