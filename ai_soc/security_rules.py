def calculate_severity(alert):

    rule_level = alert.get("rule", {}).get("level", 0)

    description = alert.get(
        "rule",
        {}
    ).get(
        "description",
        ""
    ).lower()

    if "authentication failures" in description:
        return "high"

    if "brute force" in description:
        return "high"

    if rule_level >= 12:
        return "critical"

    if rule_level >= 8:
        return "high"

    if rule_level >= 5:
        return "medium"

    return "low"