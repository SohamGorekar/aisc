books = {"B1": "Python", "B2": "AI", "B3": "DBMS", "B4": "Networks"}
members = ["Ravi", "Sita", "Amit"]
issued = {"B1": "Ravi", "B3": "Sita"}


def Book(b):
    return b in books


def Member(m):
    return m in members


def Issued(b, m):
    return issued.get(b) == m


def Available(b):
    return Book(b) and b not in issued


def CanIssue(m, b):
    return Member(m) and Available(b)


def issue(m, b):
    if CanIssue(m, b):
        issued[b] = m
        print(f"{b} ({books[b]}) issued to {m}")
    else:
        print(f"Cannot issue {b} to {m}")


print("FACTS")
print("Books   :", books)
print("Members :", members)
print("Issued  :", issued)
print("\nQUERIES")
print("Available(B2)       =", Available("B2"))
print("Issued(B1, Ravi)    =", Issued("B1", "Ravi"))
print("CanIssue(Amit, B2)  =", CanIssue("Amit", "B2"))
print("CanIssue(Amit, B1)  =", CanIssue("Amit", "B1"))
print("exists b : Available(b) =", any(Available(b) for b in books))
print("forall b : Available(b) =", all(Available(b) for b in books))
print("Books issued to Ravi    =", [b for b in books if Issued(b, "Ravi")])
print("\nACTIONS")
issue("Amit", "B2")
issue("Amit", "B1")
print("Available books now:", [books[b] for b in books if Available(b)])
