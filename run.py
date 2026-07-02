#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path

from devenv import platform_ as plat
from devenv import preflight
from devenv.steps import discover


def _ensure_local_bin_on_path() -> None:
    # mise, pipx, and the Claude Code native installer all place binaries in
    # ~/.local/bin. On a fresh machine that directory isn't on PATH yet, so a
    # tool installed by one step is invisible to subprocess calls made by a
    # later step in this same run unless we add it ourselves.
    local_bin = str(Path.home() / ".local" / "bin")
    path_entries = os.environ.get("PATH", "").split(os.pathsep)
    if local_bin not in path_entries:
        os.environ["PATH"] = os.pathsep.join([local_bin, *path_entries])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Provision this machine's dev environment.")
    parser.add_argument("--only", help="Comma-separated step names to run (default: all)")
    parser.add_argument("--skip", help="Comma-separated step names to skip")
    parser.add_argument("--dry-run", action="store_true", help="Preview steps without executing them")
    parser.add_argument("--list", action="store_true", help="List steps for this platform and exit")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    _ensure_local_bin_on_path()
    preflight.check()

    current = plat.detect()
    print(f"Detected platform: {current.value}")

    steps = [s for s in discover() if s.applies_to(current)]
    steps.sort(key=lambda s: (s.name.startswith("config-"), s.name))

    if args.list:
        for step in steps:
            print(step.name)
        return

    only = set(args.only.split(",")) if args.only else None
    skip = set(args.skip.split(",")) if args.skip else set()

    failures = []
    for step in steps:
        if only is not None and step.name not in only:
            continue
        if step.name in skip:
            continue

        if step.is_installed():
            print(f"[SKIP] {step.name}: already installed")
            continue

        if args.dry_run:
            print(f"[DRY_RUN] would run: {step.name}")
            continue

        print(f"[RUN] {step.name}")
        try:
            step.install()
        except Exception as exc:
            print(f"[FAIL] {step.name}: {exc}", file=sys.stderr)
            failures.append(step.name)

    if failures:
        print(f"\n{len(failures)} step(s) failed: {', '.join(failures)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
