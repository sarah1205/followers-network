GitHub Follower Network Visualizer
================================

Visualize a GitHub followers network for a given handle and depth.

Install
=======

::

  sudo make init install

Use
===

::

  followers handle depth

  followers arnaudleg 3

Help
====

::

  usage: follower [-h] handle depth

  positional arguments:
    handle      GitHub Handle
    depth       Graph Depth

  optional arguments:
    -h, --help  show this help message and exit
  
Example
=======

![followers network](https://raw.github.com/arnaudleg/followers-network/master/examples/followers.png)
