import shutil
import sys

MIN_PYTHON = (3, 9)


def check() -> None:
    problems = []

    if sys.version_info < MIN_PYTHON:
        problems.append(
            f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ is required, found "
            f"{sys.version_info.major}.{sys.version_info.minor}. Install a newer "
            "Python and re-run this script with it."
        )

    if shutil.which("git") is None:
        problems.append(
            "git was not found on PATH. Install it first:\n"
            "  macOS:               brew install git  (or the Xcode Command Line Tools)\n"
            "  Debian/Ubuntu/WSL2:  sudo apt-get install git\n"
            "  Windows:             winget install --id Git.Git"
        )

    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        sys.exit(1)
