import subprocess
import time
from tidevice import Device
from tidevice._wdaproxy import WDAService
from tidevice._usbmux import Usbmux

import sys


def available_devices():

    u = Usbmux().device_udid_list()

    devices = []

    for dev in u:
        device_dict = {}

        device = Device(dev)

        device_dict['devName'] = device.name
        device_dict['UDID'] = device.info.udid
        device_dict['deviceID'] = device.info.device_id
        device_dict['connectionType'] = device.info.conn_type

        devices.append(device_dict)

    return devices


def start_wda_service(udid: str, port: int):

    dev = Device(udid, Usbmux)

    serv = WDAService(dev)
    serv.set_check_interval(1.0)

    cmds = [
        sys.executable, '-m', 'tidevice', '-u', dev.udid, 'relay', str(
            port), '8100'
    ]

    p = subprocess.Popen(cmds, stdout=sys.stdout,
                         stdin=sys.stderr, close_fds=True)

    try:
        serv.start()
        while serv._service.running and p.poll() is None:
            time.sleep(1)
    finally:
        p and p.terminate()
        serv.stop()
