from random import randint

import pytest

from util.Node import Node


@pytest.fixture
def test_node():
    return Node()


@pytest.mark.parametrize("try_value, node_value", [
    (0, 0),
    (1, 1),
    (-1, -1),
    (100, 100),
    (-100, -100),
])
def test_init_value(test_node, try_value, node_value):
    test_node.add(try_value)
    assert test_node.value == node_value and test_node.left == None and test_node.right == None


@pytest.mark.parametrize("node_list, node_value, node_left_value", [
    ([2, 1], 2, 1),
    ([1, 0], 1, 0),
    ([0, -1], 0, -1),
    ([-1, -2], -1, -2),
    ([1, -1], 1, -1),
])
def test_add_left(test_node, node_list, node_value, node_left_value):
    for i in node_list:
        test_node.add(i)
    assert test_node.value == node_value and test_node.left.value == node_left_value and test_node.right == None


@pytest.mark.parametrize("node_list, node_value, node_right_value", [
    ([1, 2], 1, 2),
    ([0, 1], 0, 1),
    ([-1, 0], -1, 0),
    ([-2, -1], -2, -1),
    ([-1, 1], -1, 1),
])
def test_add_right(test_node, node_list, node_value, node_right_value):
    for i in node_list:
        test_node.add(i)
    assert test_node.value == node_value and test_node.left == None and test_node.right.value == node_right_value
