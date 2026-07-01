from devenv import platform_ as plat
from devenv.steps._native_factory import native_pkg_step

STEPS = [
    native_pkg_step("git", brew_pkg="git", apt_pkg="git", winget_id="Git.Git"),
    native_pkg_step(
        "ripgrep", brew_pkg="ripgrep", apt_pkg="ripgrep",
        winget_id="BurntSushi.ripgrep.MSVC", binary="rg",
    ),
    native_pkg_step(
        "neovim", brew_pkg="neovim", apt_pkg="neovim",
        winget_id="Neovim.Neovim", binary="nvim",
    ),
    native_pkg_step("fzf", brew_pkg="fzf", apt_pkg="fzf", winget_id="junegunn.fzf"),
    native_pkg_step("tmux", brew_pkg="tmux", apt_pkg="tmux", platforms=plat.UNIX),
    native_pkg_step(
        "wezterm", brew_pkg="wezterm", apt_pkg="wezterm",
        winget_id="wez.wezterm", brew_cask=True,
    ),
]
