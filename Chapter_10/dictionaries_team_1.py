members = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer",
}

while True:
    name = input("Enter name(quit ends): ")
    if name.lower() == "quit":
        print()
        break
    role = input("Enter role:")
    
    members[name] = role
    print()

for name in sorted(members):
    print(f"{name:<8}{members[name]}")
    