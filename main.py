from flask import Flask
import requests, base64, os
from datetime import datetime

app = Flask(__name__)

def send_log(message):
    try:
        auth = os.environ['OPENOBSERVE_AUTH_KEY']
        response = requests.post(
            f"{os.environ['OPENOBSERVE_URL']}/api/{os.environ['OPENOBSERVE_ORG']}/{os.environ['OPENOBSERVE_STREAM']}/_json",
            json=[{
                "timestamp": datetime.now().isoformat(),
                "message": message,
                "level": "info"
            }],
            headers={
                "Authorization": f"Basic {auth}",
                "Content-Type": "application/json"
            }
        )
        print(f"Log sent. Status: {response.status_code}, Response: {response.text}",flush=True)

    except Exception as e:
        print(f"Log error: {e}",flush=True)

@app.route('/')
def home():
    send_log('Homepage visited')
    return 'Hello from Cloud Run'
    
@app.route('/test-log')
def test_log():
    send_log('Test log from /test-log route')
    return 'Sent test log!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
