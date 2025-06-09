import requests
import time

TOKEN = "7204621900:AAE5P9_i8cw7h7gKSCgPzsDh3A6imGreFrg"
CHAT_ID = "@Ukraine_danger_bot"

EXCLUDED_REGIONS = ["Луганська", "Крим"]

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=data)
    return response.json()

def get_fake_alerts():
    return [
        {"type": "балістика", "region": "Київська", "time": "12:00"},
        {"type": "дрони", "region": "Харківська", "time": "12:05"},
        {"type": "ракети", "region": "Луганська", "time": "12:10"},
    ]

def filter_alerts(alerts):
    return [a for a in alerts if a["region"] not in EXCLUDED_REGIONS]

def format_alert(alert):
    return f"🚨 <b>Тривога!</b>\nТип: {alert['type']}\nОбласть: {alert['region']} до летить\nЧас: {alert['time']}"

def main():
    while True:
        alerts = get_fake_alerts()
        filtered = filter_alerts(alerts)
        for alert in filtered:
            msg = format_alert(alert)
            send_message(msg)
        time.sleep(300)

if __name__ == "__main__":
    main()
