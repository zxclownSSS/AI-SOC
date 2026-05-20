def get_recommendations(incident_type):

    recommendations = {

        "ssh_bruteforce": [
            "Block suspicious IP address",
            "Enable fail2ban",
            "Disable root SSH login",
            "Use SSH key authentication",
            "Review authentication logs"
        ]
    }

    return recommendations.get(
        incident_type,
        ["Investigate incident"]
    )