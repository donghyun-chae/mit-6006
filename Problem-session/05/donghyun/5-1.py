#!/usr/bin/env python3
#
# Problem 5-1. Graph Radius
# In any undirected graph G = (V, E), the eccentricity (u) of a vertex u ∈ V is the shortest distance to its
# farthest vertex v, i.e., (u) = max{δ(u, v) | v ∈ V }. The radius R(G) of an undirected graph G = (V, E)
# is the smallest eccentricity of any vertex, i.e., R(G) = min{(u) | u ∈ V }.
# (a) Given connected undirected graph G, describe an O(|V ||E|)-time algorithm to determine the
# radius of G.
# (b) Given connected undirected graph G, describe an O(|E|)-time algorithm to determine an upper
# bound R∗ on the radius of G, such that R(G) ≤ R∗ ≤ 2R(G).
#
#
# answer
# (a): Each vertex takes O(|V|+|E|) times for detemining its eccentricity. To determine the radius of G all vertices should be considered. So It takes O(|V|*|E|) time.
# (b): 1. 가장 먼 정점을 BFS통해 찾음(어디서 시작하든 가장 먼 정점을 찾기 위해) 2. 찾은 정점으로 부터 BFS를 통ㅇ해 가장 먼 정점을 새로 찾으면 그 거리가 지름 3. 그 값의 절반이 반지름.
