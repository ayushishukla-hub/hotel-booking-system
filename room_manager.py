from data  import ROOM_DATABASE

class RoomManager:
    @staticmethod
    def display_vacant_rooms():
        print("\n---VACANT ROOMS---")
        vacant_found = False
        for r_no, details in ROOM_DATABASE.items():
            if details[1] == "Vacant":
                print(f"Room No: {r_no}, Type: {details[0]}")
                vacant_found = True
        if not vacant_found:
            print("No vacant rooms available.")

    @staticmethod
    def display_booked_rooms():
        print("\n---BOOKED ROOMS---")
        booked_found = False
        for r_no, details in ROOM_DATABASE.items():
            if details[1] == "Booked":
                print(f"Room No: {r_no}, Type: {details[0]}")
                booked_found = True
        if not booked_found:
            print("No rooms are currently booked.")