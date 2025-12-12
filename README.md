Math Adventures — AI-Powered Adaptive Learning Prototype

A minimal adaptive learning system that dynamically adjusts math problem difficulty based on the learner’s real-time performance. Designed for children aged 5–10, this prototype demonstrates how AI can personalize learning using simple rule-based logic.



🚀 Features

✔ Three difficulty levels — Easy, Medium, Hard

✔ Automatically adjusts difficulty based on performance

✔ Tracks correctness, response time, and difficulty trends

✔ End-of-session performance summary

✔ Fully modular design (Puzzle Generator, Tracker, Adaptive Engine)

✔ Simple command-line interface (no heavy UI needed)

🧩 Project Structure

math-adaptive-prototype/
├─ README.md
├─ requirements.txt
└─ src/
   ├─ main.py
   ├─ puzzle_generator.py
   ├─ tracker.py
   └─ adaptive_engine.py
   How It Works

1️⃣ Puzzle Generator

Generates math problems based on difficulty:

Easy → small addition/subtraction

Medium → larger numbers + multiplication

Hard → multiplication & clean division


2️⃣ Performance Tracker

Records:

Correct/incorrect

User answer

Correct answer

Time taken

Difficulty


Computes:

Accuracy

Average response time

Recent performance (last 3 questions)


3️⃣ Adaptive Engine

Implements rule-based difficulty shifting:

Increase difficulty
If recent accuracy ≥ 80% and average time < 7s

Decrease difficulty
If accuracy ≤ 50% or time > 15s

Otherwise
Maintain same difficulty


Also recommends the next starting level after the session.
▶️ Running the Project

Step 1: Navigate to the src folder

cd src

Step 2: Run the main program

python main.py

Step 3: Follow the CLI instructions

Enter your name

Choose starting difficulty

Solve math puzzles

View performance summary


📊 End-of-Session Summary Includes

Total questions attempted

Correct vs incorrect

Accuracy (%)

Average response time

Difficulty transition breakdown

Recommended next difficulty level


🧠 Why Rule-Based Adaptation?

Simple and explainable

No dataset required

Ideal for early-stage prototypes

Easy to tune
🔮 Future Enhancements

ML-based difficulty prediction

Personalized learner profiles

Skill-based analysis (addition vs multiplication)

A Streamlit web UI

Gamification (rewards, streaks, levels)


📄 Technical Note

A separate 2-page technical explanation includes:

Architecture diagram

Adaptive logic breakdown

Key metrics tracked

Design rationale


🤝 Contributions

This is a learning-focused prototype.
Feel free to open issues or contribute improvements!

🧑‍💻 Author
Ragul(Ragul3008)
