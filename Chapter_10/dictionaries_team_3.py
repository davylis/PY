members = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer",
}
while True:
    name = input("Enter name (quit ends): ")

    if name.lower() == "quit":
        break

    if name in members:
        print(f"{name} is a {members[name]}")
    else:
        print(f"{name} is not in the team")
    print()