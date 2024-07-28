# marshmallow_shooter

## Setup
1. `sudo apt update`
2. `python -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install pyusb click`
5. `source .venv/bin/activate && sudo $(which python) dfu.py --download 6_channels_firmware.bin`
6. `source .venv/bin/activate && sudo $(which python) mic.py`

## Run
Manual: `source .venv/bin/activate && sudo $(which python) app.py`
Auto: `source .venv/bin/activate && sudo $(which python) main.py`

## Tuning
1. `source .venv/bin/activate && $(which python) tuning.py -p`
