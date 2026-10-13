class Room:
    def __init__(self, room_no, room_type, status="Vacant"):
        self.room_no = room_no
        self.room_type = room_type
        self.status = status

    def book_room(self):
        if self.status == "Vacant":
            self.status = "Booked"
            return True
        else:
            return False

    def vacate_room(self):
        if self.status == "Booked":
            self.status = "Vacant"
            return True
        else:
            return False

    def get_room_info(self):
        return {
            "room_no": self.room_no,
            "room_type": self.room_type,
            "status": self.status
        }   