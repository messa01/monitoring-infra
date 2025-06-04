
from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
	data = request.get_json()
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	print(f"\n ALERTE RECUE - {timestamp}")
	print("=" * 50)

	for alert in data.get('alerts', []):
		status = alert.get('status', 'unknown')
		alertname = alert.get('labels', {}).get('alertname', 'unknown')
		summary = alert.get('annotations', {}).get('summary', 'no summary')
		description = alert.get('annotations', {}).get('description', 'no description')

		print(f"Status: {status.upper()}")
		print(f" Alert: {alertname}")
		print(f" Summary: {summary}")
		print(f"Description: {description}")
		print("-" * 30)

	return "Alert received", 200

@app.route('/health')
def health():
	return "Webhook server is running!", 200

if __name__=='__main__':
	app.run(host='0.0.0.0', port=9094, debug=True)
