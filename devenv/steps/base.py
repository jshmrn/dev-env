from dataclasses import dataclass
from typing import Callable

from devenv.platform_ import Platform


@dataclass
class Step:
    name: str
    platforms: set
    is_installed: Callable[[], bool]
    install: Callable[[], None]

    def applies_to(self, current: Platform) -> bool:
        return current in self.platforms
