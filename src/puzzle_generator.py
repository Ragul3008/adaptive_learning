import random
from typing import Tuple


DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]


class PuzzleGenerator:
    def __init__(self):
        pass

    def generate(self, difficulty: str) -> Tuple[str, float]:
        """
        Returns:
            question (str): e.g. "3 + 5 = ?"
            answer (float): the correct numeric answer
        """
        if difficulty == "Easy":
            return self._easy_puzzle()
        elif difficulty == "Medium":
            return self._medium_puzzle()
        elif difficulty == "Hard":
            return self._hard_puzzle()
        else:
            # Fallback
            return self._easy_puzzle()

    def _easy_puzzle(self) -> Tuple[str, float]:
        # small addition / subtraction 0–10
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        op = random.choice(["+", "-"])
        if op == "+":
            ans = a + b
        else:
            ans = a - b
        question = f"{a} {op} {b} = ?"
        return question, ans

    def _medium_puzzle(self) -> Tuple[str, float]:
        # slightly bigger numbers, addition / subtraction / small multiplication
        op = random.choice(["+", "-", "*"])
        if op in ["+", "-"]:
            a = random.randint(10, 50)
            b = random.randint(1, 30)
            ans = a + b if op == "+" else a - b
        else:
            # multiplication up to 10x10
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            ans = a * b
        question = f"{a} {op} {b} = ?"
        return question, ans

    def _hard_puzzle(self) -> Tuple[str, float]:
        # multiplication and simple division
        op = random.choice(["*", "/"])
        if op == "*":
            a = random.randint(5, 12)
            b = random.randint(5, 12)
            ans = a * b
        else:
            # create divisible division problems
            b = random.randint(2, 12)
            ans = random.randint(2, 12)
            a = b * ans
        question = f"{a} {op} {b} = ?"
        return question, float(ans)