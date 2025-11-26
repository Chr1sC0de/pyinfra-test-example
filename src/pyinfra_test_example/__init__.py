from pyinfra_test_example import inventories
from pyinfra_test_example.deploys import core

__all__ = ["inventories"]


def main():
    core.install()
