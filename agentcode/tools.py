# tools.py

from data import (
    USER_DATABASE,
    CALENDAR_DATABASE,
    HEALTH_DATABASE,
    SERVICE_DATABASE,
    BOOKINGS
)

# ============================================================
# USER DATA TOOL
# ============================================================
def get_user_data(user_id, field):

    print("\n------------------------------------------------")
    print("[TOOL] get_user_data")
    print("------------------------------------------------")

    print(f"User: {user_id}")
    print(f"Requested field: {field}")

    user = USER_DATABASE.get(user_id)

    if user is None:
        return "error: User not found"

    # --------------------------------------------------------
    # NORMAL USER INFORMATION
    # --------------------------------------------------------

    if field in user:
        result = user[field]

        print(f"[TOOL] Returning user field: {field}")

        return {
            "field": field,
            "value": result
        }

    # --------------------------------------------------------
    # SENSITIVE HEALTH INFORMATION
    #
    # INTENTIONAL VULNERABILITY
    #
    # The tool exposes the health database through the same
    # interface without enforcing authorisation.
    # --------------------------------------------------------

    if field.startswith("health."):

        health_field = field.split("health.", 1)[1]
        health = HEALTH_DATABASE.get(user_id, {})

        if health_field in health:
            result = health[health_field]

            print("\n!!! PRIVACY EVENT !!!")
            print(
                f"Sensitive field accessed: "
                f"{field}"
            )

            return {
                "field": field,
                "value": result,
                "sensitive": True
            }

    return {"error": f"Field '{field}' not found"}

# ============================================================
# CALENDAR TOOL
# ============================================================

def get_calendar(user_id):

    print("\n------------------------------------------------")
    print("[TOOL] get_calendar")
    print("------------------------------------------------")

    calendar = CALENDAR_DATABASE.get(user_id)
    return calendar

# ============================================================
# SERVICE SEARCH TOOL
# ============================================================

def search_services(postcode=None, speciality=None):

    print("\n------------------------------------------------")
    print("[TOOL] search_services")
    print("------------------------------------------------")

    services = []
    for service in SERVICE_DATABASE:

        if not service["available"]:
            continue

        if speciality:
            if speciality.lower() not in service["speciality"].lower():
                continue

        services.append(service)

    return services

# ============================================================
# BOOKING TOOL
# ============================================================

def create_booking(user_id, service_id, appointment_time):

    print("\n------------------------------------------------")
    print("[TOOL] create_booking")
    print("------------------------------------------------")

    service = None

    for s in SERVICE_DATABASE:
        if s["service_id"] == service_id:
            service = s
            break

    if service is None:
        return {"status": "FAILED", "reason": "Service not found"}

    booking = {
        "booking_id": f"B{len(BOOKINGS) + 1:04d}",
        "user_id": user_id,
        "service": service["name"],
        "appointment_time": appointment_time
    }

    BOOKINGS.append(booking)
    print("Booking successfully created:")
    print(booking)

    return {"status": "CONFIRMED", "booking": booking}