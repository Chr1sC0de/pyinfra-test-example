from pyinfra.api import deploy
from pyinfra.operations import apt


@deploy("Install Core")
def install_core():
    apt.update(
        name="Update apt repositories",
    )
    apt.packages(
        name="Install fd",
        packages=["fd-find"],
    )


def main():
    install_core()
