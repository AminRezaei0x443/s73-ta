from app.core.network import Network


def test_network():
    n = Network()
    n.add_node(1)
    n.add_node(0)
    n.add_node(1)
    n.add_node(1)
    n.add_node(3)
    n.add_node(2)
    print(n.topology())
    n.remove_node(3)
    print(n.topology())
