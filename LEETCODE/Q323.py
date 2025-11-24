class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        # Output: 2
        # Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
        # Output: 1
        roots = list(range(n))
        for edge in edges:
            self._union(roots, edge)
        unique_graphs = set()
        for root in roots:
            unique_graphs.add(self._find(roots, root))
        return len(unique_graphs)

    def _find(self, roots: List[int], node: int) -> int: 
        """ return root of given node"""
        # base case
        if node != roots[node]:
            roots[node] = self._find(roots, roots[node])
        # recursive case
        return roots[node]
    def _union(self, roots: List[int], edge: List[int]):
        """ modify the roots array if edges arent already unionized, otherwise change parent node"""
        root_a = self._find(roots, edge[0])
        root_b = self._find(roots, edge[1])
        if root_a != root_b:
            roots[edge[1]] = root_a
    