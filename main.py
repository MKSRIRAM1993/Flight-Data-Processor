from typing import List, Dict

class FlightDataProcessor():
    
    def __init__(self) -> None:
        self.flights: List[Dict]= []
    
    def add_flight(self,data:Dict) -> None:
        self.flights.append(data)

    def remove_flight(self,flight_number:str) -> None:
            self.flights = [f for f in self.flights if f["flight_number"] != flight_number]

    def flight_by_status(self,status:str) -> List[Dict]:
        res = []
        for i in self.flights:
            if i["status"] == status:
                res.append(i)
        return res
    
    def get_longest_flight(self)-> Dict:
        maxdur = 0
        for i in self.flights:
            if i["duration_minutes"] > maxdur:
                maxdur = i["duration_minutes"]
                maxflightindex = i.copy()
        return maxflightindex
        
    def __sizeof__(self) -> int:
        return len(self.flights)
        pass


# fm = FlightDataProcessor()

# data = [
#     {"flight_number":"1", "departure_time":"","arrival_time":"","duration_minutes":4,"status":"ON_TIME"},
#     {"flight_number":"2", "departure_time":"","arrival_time":"","duration_minutes":6,"status":"DELAYED"},
#     {"flight_number":"3", "departure_time":"","arrival_time":"","duration_minutes":4,"status":"ON_TIME"},
#     {"flight_number":"4", "departure_time":"","arrival_time":"","duration_minutes":3,"status":"CANCELLED"},
#     {"flight_number":"5", "departure_time":"","arrival_time":"","duration_minutes":5,"status":"DELAYED"},
#     {"flight_number":"6", "departure_time":"","arrival_time":"","duration_minutes":7,"status":"CANCELLED"},
# ]

# for i in data:
#     fm.add_flight(i)

# print(fm.get_longest_flight())
# print(fm.flight_by_status("DELAYED"))
