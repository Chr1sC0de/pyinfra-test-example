# README


## Deploy to a VM

```bash 
pyinfra pyinfra_test_example.inventories.ssh pyinfra_test_example.main
```

## Deploy to podman

```bash 
pyinfra pyinfra_test_example.inventories.podman pyinfra_test_example.main
```

## Podman restart the ssh container 

```bash
podman-compose down ubuntu-podman-ssh
podman-compose up --force-recreate -d ubuntu-podman-ssh
```
