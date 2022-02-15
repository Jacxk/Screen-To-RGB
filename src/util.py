from pathlib import Path
from typing import List
from re import match

from .interface.mode import Mode
from .interface.sdk import SDK

def initialize_modes() -> List[Mode]:
    modes = []
    paths = list(Path("src/handlers/modes").rglob("*.py"))
    paths = [*map(Path.stem.fget, paths)]

    for path in paths:
        mod = __import__(f'src.handlers.modes.{path}', fromlist=[path])
        klass = getattr(mod, path)
        modes.append(klass)

    return modes

def initialize_sdks() -> List[SDK]:
    sdks = []
    paths = list(Path("src/handlers/sdk").rglob("*.py"))
    paths = [*map(Path.stem.fget, paths)]

    for path in paths:
        mod = __import__(f'src.handlers.sdk.{path}', fromlist=[path])
        klass = getattr(mod, path)
        sdks.append(klass)

    return sdks
