class PlateResult:
    def __init__(self, weight: int, count: int) -> None:
        self.weight = weight
        self.count = count

    def __str__(self) -> str:
        return f"PlateResult: Weight:{self.weight} Count:{self.count}"