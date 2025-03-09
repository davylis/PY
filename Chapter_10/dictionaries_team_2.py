members = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer",
}

member_names = []
for key in members:
    member_names.append(key)

print(' '.join(member_names))
member_names.sort()
print(' '.join(member_names))
