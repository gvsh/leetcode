



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



def is_a_solution(a, data):
    return len(a) == data

def process_solution(a, data):
    print("{", end = "")
    for exists, elem in zip(a, range(1, data + 1)):
        if exists: print(elem, end = "")
    print("}", end = " ")

def construct_candidates(a, data):
    return [True, False]

def make_move():
    pass

def unmake_move():
    pass



def generate_subsets(n):
    backtrack([], n)

if __name__ == "__main__":
    generate_subsets(3)
    