from typing import Optional, Tuple
from puzzle_generator import DIFFICULTY_LEVELS
from tracker import PerformanceTracker


class AdaptiveEngine:
    def __init__(self, tracker: PerformanceTracker):
        self.tracker = tracker
        self.current_difficulty = "Easy"

    def set_initial_difficulty(self, difficulty: str):
        """Safely set initial difficulty."""
        self.current_difficulty = (
            difficulty if difficulty in DIFFICULTY_LEVELS else "Easy"
        )

    def get_current_difficulty(self) -> str:
        return self.current_difficulty

    def update_difficulty(self):
        """
        Adjust difficulty using recent performance.
        Rules:
        - Increase: accuracy >= 0.8 AND avg time < 7s
        - Decrease: accuracy <= 0.5 OR avg time > 15s
        - Else: no change
        """
        result = self.tracker.recent_performance(n=3)

        # Ensure recent_performance returns correct structure
        if not result or len(result) != 2:
            return

        recent_acc, recent_time = result

        # Avoid None or invalid values
        if recent_acc is None or recent_time is None:
            return

        # Increase difficulty
        if recent_acc >= 0.8 and recent_time < 7:
            self.current_difficulty = self._next_level()

        # Decrease difficulty
        elif recent_acc <= 0.5 or recent_time > 15:
            self.current_difficulty = self._prev_level()

    def _next_level(self) -> str:
        """Move one level up safely."""
        idx = DIFFICULTY_LEVELS.index(self.current_difficulty)
        if idx < len(DIFFICULTY_LEVELS) - 1:
            return DIFFICULTY_LEVELS[idx + 1]
        return self.current_difficulty

    def _prev_level(self) -> str:
        """Move one level down safely."""
        idx = DIFFICULTY_LEVELS.index(self.current_difficulty)
        if idx > 0:
            return DIFFICULTY_LEVELS[idx - 1]
        return self.current_difficulty

    def recommended_next_level(self) -> str:
        """
        Suggest starting difficulty for next session.
        - accuracy > 0.8 → go up
        - accuracy < 0.5 → go down
        - otherwise → stay same
        """
        overall_acc = self.tracker.overall_accuracy()

        # If no accuracy data exists
        if overall_acc is None:
            return self.current_difficulty

        idx = DIFFICULTY_LEVELS.index(self.current_difficulty)

        if overall_acc > 0.8 and idx < len(DIFFICULTY_LEVELS) - 1:
            return DIFFICULTY_LEVELS[idx + 1]

        if overall_acc < 0.5 and idx > 0:
            return DIFFICULTY_LEVELS[idx - 1]

        return self.current_difficulty