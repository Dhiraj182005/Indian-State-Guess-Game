# Indian-State-Guess-Game
A Python Turtle-based interactive geography game where users guess Indian States and Union Territories by name and their positions are marked on the map of India. Includes data logging for missed states.

# 🇮🇳 Indian State Guess Game

A fun and educational Python game built using the Turtle graphics library and Pandas. This game helps players learn the names and locations of Indian States and Union Territories on a map.


## 🧠 Game Objective

Guess all the 28 Indian States and 8 Union Territories by typing their names. Each correct guess marks the state/UT on the map. The game ends when all 36 regions are guessed correctly or the player types `Exit`.

If the player chooses to exit early, a `missing_state.csv` file is generated with the names of the remaining states to help improve learning.

---

## 🛠 Features

- 🗺️ Interactive map of India using Turtle graphics
- 📌 Marks each guessed state at its correct geographical position
- 🧾 Saves a CSV of missed states if player exits early
- 📚 Helps improve geographical knowledge of India

---

## 📂 Project Structure

```bash
indian-state-guess-game/
│
├── map_of_India.gif           # Map of India used in the game
├── states_and_uts.csv         # Dataset containing state names with x, y coordinates
├── missing_state.csv          # (Generated) States not guessed
├── indian_state_guess_game.py # Main game logic
└── README.md                  # Project documentation
