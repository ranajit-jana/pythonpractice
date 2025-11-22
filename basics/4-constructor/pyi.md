# Python `.pyi` and MRO Cheat‑Sheet

A concise reference you can commit to your repository.

---

## 1. What is a `.pyi` File?

A `.pyi` file is a **type stub file** used by type checkers (like mypy) to describe:

* The functions
* Classes
* Variables
* Signatures
* Types

It **contains no implementation**, only type definitions.

Use cases:

* Provide types for libraries written in C or compiled extensions.
* Override/improve type hints for third‑party libraries.
* Create stable public API signatures.

---

## 2. Basic `.pyi` Structure

```python
# example.pyi
from typing import Optional

def add(x: int, y: int) -> int: ...

class User:
    name: str
    age: int
    def greet(self) -> str: ...
```

`...` means “no implementation”.

---

## 3. Stubs for Modules

If `example.py` exists, you can create:

```
example.pyi
```

Mypy will use the `.pyi` first.

---

## 4. Class Attributes in `.pyi`

```python
class Config:
    host: str
    port: int
    debug: bool
```

This declares attributes without defining `__init__`.

If needed:

```python
class Config:
    host: str
    port: int
    debug: bool
    def __init__(self, host: str, port: int, debug: bool = ...) -> None: ...
```

---

## 5. Overloads in `.pyi`

```python
from typing import overload

@overload
def load(value: int) -> str: ...

@overload
def load(value: str) -> int: ...

def load(value): ...  # implementation in .py
```

---

## 6. Private Members in Stubs

Prefix with `_`:

```python
def _helper() -> None: ...
```

---

## 7. Distributing Stub Files

Two ways:

### A. Inline (same project)

Place `.pyi` file next to `.py`.

### B. Stub Packages

For third‑party libs:

```
packagename-stubs/
└── packagename/
    └── __init__.pyi
```

Include:

```
pyproject.toml → contains: "typing_extensions" or "PEP 561" settings
```

---

## 8. MRO (Method Resolution Order) — Short Summary

MRO defines **the order in which Python searches classes** when executing:

* Attribute lookup
* Methods
* `super()` calls

Python uses **C3 linearization**.

Get MRO programmatically:

```python
ClassName.__mro__
ClassName.mro()
```

---

## 9. Simple MRO Example

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
```

Output:

```
[D, B, A, C, object]
```

Python ensures:

* monotonicity
* consistent ordering
* avoids diamond conflicts

---

## 10. `super()` and MRO

`super()` follows the MRO order.

```python
class A:
    def run(self): print("A")

class B(A):
    def run(self):
        super().run()
        print("B")

class C(A):
    def run(self):
        super().run()
        print("C")

class D(B, C):
    def run(self):
        super().run()
        print("D")
```

Run:

```python
D().run()
```

Output:

```
A
C
B
D
```

This is the classic diamond pattern resolved by MRO.

---

## 11. Why `.pyi` + MRO Matters

* `.pyi` files describe types for classes — often in complex multiple‑inheritance structures.
* Understanding MRO helps write correct stub class hierarchies.

Example:

```python
class Manager(Employee, Logger): ...
```

Stub must reflect correct MRO.

---

## 12. Best Practices

* Keep `.pyi` files minimal.
* Use `...` instead of `pass`.
* Only include public API unless documenting private API is required.
* Use overload where needed.
* Check with `mypy --strict`.

---

## 13. Useful Mypy Commands

```
mypy yourproject/
```

Strict mode:

```
mypy yourproject/ --strict
```

Check stubs only:

```
mypy --disallow-untyped-defs
```

---

## 14. References

* mypy: Stub Files documentation
* typing documentation: Writing Stubs
* PEP 484: Type Hints
* PEP 561: Distributing Stub Files
* MRO: C3 Linearization (Python docs)

