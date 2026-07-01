import shutil
import subprocess

from devenv import platform_ as plat
from devenv.pkgmanagers import winget
from devenv.steps.base import Step


def is_installed() -> bool:
    return shutil.which("mise") is not None


def install() -> None:
    if plat.detect() == plat.Platform.WINDOWS:
        winget.install("jdx.mise")
    else:
        subprocess.run("curl https://mise.run | sh", shell=True, check=True)


STEP = Step(name="mise", platforms=plat.ALL, is_installed=is_installed, install=install)
