
# It presents a way to access the elements of an object without exposing the underlying presentation.

class RadioStation:
    
    def __init__(self, frequency):
        self.frequency = frequency


class StationList(object):
    
    _stations = list()
    _counter = 0
    
    def __init__(self):
        pass
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._counter > len(self._stations) - 1:
            raise StopIteration
        else:
            self._counter += 1
            return self._stations[self._counter - 1]
    
    def add_station(self, station):
        self._stations.append(station)
    
    def remove_station(self, station):
        to_remove = station.frequency
        stations = [x for x in self._stations if x.frequency != to_remove]

    def count(self):
        return len(self._stations)
    
    def current(self):
        return self._stations[self._counter]
    
    def rewind(self):
        self._counter = 0


station_list = StationList()
station_list.add_station(RadioStation(89))
station_list.add_station(RadioStation(101))
station_list.add_station(RadioStation(102))
station_list.add_station(RadioStation(103.2))

for station in station_list:
    print(station.frequency)
    
station_list.remove_station(RadioStation(89))