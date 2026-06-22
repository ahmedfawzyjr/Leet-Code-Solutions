from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def sortItems(
        self,
        n: int,
        m: int,
        group: List[int],
        beforeItems: List[List[int]],
    ) -> List[int]:
        # Assign a unique group id to items that don't belong to any group.
        group_id = [0] * n
        members = defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                gid = m + i
            else:
                gid = group[i]
            group_id[i] = gid
            members[gid].append(i)

        # Build item-level graph for dependencies inside the same group.
        same_group_adj = [[] for _ in range(n)]
        same_group_indegree = [0] * n
        for item in range(n):
            for prev in beforeItems[item]:
                if group_id[prev] == group_id[item]:
                    same_group_adj[prev].append(item)
                    same_group_indegree[item] += 1

        # Topologically sort items inside each group.
        within_group_order = {}
        for gid, items in members.items():
            indegree = {item: same_group_indegree[item] for item in items}
            adj = {item: [] for item in items}
            for item in items:
                for nxt in same_group_adj[item]:
                    if group_id[nxt] == gid:
                        adj[item].append(nxt)

            heap = []
            for item in items:
                if indegree[item] == 0:
                    heappush(heap, item)

            order = []
            while heap:
                item = heappop(heap)
                order.append(item)
                for nxt in adj[item]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        heappush(heap, nxt)

            if len(order) != len(items):
                return []
            within_group_order[gid] = order

        # Build group-level graph for inter-group dependencies.
        group_adj = defaultdict(list)
        group_indegree = {gid: 0 for gid in members}
        group_edges = set()
        for item in range(n):
            for prev in beforeItems[item]:
                g1 = group_id[prev]
                g2 = group_id[item]
                if g1 != g2:
                    group_edges.add((g1, g2))

        for g1, g2 in group_edges:
            group_adj[g1].append(g2)
            group_indegree[g2] += 1

        # Topologically sort groups.
        heap = []
        for gid in members:
            if group_indegree[gid] == 0:
                heappush(heap, gid)

        result = []
        while heap:
            gid = heappop(heap)
            result.extend(within_group_order[gid])
            for nxt in group_adj[gid]:
                group_indegree[nxt] -= 1
                if group_indegree[nxt] == 0:
                    heappush(heap, nxt)

        return result if len(result) == n else []


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n1 = 8
    m1 = 2
    group1 = [-1, -1, 1, 0, 0, 1, 0, -1]
    before1 = [[], [6], [5], [6], [3, 6], [], [], []]
    print(solution.sortItems(n1, m1, group1, before1))

    # Example 2
    n2 = 8
    m2 = 2
    group2 = [-1, -1, 1, 0, 0, 1, 0, -1]
    before2 = [[], [6], [5], [6], [3], [], [4], []]
    print(solution.sortItems(n2, m2, group2, before2))
