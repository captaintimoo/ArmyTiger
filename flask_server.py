
from flask import Flask, render_template_string, request, jsonify
import pandas as pd
import time
import random

app = Flask(__name__)

# 부대 및 간부 정보 (기본값)
phonebook = {
    "부대 A": [{"name": "김상사", "phone": "010-1111-2222", "duty": True}, {"name": "박중사", "phone": "010-3333-4444", "duty": False}],
    "부대 B": [{"name": "이소위", "phone": "010-5555-6666", "duty": True}],
    "부대 C": [{"name": "최대위", "phone": "010-7777-8888", "duty": False}, {"name": "장소령", "phone": "010-9999-0000", "duty": True}]
}

logs = []

# 실시간 시뮬레이션용 부대 목록
locations = [f"부대 {chr(i)}" for i in range(ord('A'), ord('Z') + 1)]

# HTML 파일 로드
with open("dashboard_editable_phonebook.html", "r", encoding="utf-8") as f:
    html_template = f.read()

@app.route("/")
def index():
    return render_template_string(html_template)

@app.route("/logs")
def get_logs():
    return jsonify(logs[-50:])

@app.route("/phonebook/<unit>")
def get_phonebook(unit):
    return jsonify(phonebook.get(unit, []))

@app.route("/update_phonebook", methods=["POST"])
def update_phonebook():
    data = request.json
    unit = data.get("unit")
    name = data.get("name")
    phone = data.get("phone")
    duty = data.get("duty", False)
    if not unit or not name or not phone:
        return "Invalid input", 400

    if unit not in phonebook:
        phonebook[unit] = []
    for entry in phonebook[unit]:
        if entry["name"] == name:
            entry["phone"] = phone
            entry["duty"] = duty
            break
    else:
        phonebook[unit].append({"name": name, "phone": phone, "duty": duty})

    return "OK", 200

@app.route("/report", methods=["POST"])
def report():
    data = request.json
    unit = data.get("location")
    report = data.get("report")
    reason = data.get("reason")
    for log in reversed(logs):
        if log["location"] == unit and log["prediction"] == 1 and log.get("report") == "":
            log["report"] = report
            log["reason"] = reason
            break
    return "Reported", 200

@app.route("/generate_log")
def generate_log():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    location = random.choice(locations)
    prediction = 1 if random.random() < 0.25 else 0
    logs.append({
        "timestamp": now,
        "location": location,
        "prediction": prediction,
        "report": "",
        "reason": ""
    })
    return "Log Added", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
