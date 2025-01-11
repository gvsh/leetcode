

# found all solutions yet?
finished = False 
ans = []


def backtrack(a, first_num, n, k):
    
    if is_a_solution(a, n, k):
        process_solution(a, n, k)
    else:
        # candidates for next position
        candidate_list = construct_candidates(a, n, k)
        # for candidate1, candidate2 in zip(candidate_list, candidate_list[1:]):
        for candidate in candidate_list:
            # make_move(a, candidate)
            backtrack(a + [candidate], first_num , n, k)
            # unmake_move(a)
            # terminate early 
            if finished: return



def generate_combinations(n, k):
    backtrack([], 1, n, k)

def is_a_solution(a, n, k):
    return len(a) == k

def process_solution(a, n, k):
    ans.append(a)
    print(a, end = " ")

def construct_candidates(a, n, k):
    initial_set = set(range(1, n + 1)) - set(a)
    if a:
        max_val = max(a)
    else:
        max_val = -1

    return [elem for elem in initial_set if elem > max_val]

def make_move(a, candidate):
    a.append(candidate)

def unmake_move(a):
    a.pop()



generate_combinations(4, 2)

