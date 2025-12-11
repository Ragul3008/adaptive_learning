import time

from puzzle_generator import PuzzleGenerator, DIFFICULTY_LEVELS
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def get_initial_difficulty() -> str:
    print("Choose starting difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter 1/2/3: ").strip()

    mapping = {"1": "Easy", "2": "Medium", "3": "Hard"}
    return mapping.get(choice, "Easy")


def main():
    print("Welcome to Math Adventures — Adaptive Learning Prototype!")
    user_name = input("Enter your name: ").strip() or "Learner"

    tracker = PerformanceTracker()
    engine = AdaptiveEngine(tracker)
    generator = PuzzleGenerator()

    start_diff = get_initial_difficulty()
    engine.set_initial_difficulty(start_diff)

    print(f"\nHi {user_name}! Starting at {start_diff} level.")
    print("You can type 'q' at any time to end the session.\n")

    num_questions = 10  # or ask user how many they want

    for i in range(1, num_questions + 1):
        current_diff = engine.get_current_difficulty()
        question, correct_answer = generator.generate(current_diff)

        print(f"\nQuestion {i} (Difficulty: {current_diff})")
        print(question)

        start_time = time.perf_counter()
        user_input = input("Your answer: ").strip()
        end_time = time.perf_counter()

        if user_input.lower() == "q":
            print("\nEnding session early.")
            break

        time_taken = end_time - start_time

        try:
            user_answer = float(user_input)
        except ValueError:
            print("Invalid input, counting as incorrect.")
            user_answer = None
            correct = False
        else:
            # Compare with tolerance, in case of division
            correct = abs(user_answer - correct_answer) < 1e-3

        if correct:
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect. The correct answer is {correct_answer}.")

        tracker.log_attempt(
            question=question,
            user_answer=user_answer,
            correct_answer=correct_answer,
            correct=correct,
            time_taken=time_taken,
            difficulty=current_diff,
        )

        # Update difficulty for next question
        engine.update_difficulty()

    # End-of-session summary
    print("\n=== Session Summary ===")
    print(tracker.summary())
    print("\nSuggested starting level next time:",
          engine.recommended_next_level())
    print("\nThanks for playing, keep practicing!")


if __name__ == "__main__":
    main()