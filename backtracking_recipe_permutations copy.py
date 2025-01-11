



# found all solutions yet?
finished = False 

def backtrack(a, data):
    
    if is_a_solution(a, data):
        process_solution(a, data)
    else:
        # candidates for next position
        candidate_list = construct_candidates(a, data)
        for candidate in candidate_list:
            make_move()
            backtrack(a + [candidate], data)
            unmake_move()
            # terminate early 
            if finished: return




def generate_permutations(n):
    backtrack([], n)

def is_a_solution(a, data):
    return len(a) == data

def process_solution(a, data):
    print(a, end = " ")

def construct_candidates(a, data):
    return set(range(1, data + 1)) - set(a)

def make_move():
    pass

def unmake_move():
    pass


generate_permutations(3)

