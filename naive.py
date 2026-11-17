text = input("Enter text: ")
pattern = input("Enter pattern: ")

found = False

for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        print("Pattern found at index:", i)
        found = True

if not found:
    print("No match found.")
