def papers(amount):
    papers = [200, 100, 50, 20, 10, 5, 1]
    result = []

    for paper in papers:
        count = amount // paper
        if count > 0:
            result.append(f"{count}x {paper} L.E.")
            amount -= count * paper

    return " + ".join(result)
amount = int(input("Enter the amount in Egyptian Pounds: "))
print(papers(amount))




