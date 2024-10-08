"""Module to store and calculate statistics of score."""

from typing import Iterable, Sized

class Scorecard(Iterable, Sized):
    """Accumulate scores and compute their average."""

    def __init__(self):
        """Initialize a new Scorecard."""
        self.scores: list[float] = []

    def __len__(self):
        return len(self.scores)

    def __iter__(self):
        return iter(self.scores)

    def add_score(self, score: float):
        """Add a score to the Scorecard."""
        self.scores.append(score)

    def average(self) -> float:
        """Return the average of all scores, 0 if no scores."""
        return sum(self.scores)/max(1,len(self.scores))



def print_scores(score_card: Scorecard):
    """Print statistics for the scorecard and the actual scores."""
    print(f"Scorecard contains {len(score_card)} scores.")
    print(f"Min score: {min(score_card)}  Max score: {max(score_card)}.")
    for score in score_card:
        print(score)


def ordinal(num: int) -> str:
    """Return the ordinal value of an integer; works for numbers up to 20.

    For examples: ordinal(1) is '1st', ordinal(2) is '2nd'.
    """
    suffixes: dict[int,str] = {1: "st", 2: "nd", 3: "rd"}
    return str(num) + suffixes.get(num, "th")


if __name__ == "__main__":
    # Interactively add scores and print some statistics.
    scorecard = Scorecard()

    print("Input 3 scores.")
    for count in range(1,4):
        score = float(input(f"input {ordinal(count)} score: "))
        scorecard.add_score(score)

    print("The average is ", scorecard.average())

    print_scores(scorecard)
