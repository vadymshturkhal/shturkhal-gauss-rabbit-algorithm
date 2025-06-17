# shturkhal-gauss-rabbit-algorithm
Shturkhal-Gauss-Rabbit algorithm for solving Frobenius coin problem.

Shturkhal-Gauss-Rabbit algorithm v. 6 brief analysis:
    1. Time complexity is the (Frobenius number) * min(coefficients);
    2. Memory requirements of v. 6 is min(coefficients);

v. 6 updates:
    1. replaced try...except with get;
    2. replaced heap priority queue with Tim Sort priority queue;
    3. added congruences with (residues, Apery set, related zeros) as output;

Note:
    1. Algorithm is based on Shturkhal-Gauss-Rabbit graph linearization;
    2. Algorithm works with (coefficients set length) > 1 and gcd(coefficients set) = 1.
