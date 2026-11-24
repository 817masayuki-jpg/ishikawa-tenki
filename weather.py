import os
import urllib.request
import json
from datetime import datetime, timedelta, timezone

# 日本時間にする設定
JST = timezone(timedelta(hours=+9), 'JST')
now = datetime.now(JST).strftime('%Y年%m月%d日 %H時%M分')

# 石川県（金沢）の天気を取りに行く
API_KEY = os.environ['WEATHER_API_KEY']
URL = f'https://api.openweathermap.org/data/2.5/weather?lat=36.5613&lon=136.6562&appid={API_KEY}&units=metric&lang=ja'

with urllib.request.urlopen(URL) as response:
    data = json.loads(response.read().decode('utf-8'))
    tenki = data['weather'][0]['description']
    kion = data['main']['temp']
    
    print("===============================")
    print(f"📅 日時：{now}")
    print(f"🌤️ 石川県の天気：{tenki}")
    print(f"🌡️ 今の気温：{kion}度")
    print("===============================")
