def answer(l):
    # level 2, challenge 1
    # Finished in 22 min (tried many other things)
    l.sort(key=lambda s: [int(u) for u in s.split('.')])
    return l


if __name__ == "__main__":
    print(answer(["1.1.2", "1.0", "1.0.0", "1", "1.3.3", "1.0.12", "1.0.2"]))
