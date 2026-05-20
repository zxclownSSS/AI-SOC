def normalize_incident_type(incident_type):

    incident_type = incident_type.lower()

    mappings = {

        "ssh authentication failure":
            "ssh_bruteforce",

        "ssh authentication failures":
            "ssh_bruteforce",

        "brute force attack":
            "ssh_bruteforce",

        "ssh brute force":
            "ssh_bruteforce"
    }

    return mappings.get(
        incident_type,
        "unknown_incident"
    )