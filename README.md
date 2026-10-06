# Number-Guessing-Challenge
"A Python terminal number guessing game where you crack a vault using hints, a heat meter, scan power-ups and a scoring system."
# 🔐 Vault Cracker

A terminal-based number guessing game written in Python. You play a hacker trying to crack a vault by guessing its secret access code before the security system locks you out.

---

## 📋 Table of Contents

- [About the Game](#-about-the-game)
- [Requirements](#-requirements)
- [How to Run](#-how-to-run)
- [Game Rules](#-game-rules)
- [Difficulty Levels](#-difficulty-levels)
- [Hints and Heat Meter](#-hints-and-heat-meter)
- [Scan Power-Up](#-scan-power-up)
- [Scoring System](#-scoring-system)
- [Regulations (Dos and Don'ts)](#-regulations-dos-and-donts)
- [Example Gameplay](#-example-gameplay)
- [Running on Online Compilers](#-running-on-online-compilers)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)

---

## 🎮 About the Game

The computer secretly picks a random access code. Your job is to guess it within a limited number of attempts. After every wrong guess you get:

- a **direction hint** (`too LOW` or `too HIGH`)
- a **heat meter** reading showing how close you are

You can also spend a limited **scan** to reveal an extra clue about the code. You can play as many rounds as you like, and the game tracks your attempts and score.

---

## 🛠 Requirements

- Python **3.6 or higher**
- No external libraries needed (uses only the built-in `random` module)

Check your Python version:

```bash
python --version
```

---

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```

2. Go into the project folder:

   ```bash
   cd <your-repo-name>
   ```

3. Run the game:

   ```bash
   python vault_cracker.py
   ```

   On some systems you may need `python3 vault_cracker.py`.

---

## 📜 Game Rules

1. At the start of every round, choose a **difficulty level** (1, 2 or 3).
2. The computer picks a **secret code** (a whole number) within the range of that level.
3. Enter your guess as a whole number. After each guess the game tells you whether it was too low or too high, and how hot or cold you are.
4. You have a **limited number of attempts**. Every valid guess uses one attempt.
5. If you guess the code, you win the round and earn points.
6. If you run out of attempts, you are **locked out**. The code is revealed and you score 0 for the round.
7. After each round, your stats are displayed and you can choose to play another round (`y`) or quit (`n`).

---

## 🎚 Difficulty Levels

| Level | Name          | Code Range | Attempts | Scans |
|-------|---------------|------------|----------|-------|
| 1     | Rookie Hacker | 1 – 50     | 8        | 2     |
| 2     | Pro Hacker    | 1 – 100    | 7        | 1     |
| 3     | Elite Hacker  | 1 – 500    | 9        | 1     |

---

## 🌡 Hints and Heat Meter

After every wrong guess you see a direction hint plus a heat level. The heat level depends on how far your guess is from the code, as a percentage of the full range:

| Heat Level      | Distance from the code            |
|-----------------|-----------------------------------|
| 🔥 BURNING HOT  | within 2% of the range            |
| 🌶 Hot          | within 5%                         |
| ☀️ Warm         | within 10%                        |
| ❄️ Cold         | within 25%                        |
| 🧊 Freezing     | more than 25% away                |

---

## 📡 Scan Power-Up

Type `scan` instead of a number to use a scan and reveal one clue about the secret code.

- A scan **does not use up an attempt**, but it **costs 150 points** from your round score.
- Each scan gives one random clue, and the same clue is never repeated in a round:
  - whether the code is **even or odd**
  - whether the code is **divisible by 3**
  - the **sum of the digits** of the code
  - whether the code is in the **lower or upper half** of the range
- If you have no scans left, the game tells you and nothing is lost.

---

## 🏆 Scoring System

Each round you win is scored out of **1000 points**:

```
Round score = 1000 - 100 × (extra attempts after the first) - 150 × (scans used)
```

- The minimum round score is **0**.
- A lost round scores **0**.
- Cracking the vault on your **first attempt with no scans** gives the maximum **1000 points**.

After each round the game shows:

- Rounds played
- Vaults cracked (wins)
- Total attempts made
- Total score
- Fewest attempts used in a win

---

## ⚖️ Regulations (Dos and Don'ts)

**Do:**

- ✅ Enter only **whole numbers** as guesses (for example `25`, not `25.5`).
- ✅ Keep your guess **within the range** of the chosen level.
- ✅ Type `scan` (any letter case) to use a scan.
- ✅ Answer `y` to play again or `n` to quit when asked.

**Don't:**

- ❌ Don't enter letters or symbols as guesses. The game will show an "Invalid input" message.
- ❌ Don't guess outside the level's range. You will be asked to try again.
- ❌ Don't expect to use more scans than your level allows.

**Fair play notes:**

- Invalid inputs and out-of-range numbers **do not** use up attempts.
- The secret code is **randomly generated every round**, so it cannot be predicted from earlier rounds.
- Any answer other than `y` at the "play again" prompt ends the game.

---

## 💻 Example Gameplay

```
============================================
  V A U L T   C R A C K E R
  Guess the secret access code before the
  security system locks you out!
============================================

Choose difficulty:
  1. Rookie Hacker  (1-50, 8 attempts, 2 scan(s))
  2. Pro Hacker  (1-100, 7 attempts, 1 scan(s))
  3. Elite Hacker  (1-500, 9 attempts, 1 scan(s))
Level: 1

Level: Rookie Hacker
Code range: 1 to 50 | Attempts: 8 | Scans: 2
Type a number to guess, or 'scan' to use a scan for a clue.

[8 attempt(s) left] Enter code: 25
Access denied. 25 is too LOW. Heat: Warm

[7 attempt(s) left] Enter code: scan
SCAN RESULT: The code is in the UPPER half of the range.  (1 scan(s) left)

[7 attempt(s) left] Enter code: 40
Access denied. 40 is too LOW. Heat: Hot

[6 attempt(s) left] Enter code: 42

ACCESS GRANTED! Vault cracked in 3 attempt(s).
Score for this round: 650
```

---

## 🌐 Running on Online Compilers

Some online compilers have a separate **Input** box. In that case, type all your inputs there, **one per line, in the order the game asks for them**:

1. The level (`1`, `2` or `3`)
2. Your guesses (numbers or `scan`)
3. `y` to play again or `n` to quit

Example input for Rookie level:

```
1
25
10
40
30
```

If the inputs run out, the game exits cleanly with a message. Because the secret code is random, the best experience is running the game in a terminal or IDE where you can type each guess live.

---

## 📁 Project Structure

```
.
├── vault_cracker.py   # The game
└── README.md          # Rules and instructions
```

---

## 🤝 Contributing

Ideas to extend the game:

- Add a high-score file that saves scores between sessions
- Add a timer mode
- Add more scan clue types
- Add a two-player mode

Fork the repository, make your changes and open a pull request.

---

## 📄 License

Add your preferred license here (for example MIT).

Enjoy cracking vaults! 🔓
