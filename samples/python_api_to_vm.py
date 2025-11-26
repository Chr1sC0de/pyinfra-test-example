import os

from pyinfra.api import Config, Inventory, State
from pyinfra.api.connect import connect_all
from pyinfra.api.deploy import add_deploy
from pyinfra.api.facts import get_facts
from pyinfra.api.operations import run_ops
from pyinfra.facts.server import Os

import pyinfra_test_example

# Define your inventory (@local means execute on localhost using subprocess)
# https://docs.pyinfra.com/en/3.x/apidoc/pyinfra.api.inventory.html
inventory = Inventory(
    (
        [
            (
                f"@ssh/{os.environ['VM_IP_ADDRESS']}",
                {
                    "ssh_user": os.environ["VM_USER"],
                    "_sudo_password": os.environ["VM_PASSWORD"],
                },
            )
        ],
        {},
    )
)

# Define any config you need
# https://docs.pyinfra.com/en/3.x/apidoc/pyinfra.api.config.html
config = Config()

# Set up the state object
# https://docs.pyinfra.com/en/3.x/apidoc/pyinfra.api.state.html
state = State(inventory=inventory, config=config)

# Connect to all the hosts
connect_all(state)

# Start adding operations
result1 = add_deploy(
    state,
    pyinfra_test_example.main,
)

# And finally we run the ops
run_ops(state)


# We can also get facts for all the hosts
# https://docs.pyinfra.com/en/3.x/apidoc/pyinfra.api.facts.html
print(get_facts(state, Os))
