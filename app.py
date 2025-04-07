from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = [
        {"symbol": "XAUUSD", "bid": 2312.45, "ask": 2312.95},
        {"symbol": "EURUSD", "bid": 1.0835, "ask": 1.0838},
        {"symbol": "USDJPY", "bid": 151.28, "ask": 151.32},
        {"symbol": "GBPUSD", "bid": 1.2640, "ask": 1.2644},
        {"symbol": "USDCHF", "bid": 0.9021, "ask": 0.9025},
        {"symbol": "USDCAD", "bid": 1.3540, "ask": 1.3544},
        {"symbol": "NZDUSD", "bid": 0.6045, "ask": 0.6048},
    ]
    return jsonify({"success": True, "quotes": quotes})

@app.route('/predict', methods=['POST'])
def predict_signal():
    data = request.get_json()
    symbol = data.get("symbol", "XAUUSD")
    timeframe = data.get("timeframe", "1m")

    prediction = random.choice(["Buy", "Sell", "Hold"])
    stop_loss = round(random.uniform(0.1, 0.5), 2)
    take_profit = round(random.uniform(0.5, 1.5), 2)

    return jsonify({
        "success": True,
        "symbol": symbol,
        "timeframe": timeframe,
        "prediction": prediction,
        "stop_loss": stop_loss,
        "take_profit": take_profit
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
