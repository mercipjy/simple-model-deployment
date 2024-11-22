from flask import Flask, request, jsonify
import pickle

# 1. Flask 앱 생성
app = Flask(__name__)

# 2. 모델 로드
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# 3. 예측 API 생성
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # JSON 데이터 가져오기
    features = data.get("features", [])
    
    if not features:
        return jsonify({"error": "No features provided"}), 400
    
    prediction = model.predict([features])
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
