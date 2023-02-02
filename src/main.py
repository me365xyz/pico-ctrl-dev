from wlan import RunWlan
from AP import RunAP
from secrets import secrets

ssid = secrets['ssid']

if ssid == "":
    RunAP()
else:
    RunWlan()
