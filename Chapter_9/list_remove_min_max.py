def remove_min_max(a):
    if len(a) == 0:
        return
    min_v=min(a)
    a.remove(min_v)
    if len(a) == 0:
        return
    max_v = max(a)
    a.remove(max_v)

def main():
    a = [3, 1, 4, 1, 5]
    remove_min_max(a)
    print(a)
if __name__ == "__main__":
    main()