# string_utils

A lightweight, dependency-free Python library of string helpers: case conversion, text analysis, string comparison, number-system and encoding conversions, and IP address validation.

## Installation

Copy `StringUtils.py` into your project, then:

```python
import StringUtils as su
```

## Quick start

```python
import StringUtils as su

su.to_snake_case("HelloWorld")        # "hello_world"
su.to_camel_case("hello_world")       # "helloWorld"
su.levenshtein("kitten", "sitting")   # 3
su.rot13("Hello")                     # "Uryyb"
su.text_to_binary("Hi")               # "01001000 01101001"
su.is_valid_ipv4("192.168.1.1")       # True
su.is_private_ip("10.0.0.5")          # True
```

## API reference

### Case conversion

| Function | Description | Example |
|---|---|---|
| `to_snake_case(string)` | Convert to `snake_case` | `"Hello World"` → `"hello_world"` |
| `to_camel_case(string)` | Convert to `camelCase` | `"hello world"` → `"helloWorld"` |
| `to_kebab_case(string)` | Convert to `kebab-case` | `"Hello World"` → `"hello-world"` |
| `to_constant_case(string)` | Convert to `CONSTANT_CASE` | `"hello world"` → `"HELLO_WORLD"` |
| `dot_case(string)` | Convert to `dot.case` | `"Hello World"` → `"hello.world"` |
| `title_case(string)` | Capitalize each word | `"hello world"` → `"Hello World"` |
| `to_lower_case(string)` | Lowercase the string | `"HeLLo"` → `"hello"` |
| `to_upper_case(string)` | Uppercase the string | `"hello"` → `"HELLO"` |
| `swap_case(string)` | Invert the case of each letter | `"Hello"` → `"hELLO"` |
| `is_upper_case(string)` | `True` if the string is all uppercase | `"ABC"` → `True` |
| `is_lower_case(string)` | `True` if the string is all lowercase | `"abc"` → `True` |

### Text manipulation and analysis

| Function | Description |
|---|---|
| `reverse(string)` | Return the string reversed |
| `rot13(string)` | Apply the ROT13 letter-substitution cipher |
| `longest_word(string)` | Return the longest word in the string |
| `char_frequency(string)` | Count occurrences of each character |
| `vowel_count(string)` | Count the vowels in the string |
| `center_print(string)` | Print the string centered in the terminal |
| `pretty_print(string)` | Print the string with decorative formatting |

### String comparison

| Function | Description |
|---|---|
| `levenshtein(a, b)` | Edit distance: minimum insertions, deletions and substitutions to turn `a` into `b` |
| `lcs(a, b)` | Longest common subsequence of `a` and `b` |
| `similarity(...)` | Similarity score between two strings |
| `hamming_distance(...)` | Number of positions at which two equal-length strings differ |
| `compare_versions(...)` | Compare version strings such as `"1.2.10"` vs `"1.10.0"` |

### Number systems and encodings

| Function | Description | Example |
|---|---|---|
| `to_binary(n)` | Integer → binary string | `10` → `"1010"` |
| `from_binary(string)` | Binary string → integer | `"1010"` → `10` |
| `to_hex(...)` | Integer → hexadecimal string | `255` → `"ff"` |
| `from_hex(string)` | Hexadecimal string → integer | `"ff"` → `255` |
| `to_octal(...)` | Integer → octal string | `8` → `"10"` |
| `from_octal(string)` | Octal string → integer | `"10"` → `8` |
| `text_to_binary(string)` | Text → binary representation of each character | `"A"` → `"01000001"` |
| `binary_to_text(string)` | Binary representation → text | `"01000001"` → `"A"` |
| `text_to_hex(string)` | Text → hexadecimal representation | `"Hi"` → `"4869"` |
| `hex_to_text(string)` | Hexadecimal representation → text | `"4869"` → `"Hi"` |
| `ascii_codes(s)` | List of ASCII/Unicode code points | `"Hi"` → `[72, 105]` |

### Networking

| Function | Description | Example |
|---|---|---|
| `is_valid_ipv4(string)` | `True` if the string is a valid IPv4 address | `"192.168.0.1"` → `True` |
| `is_valid_ipv6(string)` | `True` if the string is a valid IPv6 address | `"::1"` → `True` |
| `is_private_ip(string)` | `True` if the address is in a private range (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) | `"10.0.0.5"` → `True` |

## License

MIT
