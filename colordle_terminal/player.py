"""
player.py
Defines the abstract class for all types of players
This includes human players and bots
"""
from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def guess(self, num_slots: int) -> tuple[int]:
        pass

    @abstractmethod
    def process_result(self, result: int) -> None:
        pass
