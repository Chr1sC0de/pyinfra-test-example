import os

app_servers = [
    (
        f"@ssh/{os.environ['VM_IP_ADDRESS']}",
        {
            "ssh_user": os.environ["VM_USER"],
            "_sudo_password": os.environ["VM_PASSWORD"],
        },
    )
]
