from collections import deque

# ---------------------------------------------
# Function to check safety
# ---------------------------------------------
def is_safe(m_left, c_left):
    # Calculate right bank people
    m_right = 3 - m_left
    c_right = 3 - c_left

    # Unsafe if missionaries are outnumbered
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False

    return True


# ---------------------------------------------
# Generate all possible next states
# ---------------------------------------------
def get_next_states(state):
    """
    state = (missionaries_left, cannibals_left, boat_position)
    boat_position: 0 = left, 1 = right
    """
    m, c, boat = state
    moves = [(2,0), (0,2), (1,0), (0,1), (1,1)]
    next_states = []

    for m_move, c_move in moves:
        if boat == 0:  # Boat on LEFT bank
            new_m = m - m_move
            new_c = c - c_move
            new_boat = 1
        else:          # Boat on RIGHT bank
            new_m = m + m_move
            new_c = c + c_move
            new_boat = 0

        if 0 <= new_m <= 3 and 0 <= new_c <= 3:
            if is_safe(new_m, new_c):
                next_states.append((new_m, new_c, new_boat))

    return next_states


# ---------------------------------------------
# BFS Algorithm
# ---------------------------------------------
def bfs():
    start_state = (3, 3, 0)
    goal_state = (0, 0, 1)

    queue = deque()
    queue.append((start_state, []))
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        visited.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))

    return None


# ---------------------------------------------
# Run BFS and print solution
# ---------------------------------------------
solution = bfs()

print("Solution Path:\n")
for step in solution:
    print(step)
