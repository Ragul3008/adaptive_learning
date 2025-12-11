from typing import List, Dict
import statistics


class PerformanceTracker:
    def __init__(self):
        # Each record: {
        #   "question": str,
        #   "user_answer": float,
        #   "correct_answer": float,
        #   "correct": bool,
        #   "time_taken": float,
        #   "difficulty": str
        # }
        self.records: List[Dict] = []

    def log_attempt(
        self,
        question: str,
        user_answer: float,
        correct_answer: float,
        correct: bool,
        time_taken: float,
        difficulty: str,
    ):
        self.records.append(
            {
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "correct": correct,
                "time_taken": time_taken,
                "difficulty": difficulty,
            }
        )

    def overall_accuracy(self) -> float:
        if not self.records:
            return 0.0
        correct_count = sum(1 for r in self.records if r["correct"])
        return correct_count / len(self.records)

    def average_time(self) -> float:
        if not self.records:
            return 0.0
        times = [r["time_taken"] for r in self.records]
        return statistics.mean(times)

    def recent_performance(self, n: int = 3):
        """Return accuracy and avg time over last n attempts."""
        if not self.records:
            return 0.0, 0.0
        subset = self.records[-n:]
        acc = sum(1 for r in subset if r["correct"]) / len(subset)
        times = [r["time_taken"] for r in subset]
        avg_time = statistics.mean(times)
        return acc, avg_time

    def summary(self) -> str:
        if not self.records:
            return "No attempts made."

        total = len(self.records)
        correct = sum(1 for r in self.records if r["correct"])
        accuracy_pct = self.overall_accuracy() * 100
        avg_time = self.average_time()

        # Optional: per-difficulty breakdown
        per_diff = {}
        for r in self.records:
            d = r["difficulty"]
            per_diff.setdefault(d, {"total": 0, "correct": 0})
            per_diff[d]["total"] += 1
            if r["correct"]:
                per_diff[d]["correct"] += 1

        lines = []
        lines.append(f"Total questions: {total}")
        lines.append(f"Correct: {correct} ({accuracy_pct:.1f}%)")
        lines.append(f"Average time per question: {avg_time:.2f} seconds")

        lines.append("\nPerformance by difficulty:")
        for d, stats in per_diff.items():
            if stats["total"] == 0:
                continue
            acc = (stats["correct"] / stats["total"]) * 100
            lines.append(f"  - {d}: {stats['correct']}/{stats['total']} ({acc:.1f}%)")

        return "\n".join(lines)