## Shturkhal-Gauss-Rabbit algorithm description:
* Shturkhal-Gauss-Rabbit algorithm for solving Frobenius coin problem;
* Algorithm is based on Shturkhal-Gauss-Rabbit graph linearization method which is suitable for unbounded cases;
* Graph linearization method is based on never-go-back approach;
* Graph linearization method is based on never-go-further approach;

## Acknowledgments:
* Carl Friedrich Gauss;
* Witold Lipski;
* Timofey Khirianov;
* Valeriy Petukhov;
* Filipp Vecherovsky;
* Maxim Kammerer;
* Lev Abalkin;
* The Rabbit;

## Shturkhal-Gauss-Rabbit algorithm v. 6 brief analysis:
* Time complexity is the (Frobenius number) * (modulus);
* Memory requirements is (modulus);

## v. 6 updates:
* Replaced try...except with get;
* Replaced heap priority queue with Tim Sort priority queue;
* Added congruences with (residues, Apery set, related zeros) as output;

## Notes:
* Algorithm works with (coefficients set length) > 1 and gcd(coefficients set) = 1;
* Time complexity (Frobenius number) * (modulus) of the solving that NP-Hard problem in general is still not enough to get Clay;
* The Rabbit always find Hamiltonian Path of Apery set in Frobenius graph;

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
* Restricted Frobenius problem;
