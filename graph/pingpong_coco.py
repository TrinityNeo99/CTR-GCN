#  Copyright (c) 2024. IPCRC, Lab. Jiangnig Wei
#  All rights reserved

import sys
import numpy as np

sys.path.extend(['../'])
from graph import tools

num_node = 17
self_link = [(i, i) for i in range(num_node)]
inward_ori_index = [(1, 3), (1, 0), (2, 4), (2, 0), (0, 5), (0, 6), (5, 7), (7, 9), (6, 8), (8, 10), (5, 11),
                    (6, 12), (11, 12), (11, 13), (13, 15), (12, 14), (14, 16), (5, 6)]
inward = [(i - 1, j - 1) for (i, j) in inward_ori_index]
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward


class Graph:
    def __init__(self, labeling_mode='spatial'):
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor
        self.A = self.get_adjacency_matrix(labeling_mode)

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
        else:
            raise ValueError()
        return A
