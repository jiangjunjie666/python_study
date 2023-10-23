# 有一个不为你所知的秘密字符串。给出一个随机三个字母的组合的集合，恢复原来的字符串。
# 这里的三个字母的组合被定义为三个字母的序列，每个字母在给定的字符串中出现在下一个字母之前。"whi "是字符串 "whatisup "的一个三个字母的组合。
# 作为一种简化，你可以假设没有一个字母在秘密字符串中出现超过一次。
# 对于给你的三个字母的组合，除了它们是有效的三个字母的组合以及它们包含足够的信息来推导出原始字符串之外，你可以不做任何假设。特别是，这意味着秘密字符串永远不会包含不出现在给你的三个字母的组合中的字母。

def recoverSecret(triplets):
    # 创建一个字典用于表示字母之间的依赖关系
    graph = {}

    # 初始化图的数据结构
    for triplet in triplets:
        for char in triplet:
            if char not in graph:
                graph[char] = set()

    # 基于 triplets 构建图
    for triplet in triplets:
        graph[triplet[0]].add(triplet[1])
        graph[triplet[1]].add(triplet[2])

    # 执行拓扑排序
    def topological_sort(node, visited, result):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                topological_sort(neighbor, visited, result)
            result.insert(0, node)

    result = []
    visited = set()
    for node in graph:
        topological_sort(node, visited, result)

    return ''.join(result)


# 测试
triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

print(recoverSecret(triplets))  # 输出: "whatisup"
