# Create an empty set
s = set()

# Add elements into the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.remove(1)
s.add(1)
s.add(3) # No Element appears twice in a set
print(s)

print(f"The set has {len(s)} elements")