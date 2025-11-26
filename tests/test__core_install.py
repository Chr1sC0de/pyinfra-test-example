import testinfra
from pyinfra.api import State
from pyinfra.api.connect import connect_all
from pyinfra.api.deploy import add_deploy
from pyinfra.api.facts import get_facts
from pyinfra.api.operations import run_ops
from pyinfra.facts.server import Os

import pyinfra_test_example


def test_my_pyinfra_deploy(state: State, host: testinfra.host.Host):
    # Connect to all the hosts
    connect_all(state)

    # Start adding operations
    add_deploy(
        state,
        pyinfra_test_example.main,
    )

    # And finally we run the ops
    run_ops(state)

    # We can also get facts for all the hosts
    # https://docs.pyinfra.com/en/3.x/apidoc/pyinfra.api.facts.html
    print(get_facts(state, Os))

    fdfind_install = host.find_command("fdfind")

    assert fdfind_install == "/usr/bin/fdfind"
