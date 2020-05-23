---
title: Dijkstra算法的简单python实现（附代码）
top: true
cover: false
toc: true
mathjax: true
date: 2020-05-19 18:43:00
password:
summary: 按照Dijkstra算法的思路用python实现了一下，用邻接矩阵表示点与点之间边的权重。刚接触Dijkstra算法，网上python实现的程序太过复杂因此没看，如果程序有错误欢迎指出。
tags:
- Dijkstra
- 算法
- python
categories:
- 算法
- python
---


## Dijkstra算法介绍：

[http://wiki.jikexueyuan.com/project/easy-learn-algorithm/dijkstra.html](http://wiki.jikexueyuan.com/project/easy-learn-algorithm/dijkstra.html)

按照Dijkstra算法的思路用python实现了一下，用邻接矩阵表示点与点之间边的权重。刚接触Dijkstra算法，网上python实现的程序太过复杂因此没看，如果程序有错误欢迎指出。

以下图为例：
![](https://img-blog.csdnimg.cn/20190321140749217.png)

他的邻接矩阵如下：
![](https://img-blog.csdnimg.cn/20190321141010935.png)

=>

```Python
Inf = float('inf')
Adjacent = [[0, 1, 12, Inf, Inf, Inf], 
            [Inf, 0, 9, 3, Inf, Inf], 
            [Inf, Inf, 0, Inf, 5, Inf], 
            [Inf, Inf, 4, 0, 13, 15], 
            [Inf, Inf, Inf, Inf, 0, 4], 
            [Inf, Inf, Inf, Inf, Inf, 0]]
Src, Dst, N = 0, 5, 6
```
 Src表示起点的编号，Dst表示终点的编号，N表示结点个数.
 
 Dijkstra算法实现:
 
```Python
def dijstra(adj, src, dst, n):
    dist = [Inf] * n
    dist[src] = 0
    book = [0] * n # 记录已经确定的顶点
    # 每次找到起点到该点的最短途径
    u = src
    for _ in range(n-1):    # 找n-1次
        book[u] = 1 # 已经确定
        # 更新距离并记录最小距离的结点
        next_u, minVal = None, float('inf')
        for v in range(n):    # w
            w = adj[u][v]
            if w == Inf:    # 结点u和v之间没有边
                continue
            if not book[v] and dist[u] + w < dist[v]: # 判断结点是否已经确定了，
                dist[v] = dist[u] + w
                if dist[v] < minVal:
                    next_u, minVal = v, dist[v]
        # 开始下一轮遍历
        u = next_u
    print(dist)
    return dist[dst]
```

dist为起点->每个结点的距离的列表。（所以起点要赋值为0:dist[src] = 0），而 book的作用是记录已经确定了最短距离的结点的列表。整体程序如下：

```Python
​

Inf = float('inf')
Adjacent = [[0, 1, 12, Inf, Inf, Inf],
            [Inf, 0, 9, 3, Inf, Inf],
            [Inf, Inf, 0, Inf, 5, Inf],
            [Inf, Inf, 4, 0, 13, 15],
            [Inf, Inf, Inf, Inf, 0, 4],
            [Inf, Inf, Inf, Inf, Inf, 0]]
Src, Dst, N = 0, 5, 6


def dijstra(adj, src, dst, n):
    dist = [Inf] * n
    dist[src] = 0
    book = [0] * n # 记录已经确定的顶点
    # 每次找到起点到该点的最短途径
    u = src
    for _ in range(n-1):    # 找n-1次
        book[u] = 1 # 已经确定
        # 更新距离并记录最小距离的结点
        next_u, minVal = None, float('inf')
        for v in range(n):    # w
            w = adj[u][v]
            if w == Inf:    # 结点u和v之间没有边
                continue
            if not book[v] and dist[u] + w < dist[v]: # 判断结点是否已经确定了，
                dist[v] = dist[u] + w
                if dist[v] < minVal:
                    next_u, minVal = v, dist[v]
        # 开始下一轮遍历
        u = next_u
    print(dist)
    return dist[dst]

dijstra(Adjacent, Src, Dst, N)
```

运行结果为：[0, 1, 8, 4, 13, 17]

