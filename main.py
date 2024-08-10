import RPi.GPIO as GPIO
import time
import threading
from sshkeyboard import listen_keyboard

from mic import MIC
from pwm import PWM
from servo import SERVO


def motor_control():
    while True:
        if Mic.get_vad():
            doa = Mic.get_doa()
            print(doa)
            if -180 <= doa <= -5:
                Motor.turn_right(80)
            elif 5 <= doa <= 180:
                Motor.turn_left(80)
            if 5 <= abs(doa) <= 50:
                time.sleep(0.1)
            elif 50 < abs(doa) <= 90:
                time.sleep(0.2)
            elif 90 < abs(doa) <= 180:
                time.sleep(0.3)
            Motor.stop()
            time.sleep(0.5)


def press(key):
    if key == "space":
        print("Marshmallow-Shoot!")
        Servo.servo_ctrl(0)


if __name__ == "__main__":
    Motor = PWM()
    Mic = MIC()
    Servo = SERVO()

    motor_thread = threading.Thread(target=motor_control)
    motor_thread.start()

    try:
        listen_keyboard(on_press=press)
    except Exception as e:
        print(e)
    finally:
        motor_thread.join()
        del Motor
        del Mic
        del Servo
        GPIO.cleanup()
