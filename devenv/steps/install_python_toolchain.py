import subprocess

from devenv import platform_ as plat
from devenv.pkgmanagers import mise
from devenv.steps.base import Step


def is_installed() -> bool:
    if not mise.is_installed("python"):
        return False
    return subprocess.run(
        ["mise", "exec", "--", "python", "-m", "pipx", "--version"],
        capture_output=True,
    ).returncode == 0


def install() -> None:
    mise.install("python", "latest")
    subprocess.run(
        ["mise", "exec", "--", "python", "-m", "pip", "install", "--user", "pipx"],
        check=True,
    )


STEP = Step(
    name="python-toolchain",
    platforms=plat.ALL,
    is_installed=is_installed,
    install=install,
)
