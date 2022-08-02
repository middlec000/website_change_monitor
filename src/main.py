# Source: https://www.geeksforgeeks.org/python-script-to-monitor-website-changes/
import time
import hashlib
from urllib.request import urlopen, Request

url_list = ["http://www.supersaas.com/schedule/wspvs/Bellingham_VIN_Calendar",
            "http://www.supersaas.com/schedule/wspvs/Marysville_VIN_Calendar"]

