from collections import deque

def is_palindrom(text):
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    char_deque = deque(cleaned_text)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
        
    return True
assert is_palindrom("radar") == True
assert is_palindrom("level") == True
assert is_palindrom("A man, a plan, a canal Panama") == True
assert is_palindrom("Madam, I'm Adam") == True
assert is_palindrom("") == True
assert is_palindrom("a") == True
assert is_palindrom("12321") == True
    
assert is_palindrom("hello") == False
assert is_palindrom("race a car") == False
assert is_palindrom("python") == False
assert is_palindrom("12345") == False