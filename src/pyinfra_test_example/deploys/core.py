from pyinfra import host
from pyinfra.api import deploy
from pyinfra.operations import apt


@deploy("Install Core Dependencies")
def install():
    apt.update(
        name="Update apt repositories",
        _sudo=host.name.startswith("@ssh"),
    )

    apt.packages(
        name="Install core dependencies",
        packages=[
            "git",
            "curl",
            "ca-certificates",
            "bat",
            "unzip",
            "ripgrep",
            "fd-find",
            "build-essential",
            "cmake",
            "gettext",
            "libtool",
            "libtool-bin",
            "pkg-config",
            "openssh-server",
            "python3",
            "python3-pip",
            "python3-venv",
            "sudo",
        ],
        _sudo=host.name.startswith("@ssh"),
    )

    # Upgrade all packages and remove unneeded transitive dependencies
    apt.upgrade(
        name="Upgrade apt packages and remove unneeded dependencies",
        auto_remove=True,
        _if=lambda: host.name.startswith("@podman"),
    )
