def render_incident(incident):

    output = f"""
=== AI SOC ANALYSIS ===

Threat Type:
{incident['incident_type']}

Severity:
{incident['severity'].upper()}

Confidence:
{incident['confidence']}

Summary:
{incident['summary']}

IOC:
"""

    for ioc in incident["iocs"]:

        value = (
            ioc.get("value")
            or ioc.get("ip")
            or ioc.get("domain")
            or "unknown"
        )

        output += f"\n- {value}"

    output += "\n\nRecommended Actions:\n"

    for rec in incident["recommendations"]:

        output += f"\n• {rec}"

    return output