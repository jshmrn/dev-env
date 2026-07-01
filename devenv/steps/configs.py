from pathlib import Path

from devenv import platform_ as plat
from devenv.backup import copy_with_backup
from devenv.steps.base import Step

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIGS_DIR = REPO_ROOT / "configs"

CONFIG_FILES = [
    ("config-zsh", ".zshrc", plat.UNIX),
    ("config-zprofile", ".zprofile", {plat.Platform.MACOS}),
    ("config-wezterm", ".wezterm.lua", plat.ALL),
    ("config-nvim", ".config/nvim/init.lua", plat.ALL),
    ("config-nvim-lock", ".config/nvim/nvim-pack-lock.json", plat.ALL),
    ("config-tmux", ".tmux.conf", plat.UNIX),
    ("config-git", ".gitconfig", plat.ALL),
    ("config-claude", ".claude/settings.json", plat.ALL),
]


def _make_step(name: str, rel_path: str, platforms: set) -> Step:
    src = CONFIGS_DIR / rel_path
    dest = Path.home() / rel_path

    def install() -> None:
        copy_with_backup(src, dest)

    return Step(name=name, platforms=platforms, is_installed=lambda: False, install=install)


STEPS = [_make_step(name, rel_path, platforms) for name, rel_path, platforms in CONFIG_FILES]
