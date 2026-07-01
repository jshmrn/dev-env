import shutil

from devenv import platform_ as plat
from devenv.pkgmanagers import apt, brew, winget
from devenv.steps.base import Step


def native_pkg_step(
    name: str,
    *,
    brew_pkg: str = None,
    apt_pkg: str = None,
    winget_id: str = None,
    brew_cask: bool = False,
    binary: str = None,
    platforms: set = None,
) -> Step:
    binary = binary or name
    platforms = platforms or plat.ALL

    def is_installed() -> bool:
        return shutil.which(binary) is not None

    def install() -> None:
        current = plat.detect()
        if current == plat.Platform.MACOS and brew_pkg:
            brew.install(brew_pkg, cask=brew_cask)
        elif current in (plat.Platform.LINUX, plat.Platform.WSL2) and apt_pkg:
            apt.install(apt_pkg)
        elif current == plat.Platform.WINDOWS and winget_id:
            winget.install(winget_id)
        else:
            raise RuntimeError(f"No install method defined for '{name}' on {current.value}")

    return Step(name=name, platforms=platforms, is_installed=is_installed, install=install)
