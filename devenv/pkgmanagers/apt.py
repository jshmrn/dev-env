import shutil
import subprocess

_updated = False


def available() -> bool:
    return shutil.which("apt-get") is not None


def is_installed(pkg: str) -> bool:
    return subprocess.run(["dpkg", "-s", pkg], capture_output=True).returncode == 0


def install(pkg: str) -> None:
    global _updated
    if not _updated:
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        _updated = True
    subprocess.run(["sudo", "apt-get", "install", "-y", pkg], check=True)
