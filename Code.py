import csv
import os
from datetime import datetime

DATA_FILE = "fitness_data.csv"

def initialize_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Steps", "Calories", "Water(L)", "Workout"])

def log_daily_data():
    date = datetime.now().strftime("%Y-%m-%d")
    steps = input("Enter steps walked: ")
    calories = input("Enter calories consumed: ")
    water = input("Enter water intake (in liters): ")
    workout = input("Workout summary: ")

    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, steps, calories, water, workout])
    
    print("✅ Data logged successfully!")

def view_progress():
    if not os.path.exists(DATA_FILE):
        print("No data found. Start logging first.")
        return
    
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)

        if len(data) == 1:
            print("No entries yet.")
            return
        
        print("\n📊 Progress Summary:")
        for row in data[1:]:
            print(f"Date: {row[0]}, Steps: {row[1]}, Calories: {row[2]}, Water: {row[3]}L, Workout: {row[4]}")

def main_menu():
    initialize_file()
    
    while True:
        print("\n==== Health & Fitness Tracker ====")
        print("1. Log Daily Data")
        print("2. View Progress")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            log_daily_data()
        elif choice == '2':
            view_progress()
        elif choice == '3':
            print("👋 Exiting. Stay healthy!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
