
def list_comprehension(socres):
    print("=== List Comprehension Examples ===")
    high_scores = [num > 2000 for num in socres]
    print(f"{high_scores}")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    s = [("alice", 2000), ("charlie", 3000), ("diana", 4000)]
    scores = [2000, 3000, 4000]
    list_comprehension(scores)
