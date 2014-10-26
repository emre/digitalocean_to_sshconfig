digitalocean_to_sshconfig
=========================

adds your droplets into your ssh config.

<img src="http://i.imgur.com/UB9qWU7.gif">

### installation

```bash
$ (sudo) pip install digitalocean_to_sshconfig
```

### usage
```bash
$ digitalocean_to_sshconfig
```

**force update on existing hostnames**

```bash
$ digitalocean_to_sshconfig --force-update=1
```

**set username for config entries -- default:root**
```bash
$ digitalocean_to_sshconfig --user=emre
```

