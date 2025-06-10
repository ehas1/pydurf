class PyDurf:
    
    # Mapping of characters to their builtin function string expressions
    CHAR_MAP = {
        'a': 'str(str)[len([[],[],[]])]',         # From "class"
        'b': 'str(len)[len([[]])]',               # From "built"
        'c': 'str(str)[len([[]])]',               # From "class"
        'e': 'str(type)[len([[],[],[],[],[],[],[],[],[],[],[]])]',  # From "type"
        'f': 'str(len)[len([[],[],[],[],[],[],[],[],[],[]])]',      # From "function"
        'h': 'str(hash)[len([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])]',  # From "hash"
        'i': 'str(len)[len([[],[],[]])]',         # From "built-in"
        'l': 'str(len)[len([[],[],[],[]])]',      # From "built-in"
        'n': 'str(len)[len([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])]',  # From "function"
        'o': 'str(bool)[len([[],[],[],[],[],[],[],[],[]])]',  # From "bool"
        'p': 'str(repr)[len([[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]])]',  # From "repr"
        'r': 'str(str)[len([[],[],[],[],[],[],[],[],[],[]])]',  # From "str"
        's': 'str(str)[len([[],[],[],[]])]',      # From "class"
        't': 'str(str)[len([[],[],[],[],[],[],[],[],[]])]',   # From "str"
        'u': 'str(len)[len([[],[]])]',            # From "built"
        'y': 'str(type)[len([[],[],[],[],[],[],[],[],[]])]'   # From "type"
    }

    @staticmethod
    def get_digit(n: int) -> str:
        """
        Generate a number using only len() and list operations.
        
        Args:
            n (int): The number to generate (>= 0)
            
        Returns:
            str: Python expression that evaluates to n
            
        Examples:
            >>> PyDurf.get_digit(0)
            'len([])'
            >>> PyDurf.get_digit(1)
            'bool([])'
            >>> PyDurf.get_digit(2)
            'len([[],[]]])'
        """
        if n < 0:
            raise ValueError("Cannot generate negative numbers")
        
        if n == 0:
            return 'len([])'
        elif n == 1:
            return 'bool([])'
        else:
            empty_lists = '[],' * n
            return f'len([{empty_lists[:-1]}])'  # Remove trailing comma

    @classmethod
    def encode(cls, text: str) -> str:
        """
        Basic encoding: Convert text to PyDurf code using only 8 characters.
        
        Uses chr() with len()-based number generation. This method is more
        verbose but uses the minimum possible character set.
        
        Args:
            text (str): Text to encode
            
        Returns:
            str: PyDurf expression that evaluates to the input text
            
        Example:
            >>> PyDurf.encode("hi")
            'chr(len([[...72 lists...]]))+chr(len([[...105 lists...]]))'
        """
        parts = []
        for c in text:
            parts.append(f'chr({cls.get_digit(ord(c))})')
        return '+'.join(parts)

    @classmethod
    def encode_advanced(cls, text: str) -> str:
        """
        Advanced encoding: Convert text using builtin function string extraction.
        
        Uses 20 unique characters but produces more concise code by extracting
        characters from builtin function string representations.
        
        Args:
            text (str): Text to encode
            
        Returns:
            str: PyDurf expression that evaluates to the input text
            
        Example:
            >>> PyDurf.encode_advanced("hi")
            'str(hash)[...]+str(len)[...]'
        """
        parts = []
        for c in text.lower():  # Convert to lowercase since our map only has lowercase
            if c in cls.CHAR_MAP:
                parts.append(cls.CHAR_MAP[c])
            else:
                # Fall back to basic encoding for characters not in our map
                parts.append(f'chr({cls.get_digit(ord(c))})')
        return '+'.join(parts)


def demo():
    """Run a demonstration of PyDurf encoding methods."""
    test_cases = ["Hello", "Python", "1234", "!@#$"]
    
    print("PyDurf Encoding Demonstration")
    print("=" * 50)
    
    for text in test_cases:
        print(f"\nEncoding: {text!r}")
        print("\nBasic encoding (8 chars):")
        basic = PyDurf.encode(text)
        print(f"Code: {basic}")
        print(f"Result: {eval(basic)!r}")
        
        print("\nAdvanced encoding (20 chars):")
        advanced = PyDurf.encode_advanced(text)
        print(f"Code: {advanced}")
        print(f"Result: {eval(advanced)!r}")


if __name__ == "__main__":
    demo() 