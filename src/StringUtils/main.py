import re
from typing import List, Union,DefaultDict,Tuple
import struct
'''
git pull                          # 1. get any changes from GitHub first
# ... edit your code ...
git status                        # 2. see what changed
git add .                         # 3. stage changes
git commit -m "Short description of what you did"   # 4. save locally
git push                          # 5. upload to GitHub
'''

def levenshtein(a,b):...
def lcs(a, b):...

class InvalidInput(TypeError):
    """Raised when the input is not a string or a list of strings."""
class InvalidCharError(Exception):
    def __init__(self,char):
        super().__init__(f"The character {self.char}does not exist in the string")
        self.char = char
def to_snake_case(string: Union[List[str], str]) -> str:
    """
    Description:
        Converts a given string or list of strings into a snake case string.
        Handles camelCase, PascalCase, spaces, hyphens and mixed separators.

    :param string:
        List[str] | str

    :return:
        str

    :raises InvalidInput:
        If the input is not a string or a list of strings.
    """
    if isinstance(string, list):
        if not all(isinstance(s, str) for s in string):
            raise InvalidInput("Input is not a string or list of strings")
        string = " ".join(string)
    elif not isinstance(string, str):
        raise InvalidInput("Input is not a string or list of strings")

    # Split acronym/word boundaries: "HTTPServer" -> "HTTP_Server"
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", string)
    # Split lower/digit-to-upper boundaries: "camelCase" -> "camel_Case"
    s = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s)
    # Replace any run of non-alphanumeric characters with one underscore
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)

    return s.strip("_").lower()

def to_camel_case(string:Union[List[str],str],type = "var"):
    if type == "class":
        pass
    if type == "var":
        pass

def to_kebab_case(string):...
def to_train_case(string):...
def to_lower_case(string):...
def to_upper_case(string):...
def title_case(string):...
def to_constant_case(string):...
def dot_case(string):...
def swap_case(string):...
def is_upper_case(string):...
def is_lower_case(string):...
def center_print(string):...
def pretty_print(string:Union[str,List[str]]) -> Union[str,List[str]]:
    """
    description:
        pretty printing for python

    :param string:
    :return:None
    """
    print("="*10)
    print(string)
    print("="*10)

def reverse(string):...
def rot13(string):...
def longest_word(string:str)->str:
    """
    description:
        Finds the longest word in the given string
    :param string:
    :return:
    """
    pattern = r"\w+"
    result = re.findall(pattern, string)
    filtered = [ len(i) for i in result]
    idx = filtered.index(max(filtered))
    longest_word = result[idx]
    return longest_word

def char_frequency(string:Union[str,List[str]],char) -> List[Tuple[str,int]]:
    """
    description: A function to find frequqncy of a character
    :param string:
    :param char:
    :return: a list of integers
    """
    if isinstance(string, str):
        if char not in string:
            raise InvalidCharError(char)
        counts = {}
        for i in string:
            count = 0
            for j in string:
                if i == j:
                    count += 1
            counts[i] = count
        counts = [ (key,value) for key,value in counts.items()]
        return counts

    if isinstance(string, list):
        if char not in string:
            raise InvalidCharError(char)
        print("Under Development, Sorry for the inconvenience :(")

def vowel_count(string):...
def similarity(string):...
def hamming_distance(string):...
def compare_versions(string):...

# Number systems and encodings
def to_binary(value:Union[str,int,float],contiguous=True)->str:
    """
    description: A function to convert int, float and str to binary strings
    :param value:
    :return: str
    """
    if isinstance(value, str):
        binary_out = ""
        for i in value:
            binary_out += f"{ord(i):08b}"
        return binary_out
    if isinstance(value, int):
        return f"{value:b}"
    if isinstance(value, float):
        packed = struct.pack("!f",value)
        integ = struct.unpack('!I',packed)[0]
        return f"{integ:32b}"

def from_binary(string):...
def to_hex(value:Union[str,int,float])->str:
    """
    description: A function to convert int, float and str to hex strings
    :param value:
    :return:
    """
    if isinstance(value, str):
        hex_out = value.encode('utf-8').hex(' ')
        return hex_out
    if isinstance(value, int):
        return hex(value)
    if isinstance(value, float):
        return hex(value)


def from_hex(string):...
def to_octal(string):...
def from_octal(string):...
def text_to_binary(string):...
def binary_to_text(string):...
def text_to_hex(string):...
def hex_to_text(string):...
def ascii_codes(s):...

# Networking
def is_valid_ipv4(string:str)->bool:
    """
    :param string:
    :return:
    """
    pattern = r"\d+"
    result = re.findall(pattern, string)
    try:
        result = [ int(i) for i in result]
        if all(0<=i<=255 for i in result):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e} value must be integer ")
def is_valid_ipv6(string):...
def is_private_ip(string):...

# Cs algorithms