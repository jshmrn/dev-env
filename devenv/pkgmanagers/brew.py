import shutil
import subprocess


def available() -> bool:
    return shutil.which("brew") is not None


def is_installed(pkg: str, cask: bool = False) -> bool:
    cmd = ["brew", "list", "--cask", pkg] if cask else ["brew", "list", "--formula", pkg]
    return subprocess.run(cmd, capture_output=True).returncode == 0


def install(pkg: str, cask: bool = False) -> None:
    cmd = ["brew", "install", "--cask", pkg] if cask else ["brew", "install", pkg]
    subprocess.run(cmd, check=True)
