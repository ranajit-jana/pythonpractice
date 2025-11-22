`builtin.pyi` (sometimes written as `_builtin.pyi`, `builtins.pyi`) is a **type stub file** used by Python type checkers (like *mypy*, *pyright*, *pylance*) and IDEs.

Let me break it down simply and clearly:

---

# ✅ **What is `builtins.pyi`?**

It is a **“.pyi” stub file** that contains *type definitions* for all the **built-in Python functions, types, and exceptions**, such as:

* `len()`
* `print()`
* `int`, `str`, `dict`, `list`
* `Exception`
* `range`
* `abs()`
* etc.

This file comes **from the Python standard library**, but it is not executed.
It is only used for *type hinting* and *editor auto-completion*.

---

# 📌 **Why “.pyi” ?**

`.pyi` means **Python Interface** file.

It has:

* function signatures
* class definitions
* type information

but **no real code**.

Example:

```python
# inside builtins.pyi
def len(obj: Sized) -> int: ...
```

No body — just `...`.

---

# 🧠 Why does Python need `builtins.pyi`?

1. **Type checkers** use it
   So tools like mypy know the correct signatures of built-ins.

2. **Language servers / editors** use it
   VS Code, PyCharm, etc. use it to provide:

   * autocomplete
   * signature help
   * error checking

3. **Static analysis** tools rely on it
   It helps these tools understand your code without running it.

---

# 📍 Where is it located?

It usually comes from the **typeshed** project (official repo that maintains stubs).
Most editors bundle it internally, e.g.:

```
python_library/typeshed/stdlib/builtins.pyi
```

Your system Python usually does **not** include it directly.
It is usually part of:

* `pyright`
* `pylance`
* `mypy`
* IDE internal typeshed

---

# 📌 Summary

| File           | Meaning                         | Purpose                         |
| -------------- | ------------------------------- | ------------------------------- |
| `.py`          | executable Python code          | runtime                         |
| `.pyi`         | type stub/interface             | static analysis, autocompletion |
| `builtins.pyi` | definitions of Python built-ins | IDE + type checker support      |

---

# ✔️ In one sentence

**`builtins.pyi` is a type stub file that describes all Python built-in functions and types for static type checking and autocomplete, not for execution.**

