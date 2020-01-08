import networkx as nx
from nets_reqs_init import *
import copy


def test_graph(G, nodes):
    G.nodes[nodes]['IT_RESOURCE'] = 0
    y = 1
    return y


def copy_test(alist):
    z = copy.deepcopy(alist)
    z[0] += 10


if  __name__=='__main__':
    test_value = test_graph(DiNSF, 10)
    print(DiNSF.nodes[10]['IT_RESOURCE'])
    # test copy function and the variable scope of a function
    l1 = [i for i in range(3)]
    copy_test(l1)
    print(l1)