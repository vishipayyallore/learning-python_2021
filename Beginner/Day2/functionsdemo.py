
# 1. Accepts Nothing | Returns None
def greet():
    print("Hello Python")

# 2. Accepts data | Returns None
def greet_v2(name: str):
    print(f"Hello {name}")

# 3. Accepts Nothing | Returns Value
def greet_v3() -> str:
    return "Hello Python (V3)"

# 4. Accepts data | Returns Value
def greet_v4(name: str) -> str:
    return f"Hello {name} (V4)"

def main():
    results = greet()
    print(f"1. Results: {results}")

    results = greet_v2("Shiva")
    print(f"2. Results: {results}")

    results = greet_v3()
    print(f"3. Results: {results}")

    results = greet_v4("Rajesh Agarwal")
    print(f"4. Results: {results}")

# Program Execution Starts Here
main()
