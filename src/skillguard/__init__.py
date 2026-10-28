"""
Deprecated alias for :mod:`skillshield`.

skillguard was renamed to skillshield in 1.1.0. ``import skillguard`` and
``from skillguard.rules import ...`` keep working until 2.0.0, and each
returns the same objects as the matching ``skillshield`` import.
"""

import importlib
import sys
import warnings

from skillshield import *  # noqa: F401,F403
from skillshield import __all__, __author__, __version__  # noqa: F401

warnings.warn(
    "The 'skillguard' package is now 'skillshield'. Change 'import skillguard' to "
    "'import skillshield'; the old name will be removed in 2.0.0.",
    DeprecationWarning,
    stacklevel=2,
)

# Make skillguard.rules, skillguard.scanner, etc. the same module objects as
# their skillshield counterparts, so isinstance checks and patches still line up.
for _name in ("cli", "models", "rules", "sarif", "scanner"):
    sys.modules[f"{__name__}.{_name}"] = importlib.import_module(f"skillshield.{_name}")
    globals()[_name] = sys.modules[f"{__name__}.{_name}"]
del _name
