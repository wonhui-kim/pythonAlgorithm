def solution(edges):
    answer = []

    if len(edges) == 1:
        return [2, 0, 1, 0]

    max_node = max(sum(edges, []))

    adj = [[] for i in range(max_node + 1)]
    reverse_adj = [[] for i in range(max_node + 1)]

    for edge in edges:
        adj[edge[0]].append(edge[1])
        reverse_adj[edge[1]].append(edge[0])

    for node in range(max_node):
        if len(adj[node]) == 0:
            continue

        if len(adj[node]) == 1 and node == adj[node][0]:
            continue

        result = [node, 0, 0, 0]
        is_graph_valid = True
        all_node = []

        for i in range(len(adj[node])):
            # 도넛 그래프
            is_donut, all_donut = donut(node, adj[node][i], adj)

            # 막대 그래프
            is_bar, all_bar = bar(node, adj[node][i], adj, reverse_adj)

            # 8자 그래프
            is_eight, all_eight = eight(node, adj[node][i], adj)

            if is_donut:
                # 기존 노드와 현재 노드 중복 있을 경우
                overlap = False

                if len(set.intersection(set(all_node), set(all_donut))) > 0:
                    overlap = True

                if overlap:
                    is_graph_valid = False
                    break

                result[1] += 1
                all_node += all_donut

            if is_bar:
                overlap = False

                if len(set.intersection(set(all_node), set(all_bar))) > 0:
                    overlap = True

                if overlap:
                    is_graph_valid = False
                    break

                result[2] += 1
                all_node += all_bar

            if is_eight:
                overlap = False

                if len(set.intersection(set(all_node), set(all_eight))) > 0:
                    overlap = True

                if overlap:
                    is_graph_valid = False
                    break

                result[3] += 1
                all_node += list(set(all_eight))

            print(result)

            if not (is_donut or is_bar or is_eight):
                is_graph_valid = False
                break

        if is_graph_valid and (len(set(all_node)) == (len(adj) - 2)):
            return result

    return [0, 0, 0, 0]


def donut(special_node, node, adj):
    start_node = node
    visited = [False for i in range(len(adj) + 1)]
    all_node = [start_node]

    # 임의 노드 -> 현재 노드
    while visited[start_node] == False:
        visited[start_node] = True

        # 모든 연결 간선은 한개
        if len(adj[start_node]):
            # 정점과 연결되었다면 아님
            if adj[start_node][0] == special_node:
                return False, []

            start_node = adj[start_node][0]
            all_node.append(start_node)
        else:
            return False, []

    if start_node == node:
        return True, all_node

    return False, []


def bar(special_node, node, adj, reverse_adj):
    visited = [False for i in range(len(adj) + 1)]
    root = node

    # root 찾기
    while reverse_adj[root] and (not visited[root]):
        visited[root] = True

        if len(reverse_adj[root]) == 1:
            new_root = reverse_adj[root][0]

            # cycle 발생
            if visited[new_root] == True:
                return False, []
            elif new_root == special_node:
                break
        else:
            if len(reverse_adj[root]) == 2:
                first_node = reverse_adj[root][0]
                second_node = reverse_adj[root][1]

                if first_node == special_node or second_node == special_node:
                    new_root = second_node

                    if first_node != special_node:
                        new_root = first_node

                    # cycle 발생하여 막대 x
                    if visited[new_root] == True:
                        return False, []

                    root = new_root
                else:
                    return False, []
            else:
                return False, []

    visited = [False for i in range(len(adj) + 1)]
    start_node = root
    all_node = [start_node]

    while len(adj[start_node]) == 1 and not visited[root]:
        visited[root] = True

        if len(adj[start_node]) == 1:
            # 다시 본인 노드로 돌아가면 성립x
            if start_node != adj[start_node][0]:
                start_node = adj[start_node][0]
                all_node.append(start_node)
            else:
                return False, []

    return True, all_node


def eight(special_node, node, adj):
    visited = [False for i in range(len(adj) + 1)]
    middle_node = node

    while not visited[middle_node]:
        visited[middle_node] = True

        if len(adj[middle_node]) == 2:
            break
        elif len(adj[middle_node]) == 1:
            middle_node = adj[middle_node][0]
        else:
            return False, []

    # 중앙 노드 연결 노드가 2개 아닐 경우
    if len(adj[middle_node]) != 2:
        return False, []

    first_start = adj[middle_node][0]
    second_start = adj[middle_node][1]
    all_node = []

    for start in [first_start, second_start]:
        start_node = start
        visited = [False for i in range(len(adj) + 1)]

        while not visited[start_node]:
            all_node.append(start_node)
            visited[start_node] = True

            if len(adj[start_node]) == 1:
                start_node = adj[start_node][0]

        # 끝나는 지점에서 도착하지 않는 경우
        if start_node != middle_node:
            return False, []

    return True, all_node


# print(solution([[2,3], [4,3], [1,1], [2,1]]))
print(solution(
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],
     [11, 9], [3, 8], [2, 13]]))