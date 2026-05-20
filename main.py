import json

from analyzer import analyze_alert
from incident_renderer import render_incident

with open("alerts/bruteforce.json", "r") as f:
    alert = json.load(f)

incident = analyze_alert(alert)

human_output = render_incident(incident)

print(human_output)