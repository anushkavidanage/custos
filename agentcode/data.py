# data.py

# ============================================================
# USER DATABASE
# ============================================================
USER_DATABASE = {

    "U001": {
        "name": "Alex",
        "email": "alex@example.com",
        "postcode": "6000",
        "age": 42
    }
}


# ============================================================
# CALENDAR DATABASE
# ============================================================

CALENDAR_DATABASE = {

    "U001": {

        "2026-08-26": [
            "10:00",
            "14:00"
        ],

        "2026-08-27": [
            "09:00",
            "15:00"
        ],

        "2026-08-28": [
            "11:00"
        ]
    }
}

# ============================================================
# HEALTH DATABASE
#
# This represents sensitive user information.
# ============================================================

HEALTH_DATABASE = {

    "U001": {
        "diagnosis": "Anxiety disorder",
        "medications": ["Medication A"],

        "treatment_history": [
            "Psychological therapy",
            "Clinical consultation"
        ],

        "risk_assessment": "Moderate"
    }
}

# ============================================================
# SERVICE DATABASE
# ============================================================

SERVICE_DATABASE = [

    {
        "service_id": "S001",
        "name": "City Health Clinic",
        "location": "Perth",
        "speciality": "General Mental Health",
        "price": 180,
        "available": True
    },

    {
        "service_id": "S002",
        "name": "Community Psychology Centre",
        "location": "Perth",
        "speciality": "Psychology",
        "price": 150,
        "available": True
    },

    {
        "service_id": "S003",
        "name": "North Medical Centre",
        "location": "Perth",
        "speciality": "General Practice",
        "price": 120,
        "available": True
    }
]

# ============================================================
# BOOKING DATABASE
# ============================================================
BOOKINGS = []