import math
import plateresult as p


class BarbellCalc:

    WEIGHT_VALUES = [45,35,25,15,10,5]

    def __init__(self, weight: int, barbellWeight = 45) -> None:
        self.weight = weight
        self.barbellWeight = barbellWeight
        self.barGoal = self.weight - self.barbellWeight

    def calculate(self):
        results = []

        for i in range(len(self.WEIGHT_VALUES)):
            count = math.floor(self.barGoal / (self.WEIGHT_VALUES[i] * 2))
            count *= 2
            results.append(p.PlateResult(self.WEIGHT_VALUES[i], count))

            self.barGoal -= self.WEIGHT_VALUES[i] * count

        self.printResults(results)

    def printResults(self, results: list):
        for i in range(len(results)):
            print(results[i])