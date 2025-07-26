"""
player.py
Defines the abstract class for all types of players
This includes human players and bots
"""
from abc import ABC, abstractmethod


class Player(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def guess(self, num_slots: int) -> tuple[int, ...]:
        pass

    @abstractmethod
    def process_result(self, guess: tuple[int, ...], result: int) -> None:
        pass
