from typing import List


class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value


def print_cards(cards: List[Card]) -> None:
    str_list = [card.suit + str(card.value) for card in cards]
    print(" ".join(str_list))
    return None


def bubble(A: List[Card]) -> None:
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j].value < A[j - 1].value:
                A[j], A[j - 1] = A[j - 1], A[j]
    return None


def selection(A: List[Card]) -> None:
    for i in range(len(A) - 1):
        minj = i
        for j in range(i, len(A)):
            if A[j].value < A[minj].value:
                minj = j
        A[i], A[minj] = A[minj], A[i]
    return None


N = int(input())
inputs = list(input().split())
C1: List[Card] = [Card(i[0], int(i[1])) for i in inputs]
C2: List[Card] = C1.copy()

bubble(C1)
selection(C2)

print_cards(C1)
print("Stable")

print_cards(C2)
if C1 == C2:
    print("Stable")
else:
    print("Not stable")
