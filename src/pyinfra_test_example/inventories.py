import os


def vm():
    return dict(
        app_servers=[
            (
                f"@ssh/{os.environ['VM_IP_ADDRESS']}",
                {
                    "ssh_user": os.environ["VM_USER"],
                    "_sudo_password": os.environ["VM_PASSWORD"],
                },
            )
        ]
    )


def podman():
    return dict(
        app_servers=[
            ("@podman/docker.io/library/ubuntu:25.04", {}),
        ]
    )
