# Pomodoro Timer

A simple **Pomodoro Timer** application built using Python and Tkinter, following the Pomodoro Technique to enhance productivity. This version is refactored using Object-Oriented Programming (OOP) for better structure and maintainability.

## Features
- Work, short break, and long break cycles
- Automatic cycle transitions
- Visual and textual feedback (✔ checkmarks) for completed work sessions
- Reset button to restart the timer

## Technologies Used
- **Python** (3.x)
- **Tkinter** (GUI framework)
- **Math module** (for time calculations)
- **AI to organize**

## Installation
### Prerequisites
Make sure you have Python installed. You can check by running:
```sh
python --version
```

### Clone the Repository
```sh
git clone https://github.com/belluccaz/pomodoro.git
cd pomodoro-timer
```

### Run the Application
```sh
python main.py
```

## Project Structure
```
├── pomodoro.py         # Main Pomodoro Timer logic (OOP)
├── constants.py        # Constants for colors, font, and time settings
├── main.py             # Entry point of the application
├── README.md           # Documentation
├── tomato.png          # Image used for UI
```

## Usage
- Click **Start** to begin the Pomodoro session.
- The timer will automatically transition between work and break periods.
- Click **Reset** to stop and reset the timer.
- A ✔ mark is added after each completed work session.

## Contributing
Feel free to fork this repository and submit pull requests if you'd like to improve the project!

## License
This project is open-source and available under the MIT License.

