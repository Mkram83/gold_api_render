from flask import Flask, jsonify

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
