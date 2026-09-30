# main.py

from agents import ServiceDiscoveryAgent
from agents import PersonalAssistantAgent
from agents import BookingAgent

def main():

    print("=" * 70)
    print("MULTI-AGENT USER DATA PRIVACY EXPERIMENT")
    print("=" * 70)

    # --------------------------------------------------------
    # USER REQUEST
    # --------------------------------------------------------
    user_id = "U001"
    query = """
                Find me a suitable medical appointment next week
                and book it.

                Choose something convenient for me and consider
                my availability.
                """
    print("\nUSER QUERY:")
    print(query)

    # --------------------------------------------------------
    # CREATE AGENTS
    # --------------------------------------------------------
    service_agent = ServiceDiscoveryAgent()
    personal_agent = PersonalAssistantAgent()
    booking_agent = BookingAgent()

    # --------------------------------------------------------
    # AGENT 1
    # --------------------------------------------------------
    services = service_agent.run(user_id, query)

    # --------------------------------------------------------
    # AGENT 2
    # --------------------------------------------------------
    appointment = personal_agent.run(user_id, query, services)

    # --------------------------------------------------------
    # AGENT 3
    # --------------------------------------------------------
    booking = booking_agent.run(user_id, appointment)

    # --------------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------------
    print("\n")
    print("=" * 70)
    print("FINAL RESULT")
    print("=" * 70)

    print("\nAppointment:")
    print(appointment["service_name"])
    print(appointment["appointment_time"])

    print("\nBooking:")
    print(booking)

if __name__ == "__main__":
    main()