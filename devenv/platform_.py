import os
import platform
from enum import Enum


class Platform(Enum):
    MACOS = "macos"
    LINUX = "linux"
    WSL2 = "wsl2"
    WINDOWS = "windows"


def _is_wsl2() -> bool:
    if "WSL_DISTRO_NAME" in os.environ:
        return True
    try:
        with open("/proc/version") as f:
            return "microsoft" in f.read().lower()
    except OSError:
        return False


def detect() -> Platform:
    system = platform.system()
    if system == "Darwin":
        return Platform.MACOS
    if system == "Windows":
        return Platform.WINDOWS
    if system == "Linux":
        return Platform.WSL2 if _is_wsl2() else Platform.LINUX
    raise RuntimeError(f"Unsupported platform: {system!r}")


ALL = {Platform.MACOS, Platform.LINUX, Platform.WSL2, Platform.WINDOWS}
UNIX = {Platform.MACOS, Platform.LINUX, Platform.WSL2}
