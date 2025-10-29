"""Simple Hello DevOps app

This module exposes a function `greeting(name)` and a CLI entrypoint.
"""

import sys


def greeting(name: str) -> str:
    """Return a hello message for the given name.

    Args:
        name: person's name

    Returns:
        Greeting string
    """
    if name is None:
        raise ValueError("name must not be None")
    name_str = str(name).strip()
    if not name_str:
        return "Hello, DevOps!"
    return f"Hello, {name_str}!"


def main(argv=None):
    argv = argv or sys.argv[1:]
    name = argv[0] if argv else "DevOps"
    print(greeting(name))


if __name__ == "__main__":
    main()
