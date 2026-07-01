import shutil
import subprocess

from devenv import platform_ as plat
from devenv.pkgmanagers import apt, brew, winget
from devenv.steps.base import Step

APT_KEYRING = "/usr/share/keyrings/wezterm-fury.gpg"
APT_SOURCE = "/etc/apt/sources.list.d/wezterm.list"


def is_installed() -> bool:
    return shutil.which("wezterm") is not None


def _install_apt() -> None:
    # WezTerm isn't in the default Debian/Ubuntu repos; it ships its own apt repo.
    # https://wezterm.org/install/linux.html
    subprocess.run(
        f"curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o {APT_KEYRING}",
        shell=True, check=True,
    )
    subprocess.run(
        f"echo 'deb [signed-by={APT_KEYRING}] https://apt.fury.io/wez/ * *' | sudo tee {APT_SOURCE}",
        shell=True, check=True,
    )
    subprocess.run(["sudo", "chmod", "644", APT_KEYRING], check=True)
    apt.update()
    apt.install("wezterm")


def install() -> None:
    current = plat.detect()
    if current == plat.Platform.MACOS:
        brew.install("wezterm", cask=True)
    elif current in (plat.Platform.LINUX, plat.Platform.WSL2):
        _install_apt()
    elif current == plat.Platform.WINDOWS:
        winget.install("wez.wezterm")


STEP = Step(name="wezterm", platforms=plat.ALL, is_installed=is_installed, install=install)
