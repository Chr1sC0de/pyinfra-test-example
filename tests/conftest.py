import subprocess
import typing as tp
from collections.abc import Generator

import pytest
import testinfra
from pyinfra.api import Config, Inventory, State


@pytest.fixture(scope="function")
def podman_id(request) -> str:
    podman_id = (
        subprocess.check_output(
            ["podman", "run", "-dt", "docker.io/library/ubuntu:25.04"]
        )
        .decode()
        .strip()
    )
    return podman_id


@pytest.fixture(scope="function")
def host(podman_id: str) -> Generator[testinfra.host.Host]:
    try:
        yield testinfra.get_host("podman://" + podman_id)
    finally:
        subprocess.check_call(["podman", "rm", "-f", podman_id])


@pytest.fixture(scope="function")
def pyinfra_hosts(podman_id: str) -> tuple[list[tp.Any], dict]:
    return (
        [f"@podman/{podman_id}"],
        {},
    )


@pytest.fixture(scope="function")
def config():
    return Config()


@pytest.fixture(scope="function")
def inventory(pyinfra_hosts: tuple[list[tp.Any]]) -> Inventory:
    return Inventory(pyinfra_hosts)


@pytest.fixture(scope="function")
def state(inventory: Inventory, config: Config) -> State:
    return State(inventory=inventory, config=config)
