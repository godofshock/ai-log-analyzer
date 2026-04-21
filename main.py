from analyzer.analyzer import parse_logs
from model.model import train, predict

data = parse_logs()

train(data)

results = predict(data)

for i, res in enumerate(results):
    if res == -1:
        print(f"[ALERT] Anomaly detected at index {i}")
