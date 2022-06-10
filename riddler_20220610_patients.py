""" Explore probablilities of hospital rooms occupancy based on a fixed patient influx."""

class Patient():
    """ A simple clas representing a patient."""
    def __init__(self, num_days_needed):
        self.num_days_needed = num_days_needed
        self.days_left = num_days_needed

class Room():
    """ A simple class representing a room in the hospital."""
    def __init__(self, patient):
        self.patient = patient

class Hospital():
    """ A simple class representing the hospital."""
    def __init__(self):
        self.rooms = []
        self.day = 0

    def _new_patients(self):
        """ Introduce 7 new patients in the hospital with durations in range 1-7."""
        for i in range(1,8):
            room_found = False
            for room in self.rooms:
                if not room.patient:
                    # print("Found an empty room.")
                    room.patient = Patient(i)
                    room_found = True
                    break
            if not room_found:
                self.rooms.append(Room(Patient(i)))

    def new_day(self):
        """ Discharge, then admit patients."""
        for room in self.rooms:
            assert room.patient
            room.patient.days_left -= 1
            if not room.patient.days_left:
                room.patient = None
        print(self)
        self._new_patients()
        self.day += 1

    def __str__(self):
        return_str = f"Day {self.day} Total Rooms: {len(self.rooms)}:"
        for room in self.rooms:
            if not room.patient:
                return_str += " EMPTY"
            else:
                return_str += f" {room.patient.days_left}/{room.patient.num_days_needed}"
        return return_str

    def print_room_allocation(self):
        """ Show how many patients have 1 day left, 2 days left, etc."""
        rooms_cnt = [0,0,0,0,0,0,0]
        for room in self.rooms:
            rooms_cnt[room.patient.days_left-1] += 1
        print(rooms_cnt)

# Main code: Instantiate a hospital and simulate.
DAYS_TO_SIMULATE=20
my_hospital = Hospital()

print(my_hospital)
for day in range(DAYS_TO_SIMULATE):
    my_hospital.new_day()
    print(my_hospital)
my_hospital.print_room_allocation()
