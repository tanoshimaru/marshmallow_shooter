# marshmallow_shooter

## Setup
1. sudo apt update
2. python -m venv .venv
3. source .venv/bin/activate
4. pip install pyusb click
5. sudo $(which python) dfu.py --download 6_channels_firmware.bin
6. sudo $(which python) DOA.py
