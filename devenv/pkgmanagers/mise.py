import shutil
import subprocess


def available() -> bool:
    return shutil.which("mise") is not None


def is_installed(tool: str) -> bool:
    return subprocess.run(["mise", "which", tool], capture_output=True).returncode == 0


def install(tool: str, version: str = "latest") -> None:
    subprocess.run(["mise", "use", "--global", f"{tool}@{version}"], check=True)
