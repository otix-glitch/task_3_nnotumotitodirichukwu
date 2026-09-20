# Random Password Generator

A command-line Python program that creates secure random passwords using Python's `secrets` module.

## Features

- Generates passwords with lowercase letters, uppercase letters, numbers, and symbols.
- Lets you choose the password length.
- Requires a minimum length of 4 characters.
- Uses cryptographically secure randomness.
- Handles invalid input without crashing.

## Requirements

- Python 3.6 or newer

No external packages are required.

## Usage

From the project directory, run:

```bash
python skills/random-password-generator.py
```

When prompted, enter the desired password length:

```text
Random Password Generator
Password length (minimum 4): 12
Generated password: I0(+.=ulN]"d
```

The generated password will be different each time.

## Python Function

The `generate_password()` function can also be imported into another Python file:

```python
from skills.random-password-generator import generate_password

password = generate_password(16)
print(password)
```

The function accepts these options:

```python
generate_password(
    length=16,
    use_uppercase=True,
    use_digits=True,
    use_symbols=True,
)
```

At least one character type is always included: lowercase letters. The requested length must be large enough to include every enabled character type.

## Security Note

The generator uses `secrets.choice()` and `secrets.SystemRandom()`, which are intended for security-sensitive random values. Avoid sharing generated passwords or storing them in plain text.
