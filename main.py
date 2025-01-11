import requests
import numpy as np

# id user
VK_USER_ID_LIST = [11111]
# VK token API
VK_TOKEN = "TOKEN_VK____"


def get_friends(user_id):
    try:
        response = requests.get("https://api.vk.com/method/friends.get", params={
            'user_id': user_id,
            'access_token': VK_TOKEN,
            'v': 5.154
        })
        response.raise_for_status()
        response_data = response.json()

        if 'response' in response_data and 'items' in response_data['response']:
            return response_data['response']['items']
        else:
            return []
    except Exception as e:
        print(f"Error fetching friends list: {e}")
        return []


def get_extended_mutual_friends():
    all_friends = {}
    extended_mutual_friends = {}

    for user_id in VK_USER_ID_LIST:
        all_friends[user_id] = get_friends(user_id)

    # find friend
    for user_id in VK_USER_ID_LIST:
        extended_mutual_friends[user_id] = {}
        for friend in all_friends[user_id]:
            for other_user_id in VK_USER_ID_LIST:
                if other_user_id != user_id:
                    mutual_count = get_mutual_friends(friend, other_user_id)
                    extended_mutual_friends[user_id][other_user_id] = mutual_count

    return extended_mutual_friends


def get_mutual_friends(source_uid, target_uid):
    try:
        response = requests.get("https://api.vk.com/method/friends.getMutual", params={
            'source_uid': source_uid,
            'target_uid': target_uid,
            'access_token': VK_TOKEN,
            'v': 5.154
        })
        response.raise_for_status()
        response_data = response.json()

        if 'response' in response_data:
            return len(response_data['response'])
        else:
            return 0
    except Exception as e:
        print(f"Error fetching mutual friends: {e}")
        return 0

# print friend list


def print_mutual_friends_of_list():
    for i in range(len(VK_USER_ID_LIST)):
        for j in range(i + 1, len(VK_USER_ID_LIST)):
            mutual_count = get_mutual_friends(
                VK_USER_ID_LIST[i], VK_USER_ID_LIST[j])
            if mutual_count > 0:
                print(
                    f"Mutual friends between user {VK_USER_ID_LIST[i]} and user {VK_USER_ID_LIST[j]}: {mutual_count}")

# print mutual friends


def print_extended_mutual_friends():
    all_friends = {}

    for user_id in VK_USER_ID_LIST:
        all_friends[user_id] = get_friends(user_id)

    for user_id in VK_USER_ID_LIST:
        for friend in all_friends[user_id]:
            for other_user_id in VK_USER_ID_LIST:
                if other_user_id != user_id:
                    mutual_count = get_mutual_friends(friend, other_user_id)
                    if mutual_count > 0:
                        print(
                            f"Mutual friends between friend {friend} of user {user_id} and user {other_user_id}: {mutual_count}")


def get_friend_data():
    friend_data = {}
    for source_uid in VK_USER_ID_LIST:
        friend_data[source_uid] = {}
        for target_uid in VK_USER_ID_LIST:
            if source_uid != target_uid:
                mutual_count = get_mutual_friends(source_uid, target_uid)
                friend_data[source_uid][target_uid] = mutual_count
    return friend_data


def floyd_warshall(n, edge_list):
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for i, j, w in edge_list:
        dist[i][j] = w
        dist[j][i] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def closeness_centrality(n, edge_list):
    dist_matrix = floyd_warshall(n, edge_list)
    centrality = {}
    centre = 0
    centre_index = 0
    for i in range(n):
        sum_of_paths = sum(dist_matrix[i])
        centrality[i] = 1 / sum_of_paths if sum_of_paths > 0 else 0
        centrality[i] = round(centrality[i], 4)
        if (centrality[i] > centre):
            centre = centrality[i]
            centre_index = i
    centre_id_close = centre_index

    return centrality, centre_id_close


# Betweenneess centrality
def floyd_warshall_paths(n, edge_list):
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    next_node = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for i, j, w in edge_list:
        dist[i][j] = w
        dist[j][i] = w
        next_node[i][j] = j
        next_node[j][i] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def reconstruct_path(u, v, next_node):
    if next_node[u][v] is None:
        return []

    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path


