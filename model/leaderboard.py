# pyright: strict
from model.utils import *
from copy import deepcopy
import json
from pathlib import Path as FilePath

class Leaderboard:
    def __init__(self, mode: GameMode):
        self._mode = mode
        self._winners: list[LeaderboardEntry] = []

    @property
    def mode(self) -> GameMode:
        return self._mode
    
    @property
    def winners(self) -> list[LeaderboardEntry]:
        return self._winners
    
    def get_winners(self) -> list[LeaderboardEntry]:
        return [deepcopy(entry) for entry in self._winners]

    def sort_winners(self):
        self._winners.sort(key=lambda v: (-v.score, v.name))

    def add_winner(self, winner: LeaderboardEntry):
        if winner.mode != self._mode:
            return
        self._winners.append(winner)
        self.sort_winners()
        self.save_to_file()
    
    def save_to_file(self, filename: str = ""):
        if not filename:
            filename = self._mode.value + ".json"
        file = FilePath(__file__).parent.parent / "leaderboard" / filename
        with open(file, 'w') as f:
            entries = {k.name: k.score for k in self._winners}
            f.write(json.dumps(entries))

    def read_file(self, filename: str):
        if not filename:
            filename = self._mode.value + ".json"
        file = FilePath(__file__).parent.parent / "leaderboard" / filename
        try:
            with open(file, 'r') as f:
                json_string = f.readline()
                json_dict = json.loads(json_string)
                entries: dict[str, int] = {k: int(json_dict[k]) for k in json_dict}
                self._winners = [LeaderboardEntry(name, entries[name], self._mode) for name in entries]
                self.sort_winners()
        except FileNotFoundError:
            print(f"File was not found. Please ensure {filename} is in the correct directory.")

# TODO update to save leaderboard files in separate folder