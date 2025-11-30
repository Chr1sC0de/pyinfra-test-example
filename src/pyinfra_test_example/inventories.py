import os


def ssh():
    return dict(
        app_servers=[
            (
                f"@ssh/{os.environ['SSH_HOST']}",
                {
                    "ssh_user": os.environ["SSH_USER"],
                    "ssh_password": os.environ["SSH_PASSWORD"],
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
