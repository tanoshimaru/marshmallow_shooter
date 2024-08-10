import time
from tuning import Tuning
import usb.core
import usb.util


class MIC():
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
        self.mic_tuning = Tuning(self.dev)

    def get_doa(self):
        doa = self.mic_tuning.direction
        if 180 <= doa < 360:
            doa = doa - 360
        return doa

    def get_vad(self):
        time.sleep(0.3)
        return self.mic_tuning.is_voice()

    def __del__(self):
        usb.util.dispose_resources(self.dev)


if __name__ == "__main__":
    mic = MIC()
    while True:
        try:
            if mic.get_vad():
                print(mic.get_doa())
        except KeyboardInterrupt:
            break
