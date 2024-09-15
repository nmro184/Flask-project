from flask import Flask, request, jsonify , render_template 
import requests
from db import query
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1281700732474622063/OWX8E6-hcBZ_RwhWHmoYsqvDrqAzxhY7wE7BZDnagEwAyKtsl0RUENabGtpKmmFgDHC_'
app = Flask(__name__)

    
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message') 

    if message:
        print(f"Message received: {message}")  
        return spread()

@app.route('/send_to_discord_and_db', methods=['POST'])
def spread():
    data = request.get_json()
    message = data.get('message')
    
    if message:
        query('INSERT INTO messages (message, created_at) VALUES (?, CURRENT_TIMESTAMP)', (message,))
        discord_data = {
            "content": message  
        }
        requests.post(DISCORD_WEBHOOK_URL, json=discord_data)
        return jsonify({"status": "success", "receivedMessage": message}), 200
    else:
        return jsonify({"status": "error", "message": "No message provided"}), 400

@app.route('/get_recent_messages', methods=['GET'])
def get_recent_messages():
    query_result = query('SELECT message, created_at FROM messages WHERE created_at >= datetime("now", "-30 minutes")')
    
    if query_result:
        messages = [{"message": row[0], "created_at": row[1]} for row in query_result]
        return  messages
    else:
        return jsonify({"status": "error", "message": "No recent messages"}), 404