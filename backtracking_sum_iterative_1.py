"""
    Reach (n) with jumps sizes in (coefficients) with min sum of them.
    Example:
        coefficients = [7, 5, 11]
        n = 229
        result = [0, 4, 19]

    Solve equations like ax + by + cz + etc. = n, 
        where (a, b, c, etc.) are coefficients,
        (x, y, z, etc.) are parameters to find.

    How it works?
        1. Check for solution using np.gcd;
        2. Remember coefficient original places;
        3. Create another list with sorted (coefficients);
        4. Try to find divisor of (c) among (coefficients)
        5. Solve congruences with mods as (coefficients);
        6. If found (divisor) and sum of absolute values of (coefficients) is greater or equal to that, then swap them;
        7. Place parameters according to (coefficients) original places using transitions table;
        8. Return parameters.

    Notes:
        1. len(coefficients) must be greater than 1;
        2. all numbers in (coefficients) must be positive;
        3. all numbers in (coefficients) must be unique.
"""


import numpy as np
from gcd_for_numpy_array import gcd_for_numpy_array


def jump_to_endpoint(jump_size, end, trace, coefficients_table) -> list:
    """
        => Jump from (start) to (end) with (jump_size);
        => Stop at the (end) or cross it once.
    """
    # print(f"{jump_size = }")
    difference = end - trace
    k = difference / jump_size

    # crucial
    if not float.is_integer(k):
        k += 1

    k = int(k)
    trace = trace + jump_size * k

    coefficients_table[jump_size] += k

    return trace


def back_trace(jump_size, trace, coefficients_table, graph, coefficients) -> list:
    """
        Delete last equal jumps from (trace) in place and return (trace).
        Also delete jumps before which was doing once
        and returned last deleted jump.
    """

    k = coefficients_table[jump_size]
    difference = k * jump_size
    trace = trace - difference
    coefficients_table[jump_size] = 0
    graph.pop()

    last_jump = graph[-1]
    coefficients_table[last_jump] -= 1
    trace -= last_jump

    if coefficients_table[last_jump] == 0:
        graph.pop()

    return trace, last_jump


def search_iteratively(coefficients: list, endpoint: int, transition_table: dict, coefficients_table: dict) -> dict:
    if len(coefficients) == 0:
        return []
    
    if endpoint < 0:
        return []
    
    if endpoint == 0:
        return []

    trace = 0
    graph = [0]  # 0 for avoid index error
    jump_size = coefficients.pop()
    
    n = 0
    while True:
        n += 1
        # jump as far as you can
        trace = jump_to_endpoint(jump_size, endpoint, trace, coefficients_table)
        # print(graph, coefficients, endpoint)

        if graph[-1] != jump_size:
            graph.append(jump_size)

        # print(trace, endpoint, graph, jump_size, coefficients_table, coefficients)

        # reached goal
        if trace == endpoint:
            # print(n)

            # for all combinations
            # print(trace)
            return coefficients_table

        # over jumped
        next_jump_size = transition_table[jump_size]

        if next_jump_size == 0:
            if len(coefficients) == 0:
                # print(trace, graph, coefficients_table)
                raise Exception("Problem is impossible.")

            trace, last_deleted_jump = back_trace(jump_size, trace, coefficients_table, graph, coefficients)

            jump_size = transition_table[last_deleted_jump]
        else:
            trace = trace - jump_size

            # get last larger jump size and remove it from trace
            coefficients_table[jump_size] -= 1

            if coefficients_table[jump_size] == 0:
                graph.pop()
    
            jump_size = next_jump_size

        if trace == 0:
            jump_size = coefficients.pop()
        
        # print(trace, graph, jump_size, coefficients_table, coefficients)

    return coefficients_table


def create_transition_table(sorted_coefficients) -> dict:
    transition_table = {}

    max_coefficient = sorted_coefficients[-1]

    for i in range(len(sorted_coefficients) - 1, 0, -1):
        key = sorted_coefficients[i]
        value = sorted_coefficients[i - 1]

        transition_table[key] = value

    # add least coefficient with value max_coefficient
    transition_table[value] = 0
    transition_table[0] = max_coefficient

    return transition_table


def create_coefficients_table(sorted_coefficients) -> dict:
    coefficients_table = {}

    for coefficient in sorted_coefficients:
        coefficients_table[coefficient] = 0

    return coefficients_table


def get_min_terms_to_endpoint(coefficients, endpoint: int):
    """
        Print all combinations of the (coefficients) sum of which gives the (endpoint).

        All (coefficients) must be non negative.
    """

    greatest_common_divisor = gcd_for_numpy_array(np.array(coefficients))
    if greatest_common_divisor != 1:
        raise Exception(f"Problem is impossible, {greatest_common_divisor = }")

    sorted_coefficients = sorted(coefficients)
    transition_table = create_transition_table(sorted_coefficients)
    coefficients_table = create_coefficients_table(sorted_coefficients)
    solution_with_least_terms = search_iteratively(sorted_coefficients, endpoint, transition_table, coefficients_table)
    compact_view = [solution_with_least_terms[coefficient] for coefficient in coefficients]
    
    return compact_view


if __name__ == "__main__":
    coefficients = [53, 59, 61, 52]
    c = 1655
    parameters = get_min_terms_to_endpoint(coefficients, c)
    print(parameters)
    coefficients = np.array(coefficients)
    parameters = np.array(parameters)
    print(np.dot(coefficients, parameters.T), c)
    print()


    # coefficients = [1153,1159,1161,1152]
    # hard = 664087  # 664085 too
    # parameters = get_min_terms_to_endpoint(coefficients, hard)
    # print(parameters)
    # coefficients = np.array(coefficients)
    # parameters = np.array(parameters)
    # print(np.dot(coefficients, parameters.T), hard)
    # print()


    # coefficients = [5, 7]
    # c = 30
    # parameters = get_min_terms_to_endpoint(coefficients, c)
    # print(parameters)
    # coefficients = np.array(coefficients)
    # parameters = np.array(parameters)
    # print(np.dot(coefficients, parameters.T), c)
    # print()


    # coefficients = [7, 5, 11]
    # c = 229
    # parameters = get_min_terms_to_endpoint(coefficients, c)
    # print(parameters)
    # coefficients = np.array(coefficients)
    # parameters = np.array(parameters)
    # print(np.dot(coefficients, parameters.T), c)
    # print()


    # coefficients = [16, 32, 101, 12421, 1242512, 35266, 555]
    # c = 42251124
    # parameters = get_min_terms_to_endpoint(coefficients, c)
    # print(parameters)
    # coefficients = np.array(coefficients)
    # parameters = np.array(parameters)
    # print(np.dot(coefficients, parameters.T), c)
    # print()


    # coefficients = [16, 32, 101, 12421, 1242512, 35266, 555]
    # c = 42251124233334
    # parameters = get_min_terms_to_endpoint(coefficients, c)
    # print(parameters)
    # coefficients = np.array(coefficients)
    # parameters = np.array(parameters)
    # print(np.dot(coefficients, parameters.T), c)
    # print()


    # coefficients = [19, 32, 101, 12421, 1242512, 35266, 555]
    # c = 422511244123
    # parameters = get_min_terms_to_endpoint(coefficients, c)
    # print(parameters)
    # coefficients = np.array(coefficients)
    # parameters = np.array(parameters)
    # print(np.dot(coefficients, parameters.T), c)
    # print()
