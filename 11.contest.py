# def solve_queries(queries):
#     multiset = set()
#     bitmask_sum_set = {0}

#     for query in queries:
#         query_type, value = query

#         if query_type == 1:
#             new_multiset = set()
#             for s in bitmask_sum_set:
#                 new_multiset.add(s + (1 << value))
#             bitmask_sum_set.update(new_multiset)
#         else:
#             if value in bitmask_sum_set:
#                 print("YES")
#             else:
#                 print("NO")

# # Input reading
# m = int(input())
# queries = [list(map(int, input().split())) for _ in range(m)]

# # Solve queries
# solve_queries(queries)



def solve_queries(queries):
    max_value = 2**29
    multiset = set()
    possible_sums = set([0])

    for query, value in queries:
        if query == 1:
            new = set()
            for s in possible_sums:
                new.add((s + (1 << value)) % max_value)
            possible_sums.update(new)
        else:
            if value in possible_sums:
                print("YES")
            else:
                print("NO")

m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]

solve_queries(queries)

