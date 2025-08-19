# MIT Introduction to Computer Science - Lecture 1 Notes

## Course Objectives
- **Knowledge of concepts**
- **Problem solving skills**
- **Programming proficiency**

---

## Finger Exercise - Lecture 1

**Problem:** Assume 3 variables are already defined for you: `a`, `b`, and `c`. Create a variable called `total` that adds `a` and `b` then multiplies the result by `c`. Include a last line in your code to print the value: `print(total)`

**Solution:**
```python
total = (a + b) * c
print(total)
```

---

## Course Topics

- How to apply computation to help solve problems
- Python programming language
- Organizing modular programs
- Simple but important algorithms
- Algorithmic complexity
- How to determine if programs are efficient

---

## Types of Knowledge

### Declarative Knowledge
Statement of fact - "what is true"

### Imperative Knowledge
How to do something or a **RECIPE** - "how to accomplish something"

> Programming is about writing recipes for a computer to execute

---

## Algorithm Example: Square Root Calculation

**Problem:** Find the square root of x (find y such that y × y = x)

**Algorithm:**
1. Start with an initial guess `g`
2. If `g × g` is close enough to `x`, stop and return `g`
3. Otherwise, make a new guess by averaging `g` and `x/g`
4. Repeat the process with the new guess until close enough

### Numerical Example (x = 16)
- Initial guess: `g = 3`
- Check: `g × g = 9` (not close enough to 16)
- Calculate new guess: `(g + x/g) / 2 = (3 + 16/3) / 2 = (3 + 5.33) / 2 = 4.17`
- New guess: `g = 4.17`
- Continue process until satisfactory accuracy

**Key Algorithm Components:**
- A sequence of simple steps
- Flow control process that specifies when each step executes
- A means of determining when to stop

---

## Computer Fundamentals

> **Computers are machines that execute algorithms**

### Computer Capabilities
1. **Speed:** Performs simple operations at hundreds of billions per second
2. **Memory:** Can store hundreds of gigabytes of information

### Types of Calculations
1. **Built into the machine** (e.g., basic arithmetic like `+`)
2. **User-defined** (ones you create as a programmer)

---

## Computer Architecture Components

- **Memory** - stores data and instructions
- **Arithmetic/Logic Unit (ALU)** - performs calculations and logical operations
- **Control Unit** - coordinates execution of instructions
- **Input/Output** - handles communication with external world

---

## Programming Language Primitives

**Turing's Discovery:** You can compute anything with only 6 basic primitives:
- left
- right  
- print
- scan
- erase
- no operation (no-op)

**Real Programming Languages** provide more convenient primitives:
- **English:** primitives are words
- **Programming Languages:** primitives are numbers, strings, and simple operators

---

## Where Programs Go Wrong

### 1. Syntactic Errors
- **Common and easily caught**
- Violations of language grammar rules
- Usually caught by the interpreter before running

### 2. Static Semantic Errors
- **Some languages check before running**
- **Can cause unpredictable behavior**
- Code is syntactically correct but doesn't make logical sense

### 3. Logical Errors
- **No linguistic errors but different meaning from intent**
- Program may:
  - Crash or stop running unexpectedly
  - Run forever (infinite loop)
  - Give an answer, but it's wrong

---

## Python Programs Structure

**A Python program consists of:**
- **Definitions** - evaluated by the interpreter
- **Commands** - executed by the Python interpreter in a shell

### Program Execution
- Commands instruct the interpreter to perform actions
- Can be typed directly in a shell (interactive mode)
- Can be stored in a file and executed all at once

### Objects
Programs work with **objects** - the fundamental data units in Python

---

## Key Takeaways

1. Programming is about creating step-by-step instructions (algorithms)
2. Computers excel at speed and storage but need precise instructions
3. Understanding different types of errors helps in debugging
4. Python provides a user-friendly way to communicate with computers
5. Everything in Python is an object

## more on objects

1. Programs manipulate **data objects**
2. Objects have a **type** that defines the kinds of things programs can do to them:
- 30:
    - is a number
    - we can add/subtract/divide/multiply/exponent/etc.

-"Anna":
    - is a sequence of characters (a **string**)
    - we can grab substrings but we can't divide by a number

3. Scalar objects(cannot be subdivided)
    - numbers
    - truth value
    - int, float, bool, NoneType
    - use type() to see the type of an object

4. Non-Scalar objects(have internal structure that can be accessed)
    - lists
    - dictionaries
    - sequence of characters (strings)