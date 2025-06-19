# shturkhal-gauss-rabbit-algorithm
Shturkhal-Gauss-Rabbit algorithm for solving Frobenius coin problem.

## Acknowledgments:
* Carl Friedrich Gauss;
* Witold Lipski;
* Timofey Khirianov;
* Valeriy Petukhov;
* Filipp Vecherovsky;

## Shturkhal-Gauss-Rabbit algorithm v. 6 brief analysis:
* Time complexity is the (Frobenius number) * (modulus);
* Memory requirements is (modulus);

## v. 6 updates:
* replaced try...except with get;
* replaced heap priority queue with Tim Sort priority queue;
* added congruences with (residues, Apery set, related zeros) as output;

## Notes:
* Algorithm is based on Shturkhal-Gauss-Rabbit graph linearization method;
* Algorithm works with (coefficients set length) > 1 and gcd(coefficients set) = 1;
* Time complexity (Frobenius number) * (modulus) of the solving that NP-Hard problem in general is still not enough to get Clay;

## Related problems:
* Knapsack;
* Shortest Path;
* Hamiltonian Path;
* Travelling Salesman;

## Frontiers:
* Linearization delay;
* C-based version;
* Linearization instead of backtracking for finding an arbitrary solution;
* Dijkstra vs Linearization in an arbitrary non-negative weights graph;
* Linearization for Frobenius function;
