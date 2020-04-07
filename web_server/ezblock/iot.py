from urllib import request
from urllib import parse
from urllib.request import urlopen
import json

class IOT(object):
    headers = {'Content-Type': 'application/json'}      # Header

    url = "https://www.ezblock.sunfounder.com/api/web/v1/"  # API Url
    def __init__(self, iot_token, device):
        self.iot_token = iot_token
        self.device = device

    def _upload(self, url, data):
        url = self.url+url
        _data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, _data)
        response = urlopen(req)
        result = response.read().decode()
        result = json.loads(result)
        if result["status"] == True:
            return result["value"]
        else:
            print("error")

    def post(self, sensorname, value):
        data = {
            "iotToken": self.iot_token,
            "deviceId": self.device,
            "sensorname": sensorname,
            "value": value,
        }
        return self._upload("iots/info", data)

    def get(self, sensorname):
        data = {
            "iotToken": self.iot_token,
            "deviceId": self.device,
            "sensorname": sensorname,
        }
        value = self._upload("iots/iotget", data)
        try:
            value = int(value)
        except:
            pass
        return value
