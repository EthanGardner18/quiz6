# In this project there are a few different inheritances. DataStorage, Display, ActivityManage, Activity. These abstract methods have subclasses
# that use SOLID by making the code more high level. Not much more code is needed to add differnent activites or other functions to the fitness tracker

from abc import ABC, abstractmethod
from typing import List, Tuple

# these classes store the data and then write it to file
class DataStorage(ABC):
    @abstractmethod
    def save_data(self, data: dict):
        pass

class FileStorage(DataStorage):
    def save_data(self, data: dict):
        with open("activity_data.txt", "a") as file:
            file.write(str(data) + "\n")

# this is responsible for the display
class Display(ABC):
    @abstractmethod
    def update(self, data: dict):
        pass

class ConsoleDisplay(Display):
    def update(self, data: dict):                     
        print("New activity data received:")
        print(data)

# this class is how the code actually works, collects and stores the data and then can load it
class ActivityMonitor:
    def __init__(self, data_storage: DataStorage, displays: List[Display]):
        self.data_storage = data_storage
        self.displays = displays

    def collect_activity_data(self, activity: str, data: dict):
        self.data_storage.save_data(data)
        self.notify_displays(activity, data)

    def notify_displays(self, activity: str, data: dict):
        for display in self.displays:
            display.update({activity: data})


# This activity class takes the activities as a string and adds them to the database, therefor the other activities are easy to add
# and because step count distance and calorie count are seperate classes they dont have to be initialized
class Activity(ABC):
    @abstractmethod
    def update(self, data: dict):
        print("Updating")
        pass

class StepCount(Activity):
    def update(self, data: dict):
        if "steps" in data:
            print(f"Step Count: {data['steps']}")

class Distance(Activity):
    def update(self, data: dict):
        if "distance" in data:
            print(f"Distance: {data['distance']} km")

class CaloriesBurned(Activity):
    def update(self, data: dict):
        if "calories" in data:
            print(f"Calories Burned: {data['calories']} cal")

def main():
    file_storage = FileStorage()
    console_display = ConsoleDisplay()
    activity_monitor = ActivityMonitor(file_storage, [console_display])

    activity_monitor.collect_activity_data("running", {"steps": 5000, "distance": 5, "calories": 300})
    activity_monitor.collect_activity_data("cycling", {"distance": 10, "calories": 200})

if __name__ == "__main__":
    main()
