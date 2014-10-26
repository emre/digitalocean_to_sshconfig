import getpass
import argparse

import digitalocean

from clint.textui import puts, indent, colored

from storm.parsers.ssh_config_parser import ConfigParser as StormParser


def get_cli_args():

    parser = argparse.ArgumentParser(
        epilog='digitalocean droplets into your SSHconfig.'
    )

    parser.add_argument(
        "-f",
        "--force-update",
        help="overwrites the related hostname entry even if it's already in the ssh config.",
        default=0
    )

    parser.add_argument(
        "-u",
        "--user",
        help="default user for the config.",
        default="root",
    )

    args = parser.parse_args()

    return args


def host_exists(host, ssh_config):
    for line in ssh_config.config_data:
        if line.get("type") == "entry":
            if line.get("host") == host:
                return True
                break

    return False


def get_token():
    return getpass.getpass("enter your digitalocean API token:")


def get_droplets():
    digitalocean_api = digitalocean.Manager(token=get_token())
    droplets = digitalocean_api.get_all_droplets()

    return droplets


def get_info(droplet, ip, args):
    return "{0} => {1}{2}{3}".format(
        colored.green(droplet.name),
        colored.cyan(args.user),
        colored.cyan("@"),
        colored.cyan(ip)
    )


def main():
    args = get_cli_args()

    ssh_config = StormParser()
    ssh_config.load()

    droplets = get_droplets()
    ssh_config_changed = False

    for droplet in droplets:
        ip = droplet.networks["v4"][0]["ip_address"]

        if host_exists(droplet.name, ssh_config):
            if args.force_update:
                ssh_config.update_host(
                    droplet.name,
                    {"hostname": ip, "user": args.user}
                )

                with indent(2):
                    puts(get_info(droplet, ip, args))

                ssh_config_changed = True

        else:
            ssh_config.add_host(droplet.name, {"hostname": ip, "user": args.user})
            ssh_config_changed = True

            with indent(2):
                puts(get_info(droplet, ip, args))

    if ssh_config_changed:
        ssh_config.write_to_ssh_config()
    else:
        with indent(2):
            puts(colored.red("all droplets already exists in your ssh config. use --force-update=1 to update."))


if __name__ == '__main__':
    main()
