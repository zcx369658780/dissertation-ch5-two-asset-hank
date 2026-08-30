"""Pure finite-root path guard used by focused MP4B validation tests."""
from pathlib import PureWindowsPath


def _norm(path: str) -> str:
    return str(PureWindowsPath(path)).rstrip("\\").casefold()


def helper_is_in_verified_pair(helper: str, logical_root: str, physical_root: str) -> bool:
    parent = _norm(str(PureWindowsPath(helper).parent))
    allowed = {_norm(logical_root), _norm(physical_root)}
    return parent in allowed and len(allowed) in (1, 2)
