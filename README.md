# SAT-solvers
Two Python apps which resolve SAT problem, one representing formulas as matrices and another one using Binary Decision Diagrams. Both programs check if there is an interpretation that satisfies a given formula.

Simple sat solver uses matrix representation for a formula, where lines of matrix represent clauses in the given formula (clauses are separated by the symbol '^' in formula). After obtaining the matrix, all possible combinations will be generated and the program will check if a combination satisfies the given formula.

BDD sat solver will also convert the given formula into a matrix and will convert by scrolling line by line the matrix into a Binary Decision Diagram. Also, the program will check if a leaf node has value 1.
