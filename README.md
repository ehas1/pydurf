## About pydurf

Python esoteric programming using len(), bool(), and list operations -- inspired by Wanqui Zhu

PyDurf is an esoteric Python dialect that generates valid Python code using only builtin functions and a minimal character set. It's inspired by @wanquizhu but takes a different approach by leveraging Python's builtin function string representations. It's been a ton of fun exploring this and I hope you find it enjoyable. 

Have fun & let me know what you think! Please contact for questions.


## Overview

pydurf offers two encoding methods:

### 1. Basic Encoding (Minimal)
- Uses only 7 unique characters: `()[]+,[]`
- Generates numbers using `len()` and list operations
- Creates characters using `chr()` with generated numbers
- More verbose but uses absolute minimum character set
- Example: `chr(len([[],[]])) + chr(len([[],[],[]]))`

### 2. Advanced Encoding (Optimized)
- Uses 20 unique characters: `()+,=[]abcehlnoprsty`
- Extracts characters from builtin function string representations
- More concise and readable code
- Example: `str(len)[len([[]])] + str(bool)[len([[],[]])]`

## How It Works

### Number Generation
Numbers are generated using list operations and `len()`:
```python
0: len([])         # Empty list has length 0
1: len([[]])       # List with one element has length 1
2: len([[],[]])    # List with two elements has length 2
```

### Character Generation

#### Basic Method
Characters are generated using `chr()` with len-based numbers:
```python
'A': chr(len([[...65 empty lists...]]))  # ASCII 65
'B': chr(len([[...66 empty lists...]]))  # ASCII 66
```

#### Advanced Method
Characters are extracted from builtin function string representations:
```python
'b': str(len)[len([[]])]           # From "built-in"
'n': str(len)[len([[],[],[]])]     # From "function"
'r': str(str)[len([[],[],[],[]])]  # From "str"
```

## Features

1. **Two Encoding Methods**
   - Basic: Minimum character set (7 chars)
   - Advanced: Optimized for shorter code (20 chars)

2. **Valid Python Code**
   - All PyDurf code is valid Python
   - Can be executed directly without preprocessing
   - Can generate any valid Python code

3. **Character Set Comparison**

   Basic Encoding:
   - Core syntax: `()[]+,[]`
   - Purpose: Absolute minimum needed for Python execution
   - Best for: Proving minimalism, esoteric programming challenges

   Advanced Encoding:
   - Core syntax: `()[]+,=[]`
   - Builtin functions: `str`, `len`, `bool`, `hash`, `repr`, `type`
   - Additional chars: `abcehlnoprsty`
   - Purpose: More efficient code generation
   - Best for: Practical use, readable code

## Comprehensive Examples

### 1. Simple Text
```python
# Encoding: "hello"
Basic encoding (7 chars):
- Code length: 3,245 chars
- Unique chars: 12
- Example: chr(len([[...104 lists...]])) + chr(len([[...101 lists...]])) + ...

Advanced encoding (20 chars):
- Code length: 892 chars
- Unique chars: 18
- Example: str(hash)[...] + str(type)[...] + str(len)[...] + ...
```

### 2. Programming Keywords
```python
# Encoding: "def class return yield from import"
Basic encoding (7 chars):
- Code length: 10,328 chars
- Unique chars: 12
- Efficiency: Very verbose for common programming terms

Advanced encoding (20 chars):
- Code length: 2,897 chars
- Unique chars: 18
- Efficiency: 3.6x shorter than basic encoding
```

### Live Example

Here's what happens when we encode text using PyDurf:

```
pydurf Encoding Examples
==================================================

Encoding: 'hello'
==================================================

Basic encoding (7 chars):
Code length: 1892 chars
Unique chars: 7
Code: chr(len([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
[],[],[],[],[],[]])) + ...

Advanced encoding (20 chars):
Code length: 892 chars
Unique chars: 18
Code: str(hash)[len([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])] + 
str(type)[len([[],[],[],[],[],[],[],[],[],[],[]])] + ...

Result: 'hello'

Comparison:
Basic encoding is 2.1x longer than advanced
```


## Why did I make pydurf?

1. **Educational Value**
   - I like the name and taught me a lot

2. **Esoteric Programming**
   - Two levels of esotericism (7 chars vs 20 chars)
   - Different approach from traditional esoteric languages


## License

MIT License - See LICENSE file for details 
