from picarx import PiCarX
import time

car = PiCarX()

actions = list(car.actions.keys())

while True:
    print("\n------ Available actions ------")
    for i, action in enumerate(actions):
        print(f"{i}: {action}")
    text = input("Enter action number: ")
    try:
        action_name = actions[int(text)]
        action = car.actions[action_name]
        print(f"Running action: {action_name}")
        action()
    except Exception as e:
        print(f"Error: {e}")

