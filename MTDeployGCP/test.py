import requests
import json

resp = requests.post("http://127.0.0.1:5000", json={"text": "โครงงานวิศวกรรมนี้เป็นการพัฒนาระบบตรวจจับ"})

print(resp.json())