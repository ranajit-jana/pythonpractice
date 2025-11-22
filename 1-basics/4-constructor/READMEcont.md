Great — let’s go deeper into **how the Python Virtual Machine actually creates, initializes, and manages objects**.
I’ll explain it step-by-step but still keep it simple and practical.

---

# 🔥 **Part 1 — What PVM does when you write `obj = MyClass(10, 20)`**

When Python sees this line, it runs through these internal steps:

---

# **1️⃣ Load the class (`MyClass`)**

Python looks up the class reference inside memory (namespace dictionary).

---

# **2️⃣ Create the object — call `__new__`**

PVM executes bytecode equivalent to:

```python
tmp = MyClass.__new__(MyClass)
```

`__new__`:

* Allocates memory for a new object
* Returns an instance (raw, empty shell)

👀 Important
If `__new__` returns a different object, Python **never calls `__init__`**.

This is why immutable types like `int` and `str` override `__new__`.

---

# **3️⃣ Initialize the object — call `__init__`**

Now Python calls:

```python
MyClass.__init__(tmp, 10, 20)
```

`__init__`:

* Adds attributes
* Sets initial values
* Configures object state

---

# **4️⃣ Assign the reference**

Variable `obj` is now made to point to this memory location:

```python
obj = tmp
```

✔ Python variables = references
✔ No object copying
✔ A variable is like a label pointing to memory

---

# Part 2 — What happens inside the PVM (Python Virtual Machine)?

PVM executes **bytecode**, produced by the Python compiler.

Example:

```python
obj = MyClass(10, 20)
```

Bytecode (simplified):

```
LOAD_GLOBAL MyClass
LOAD_CONST 10
LOAD_CONST 20
CALL_FUNCTION 2
STORE_NAME obj
```

Meaning:

1. Get class reference
2. Load arguments
3. Call class (which triggers `__new__` + `__init__`)
4. Store resulting object reference in variable

---

# part 3 — Object storage: how Python stores things in memory (important)

Every Python object has:

### ✔ **A type**

* Points to class
  Example: `<class 'MyClass'>`

### ✔ **A reference count**

Number of variables pointing to it

### ✔ **An internal dictionary (`__dict__`)**

Where attributes live

### ✔ **A memory pointer**

Where object data is stored

Example object structure:

```
+--------------------------------------+
| PyObject Header                      |
|  - Type pointer → MyClass            |
|  - Reference count                   |
+--------------------------------------+
| Data (attributes)                    |
|  __dict__ = { "x": 10, "y": 20 }     |
+--------------------------------------+
```

---

# part 4 — Reference counting (how Python knows when to delete your object)

Every time you create or copy a reference:

```python
a = obj   # reference count +1
b = obj   # reference count +1
```

When references are removed:

```python
del a     # refcount -1
```

When refcount hits **0**, Python auto-deletes the object.

CPython uses:

* Reference counting (primary)
* Garbage collector for cyclic references (backup)

---

# part 5 — Why `__new__` exists separately from `__init__`

### `__new__` → create the object

Used for immutable types (int, str, tuple)

### `__init__` → configure the object

Used for normal mutable objects (class instances)

Example with `int`:

```python
class MyInt(int):
    def __new__(cls, value):
        print("creating integer")
        return super().__new__(cls, value)

    def __init__(self, value):
        print("initializing integer")
```

Immutable objects must be built in `__new__` because they cannot change after creation.

---

# part 6 — Important fact: class call triggers both methods

When you write:

```python
MyClass(10, 20)
```

Internally:

```
MyClass.__call__(10, 20)
    → calls __new__
    → calls __init__
```

So, classes behave like functions because they implement `__call__`.

---

# ✔ Summary Diagram

```
MyClass(10, 20)
        │
        ▼
  __new__(MyClass)      → allocates memory
        │ returned object
        ▼
  __init__(obj, 10, 20) → initializes attributes
        │
        ▼
  obj stored in variable
```
