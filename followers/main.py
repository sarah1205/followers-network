import argparse

import matplotlib.pyplot as plt
import networkx as nx
import requests


def main():
    handle, depth = get_args()
    graph = nx.Graph()
    graph.add_node(handle)
    sizes = {}
    colors = {}
    graph_followers(graph, handle, depth, sizes, colors)
    nx.draw(graph, node_list=sizes.keys(),
            node_size=sizes.values(), node_color=colors.values())
    plt.savefig("followers.png")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('handle', help='GitHub Handle (string value)')
    parser.add_argument('depth', type=int, help='Graph Depth (int value)')
    args = parser.parse_args()
    return args.handle, args.depth


def graph_followers(graph, handle, depth, sizes={}, colors={}):
    if depth == 0:
        sizes[handle] = 1000
        if handle not in colors:
            colors[handle] = 'c'
        return
    uri = 'https://api.github.com/users/%s/followers' % handle
    response = requests.get(uri)
    depth -= 1
    followers = response.json()
    sizes[handle] = len(followers) * 1000
    if not colors:
        colors[handle] = 'y'
    elif handle not in colors:
        colors[handle] = 'c'
    for follower in followers:
        f_handle = follower.get('login')
        if f_handle in sizes:
            continue
        graph.add_node(f_handle)
        graph.add_edge(handle, f_handle)
        graph_followers(graph, f_handle, depth, sizes, colors)
