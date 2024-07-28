from tuning import Tuning
import usb.core
import usb.util
import time


class MIC():
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.mic_tuning = Tuning(self.dev)

    def get_doa(self):
        return self.mic_tuning.direction


if __name__ == "__main__":
    mic = MIC()
    while True:
        print(mic.get_doa())
        time.sleep(1)
