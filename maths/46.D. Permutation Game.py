t = int(input())

for _ in range(t):
    n, k, pb, ps = map(int, input().split())
    permutation = list(map(int, input().split()))
    scores = list(map(int, input().split()))

    pb -= 1  # Adjusting to 0-indexing
    ps -= 1

    bodya_score = scores[pb]
    sasha_score = scores[ps]

    for _ in range(k):
        pb = permutation[pb] - 1
        ps = permutation[ps] - 1
        bodya_score += scores[pb]
        sasha_score += scores[ps]

    if bodya_score > sasha_score:
        print("Bodya")
    elif bodya_score < sasha_score:
        print("Sasha")
    else:
        print("Draw")
