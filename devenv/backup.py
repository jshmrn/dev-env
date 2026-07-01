import shutil
from pathlib import Path

BACKUP_DIR = Path.home() / ".dev-env-backups"


def _marker_for(dest: Path) -> Path:
    return BACKUP_DIR / str(dest).replace("/", "__")


def copy_with_backup(src: Path, dest: Path) -> None:
    """Copy src to dest, preserving the first pre-existing file/dir at dest.

    Every run after the first overwrites dest unconditionally with src.
    """
    if dest.exists() or dest.is_symlink():
        marker = _marker_for(dest)
        if not marker.exists():
            BACKUP_DIR.mkdir(parents=True, exist_ok=True)
            if dest.is_dir() and not dest.is_symlink():
                shutil.copytree(dest, marker)
            else:
                shutil.copy2(dest, marker)

    dest.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dest, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dest)
