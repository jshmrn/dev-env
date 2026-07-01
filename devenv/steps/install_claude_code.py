import shutil
import subprocess

from devenv import platform_ as plat
from devenv.steps.base import Step


def is_installed() -> bool:
    return shutil.which("claude") is not None


def install() -> None:
    if plat.detect() == plat.Platform.WINDOWS:
        subprocess.run(
            ["powershell", "-Command", "irm https://claude.ai/install.ps1 | iex"],
            check=True,
        )
    else:
        subprocess.run("curl -fsSL https://claude.ai/install.sh | bash", shell=True, check=True)


STEP = Step(name="claude-code", platforms=plat.ALL, is_installed=is_installed, install=install)
