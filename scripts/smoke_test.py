"""Smoke test for the hackers_manifesto Python package."""

import importlib
import sys


def main() -> int:
    try:
        module = importlib.import_module("hackers_manifesto")
    except Exception as exc:  # pragma: no cover
        print(f"FAIL: could not import hackers_manifesto: {exc}")
        return 1

    required_symbols = [
        "get_hackers_manifesto",
        "open_manifesto_in_browser",
    ]

    missing = [name for name in required_symbols if not hasattr(module, name)]
    if missing:
        print(f"FAIL: missing symbols: {', '.join(missing)}")
        return 1

    manifesto = module.get_hackers_manifesto()
    if not isinstance(manifesto, str):
        print("FAIL: get_hackers_manifesto() did not return str")
        return 1

    checks = [
        "The Conscience of a Hacker",
        "+++The Mentor+++",
        "we're all alike",
    ]
    missing_fragments = [fragment for fragment in checks if fragment not in manifesto]
    if missing_fragments:
        print(f"FAIL: manifesto missing expected text: {missing_fragments}")
        return 1

    print("OK: smoke test passed")
    print(f"Loaded from: {getattr(module, '__file__', 'unknown')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