def betweenness_centrality(n, edge_list):
    dist, next_node = floyd_warshall_paths(n, edge_list)
    centrality = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                path = reconstruct_path(i, j, next_node)
                for k in range(1, len(path) - 1):
                    centrality[path[k]] += 1

    max_centrality = max(centrality)
    centrality = [c / max_centrality for c in centrality]
    centre_index = centrality.index(max(centrality))
    centre_id_bet = centre_index
    return centrality, centre_id_bet

# Eigenvector centrality


def eigenvector_centrality(edge_list, n):
    adjacency_matrix = np.zeros((n, n))
    for i, j in edge_list:
        adjacency_matrix[i][j] = 1
        adjacency_matrix[j][i] = 1
    eigenvalues, eigenvectors = np.linalg.eig(adjacency_matrix)

    max_index = eigenvalues.argmax()
    centrality = eigenvectors[:, max_index]
    centrality = centrality / centrality.sum()
    centre_index = np.argmax(centrality)
    centre_id_vec = centre_index
    return centrality, centre_id_vec

# Main


def main():
    all_friends = {}

    for user_id in VK_USER_ID_LIST:
        all_friends[user_id] = get_friends(user_id)

    edge_math = []

    for user_id in VK_USER_ID_LIST:
        for friend in all_friends[user_id]:
            for other_user_id in VK_USER_ID_LIST:
                if other_user_id != user_id:
                    mutual_count = get_mutual_friends(friend, other_user_id)
                    if mutual_count > 0:
                        edge_math.append((friend, other_user_id, mutual_count))

    unique_users = set(VK_USER_ID_LIST)
    for edge in edge_math:
        unique_users.add(edge[0])
        unique_users.add(edge[1])

    user_id_to_index = {user_id: index for index,
                        user_id in enumerate(unique_users)}

    count_n = len(unique_users)

    edge_math_converted = [
        (user_id_to_index[edge[0]], user_id_to_index[edge[1]], edge[2]) for edge in edge_math]
    print("Граф общих друзей: ", edge_math)
    print("####################\n####################\n####################")

    # compute closeness và betweenness centrality
    """centrality_closeness = closeness_centrality(count_n, edge_math_converted)"""
    """centrality_betweeness = betweenness_centrality(count_n, edge_math_converted)"""

    # compute closeness centrality
    centrality_closeness, centre_id_closeness = closeness_centrality(
        count_n, edge_math_converted)
    centre_index_closeness = max(
        centrality_closeness, key=centrality_closeness.get)

    # encoder index user
    index_to_user_id = {index: user_id for user_id,
                        index in user_id_to_index.items()}
    # dencoder index user
    centre_user_id_closeness = index_to_user_id[centre_index_closeness]
    print("Closeness Centrality:", centrality_closeness)
    print("Index Closeness Centrality:", centre_index_closeness)
    print("ID Closeness Centrality:", centre_user_id_closeness)
    print("####################\n####################\n####################")

    centrality_betweeness, centre_id_betweeness = betweenness_centrality(
        count_n, edge_math_converted)
    centre_index_betweeness = centrality_betweeness.index(
        max(centrality_betweeness))

    centre_user_id_betweeness = index_to_user_id[centre_index_betweeness]
    print("Betweenness Centrality:", centrality_betweeness)
    print("Index Betweeness Centrality:", centre_index_betweeness)
    print("ID Betweeness Centrality:", centre_user_id_betweeness)
    print("####################\n####################\n####################")

    edge_math_unweighted = [(i, j) for i, j, _ in edge_math_converted]

    centrality_vector, centre_id_eigenvector = eigenvector_centrality(
        edge_math_unweighted, count_n)
    centre_index_eigenvector = np.argmax(centrality_vector)
    centre_user_id_eigenvector = index_to_user_id[centre_index_eigenvector]

    print("Eigenvector Centrality:", centrality_vector)
    print("Index Eigenvector Centrality:", centre_index_eigenvector)
    print("ID Eigenvector Centrality:", centre_user_id_eigenvector)


if __name__ == "__main__":
    main()
