"""Unit tests for the small `greeting` helper.

These tests are intentionally tiny — they're for an interview/demo project.

Tests cover:
- normal name input
- empty and whitespace-only input (should use default message)
- None input raises ValueError
"""

from app import greeting
import pytest


def test_greeting_with_name():
    """greeting should return a formatted hello for a provided name."""
    assert greeting("Dennis") == "Hello, Dennis!"


def test_greeting_empty_or_whitespace():
    """Empty or whitespace-only names should fall back to the default message."""
    assert greeting("") == "Hello, DevOps!"
    assert greeting("  ") == "Hello, DevOps!"


def test_greeting_none_raises():
    """Passing None should raise a ValueError to signal invalid input."""
    with pytest.raises(ValueError):
        greeting(None)
