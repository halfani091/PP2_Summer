"""
Practice 5 — Python RegEx Exercises (w3resource)
Упражнения 1–14
"""

import re

def header(n, title):
    print(f"\n{'='*55}")
    print(f"  Exercise {n}: {title}")
    print('='*55)

def check(pattern, test_strings):
    """Вспомогательная: проверяет список строк по паттерну."""
    for s in test_strings:
        m = re.search(pattern, s)
        status = "✅ Match" if m else "❌ No match"
        print(f"  {status}: '{s}'")



header(1, "'a' followed by zero or more 'b's  (ab*)")

pattern1 = r'ab*'
tests1 = ["a", "ab", "abb", "abbb", "ac", "b"]
check(pattern1, tests1)
# re.findall — все совпадения
sample = "ac ab abb abbb"
print(f"\n  re.findall(r'ab*', '{sample}') → {re.findall(pattern1, sample)}")



header(2, "'a' followed by 2 to 3 'b's  (ab{2,3})")

pattern2 = r'ab{2,3}'
tests2 = ["ab", "abb", "abbb", "abbbb", "a"]
check(pattern2, tests2)
print(f"\n  re.findall(r'ab{{2,3}}', 'ab abb abbb abbbb') → "
      f"{re.findall(pattern2, 'ab abb abbb abbbb')}")



header(3, "Sequences of lowercase letters joined with '_'")

pattern3 = r'^[a-z]+(_[a-z]+)*$'
tests3 = ["hello_world", "foo_bar_baz", "Hello_world",
          "hello__world", "hello_", "abc"]
for s in tests3:
    m = re.match(pattern3, s)
    print(f"  {'✅ Match' if m else '❌ No match'}: '{s}'")


text3 = "Valid: hello_world foo_bar, Invalid: Hello_world hello__w"
found3 = re.findall(r'\b[a-z]+(?:_[a-z]+)+\b', text3)
print(f"\n  re.findall из текста → {found3}")



header(4, "One uppercase letter followed by lowercase letters  ([A-Z][a-z]+)")

pattern4 = r'[A-Z][a-z]+'
text4 = "The Quick brown Fox Jumps over the Lazy Dog"
found4 = re.findall(pattern4, text4)
print(f"  Text: '{text4}'")
print(f"  re.findall → {found4}")

tests4 = ["Hello", "hEllo", "HELLO", "H", "Hi", "ABC"]
check(pattern4, tests4)



header(5, "'a' followed by anything, ending in 'b'  (a.*b)")

pattern5 = r'a.*b'
tests5 = ["aab", "a123b", "ab", "aXYZb", "b", "a", "abc"]
check(pattern5, tests5)



header(6, "Replace space, comma, or dot with ':'  (re.sub)")

pattern6 = r'[ ,.]'                      
strings6 = [
    "Hello World",
    "one,two,three",
    "end.of.sentence",
    "mixed, text. here now",
]
for s in strings6:
    result = re.sub(pattern6, ':', s)
    print(f"  '{s}'")
    print(f"   → '{result}'")



header(7, "snake_case → camelCase  (re.sub + lambda)")

def snake_to_camel(name: str) -> str:
    # Находим _x и заменяем на X (заглавную)
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), name)

snake_tests = ["hello_world", "foo_bar_baz", "get_user_name",
               "my_variable_name", "parse_receipt_data"]
for s in snake_tests:
    print(f"  '{s}' → '{snake_to_camel(s)}'")



header(8, "Split string at uppercase letters  (re.split)")

def split_at_uppercase(s: str) -> list:
    return re.split(r'(?=[A-Z])', s)

tests8 = ["CamelCaseString", "HelloWorldFoo", "MyVariableName", "ABCdef"]
for s in tests8:
    parts = [p for p in split_at_uppercase(s) if p]  
    print(f"  '{s}' → {parts}")


header(9, "Insert spaces between words starting with capitals  (re.sub)")

def insert_spaces(s: str) -> str:
    
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', s)

tests9 = ["CamelCaseString", "HelloWorld", "GetUserName",
          "ParseReceiptData", "myVariableHere"]
for s in tests9:
    print(f"  '{s}' → '{insert_spaces(s)}'")



header(10, "camelCase → snake_case  (re.sub)")

def camel_to_snake(name: str) -> str:
    # 1. Вставляем _ перед заглавной после строчной: helloWorld → hello_World
    s = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    # 2. Вставляем _ между последовательностью заглавных и строчной: XMLParser → XML_Parser
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
    return s.lower()

tests10 = ["camelCase", "CamelCaseString", "getUserName",
           "parseReceiptData", "XMLParser", "myHTTPSConnection"]
for s in tests10:
    print(f"  '{s}' → '{camel_to_snake(s)}'")



header(11, "Word at end of string (optional punctuation)  (\\b\\w+[.!?,;]*$)")

pattern11 = r'\b(\w+)[.!?,;]*$'
tests11 = ["Hello World", "The quick brown fox.",
           "Is this correct?", "Yes!", "End,", "   "]
for s in tests11:
    m = re.search(pattern11, s)
    if m:
        print(f"  ✅ Match: '{s}'  →  last word: '{m.group(1)}'")
    else:
        print(f"  ❌ No match: '{s}'")



header(12, "Word containing 'z'  (\\w*z\\w*)")

pattern12 = r'\b\w*z\w*\b'
texts12 = ["The pizza was amazing", "hello world", "buzz fizz pop",
           "zoo zebra", "no z here... wait"]
for t in texts12:
    found = re.findall(pattern12, t, re.IGNORECASE)
    print(f"  '{t}'")
    print(f"   → {found if found else 'No match'}")



header(13, "'z' not at start or end of word  (\\b\\w+z\\w+\\b)")

pattern13 = r'\b\w+z\w+\b'
texts13 = ["buzz", "pizza", "zoo", "fizz", "amazing", "zebra", "frozen"]
print("  (z должна быть в середине слова — не первая, не последняя)")
for word in texts13:
    m = re.search(pattern13, word)
    print(f"  {'✅' if m else '❌'} '{word}'")



header(14, "Only letters, digits, underscores  (^\\w+$)")

pattern14 = r'^\w+$'
tests14 = ["hello_World123", "hello world", "foo-bar",
           "Valid_123", "has space", "under_score", "has.dot"]
for s in tests14:
    m = re.match(pattern14, s)
    print(f"  {'✅ Valid' if m else '❌ Invalid'}: '{s}'")


print(f"\n{'='*55}")
print("  ✅ Все 14 упражнений выполнены!")
print('='*55)