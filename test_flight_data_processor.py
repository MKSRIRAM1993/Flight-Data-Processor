from flight_data_processor import FlightDataProcessor
import unittest

# YYYY-MM-DD HH:MM

class TestFlightDataProcessor(unittest.TestCase):
    def setUp(self):
        self.fm = FlightDataProcessor()
        self.flight1 = {"flight_number":"B394", "departure_time":"2025-03-04 09:23","arrival_time":"2025-03-04 12:23","duration_minutes":4,"status":"ON_TIME"}
        self.flight2 = {"flight_number":"A204", "departure_time":"2025-04-04 09:23","arrival_time":"2025-04-04 19:23","duration_minutes":12,"status":"CANCELLED"}
        self.flight3 = {"flight_number":"B394", "departure_time":"2025-02-04 09:23","arrival_time":"2025-02-04 17:23","duration_minutes":5,"status":"ON_TIME"}
        self.flight4 = {"flight_number":"A204", "departure_time":"2025-04-04 09:23","arrival_time":"2025-04-04 15:23","duration_minutes":1,"status":"DELAYED"}
        self.fm.add_flight(self.flight1)
        self.fm.add_flight(self.flight2)
        self.fm.add_flight(self.flight4)

    def test_add_flight(self):
        self.fm.add_flight(self.flight3)
        self.assertEqual(len(self.fm.flights) , 4)
    
    def test_remove_flight(self):
        self.fm.remove_flight("B394")
        self.assertEqual(len(self.fm.flights) , 2)

    def test_get_longest_flight(self):
        longest = self.fm.get_longest_flight()
        self.assertEqual(longest["flight_number"] , "A204")        

    def test_flight_by_status(self):
        delayed_flights = self.fm.flight_by_status("DELAYED")
        self.assertEqual(len(delayed_flights), 1)
        ontime_flights = self.fm.flight_by_status("ON_TIME")
        self.assertEqual(len(ontime_flights), 1)
        cancelled_flights = self.fm.flight_by_status("CANCELLED")
        self.assertEqual(len(cancelled_flights), 1)

    def test_len(self):
        self.assertEqual(len(self.fm), 3)

if __name__ == "__main__":
    unittest.main()
