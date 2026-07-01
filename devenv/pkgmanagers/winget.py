import shutil
import subprocess


def available() -> bool:
    return shutil.which("winget") is not None


def is_installed(pkg_id: str) -> bool:
    result = subprocess.run(
        ["winget", "list", "--id", pkg_id, "--exact"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0 and pkg_id in result.stdout


def install(pkg_id: str) -> None:
    subprocess.run(
        [
            "winget", "install", "--id", pkg_id, "--exact",
            "--accept-source-agreements", "--accept-package-agreements",
        ],
        check=True,
    )
