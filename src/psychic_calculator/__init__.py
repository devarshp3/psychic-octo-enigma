"""psychic_calculator package.

Expose calculator functions at package level for simple imports:

```py
from psychic_calculator import add, divide
```
"""

from .calculator import add, divide, multiply, subtract

__all__ = ["add", "subtract", "multiply", "divide"]
