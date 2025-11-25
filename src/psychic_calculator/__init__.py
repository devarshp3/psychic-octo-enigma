"""psychic_calculator package.

Expose calculator functions at package level for simple imports:

```py
from psychic_calculator import add, divide
```
"""
from .calculator import add, subtract, multiply, divide

__all__ = ["add", "subtract", "multiply", "divide"]
