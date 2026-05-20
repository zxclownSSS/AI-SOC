import json

from ai_soc.analyzer import analyze_alert
from ai_soc.incident_renderer import render_incident

with open("alerts/bruteforce.json", "r") as f:
    alert = json.load(f)

incident = analyze_alert(alert)

human_output = render_incident(incident)

print(human_output)