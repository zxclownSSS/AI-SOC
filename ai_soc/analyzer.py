import ollama
import json

from ai_soc.prompts import SYSTEM_PROMPT
from ai_soc.security_rules import calculate_severity
from ai_soc.recommendation_rules import get_recommendations
from ai_soc.incident_mapper import normalize_incident_type

def analyze_alert(alert_data):

    severity = calculate_severity(alert_data)

    response = ollama.chat(
        model='qwen2.5:7b',
        messages=[
            {
                'role': 'system',
                'content': SYSTEM_PROMPT
            },
            {
                'role': 'user',
                'content': f'''
Severity already determined by SOC engine:
{severity.upper()}

Do not recalculate severity.

Focus on:
- attack analysis
- IOC extraction
- incident summary

Return ONLY valid JSON.

Alert:
{json.dumps(alert_data, indent=2)}
'''
            }
        ]
    )

    raw_response = response['message']['content']

    parsed = json.loads(raw_response)
    normalized_incident = normalize_incident_type(
    parsed["incident_type"]
    )

    parsed["normalized_incident_type"] = normalized_incident

    parsed["severity"] = severity


    parsed["recommendations"] = get_recommendations(
        normalized_incident
    )

    return parsed