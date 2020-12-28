from datetime import datetime
from time import sleep, time
from argparse import ArgumentParser

from fritzconnection.lib.fritzhosts import FritzHosts

SLEEP_TIME = 60


def report_hosts():
    fh = FritzHosts(address=args.ip, password=args.password)
    hosts = fh.get_active_hosts()
    return sorted((host["name"] for host in hosts), key=str.lower)


def main():
    while True:
        t = datetime.now()

        filename = t.strftime("%Y-%m-%d") + ".csv"

        with open(filename, mode="a+") as f:
            hosts = report_hosts()
            active = ["{};{}\n".format(t, h) for h in hosts]
            f.writelines(active)

        sleep(SLEEP_TIME - time() % SLEEP_TIME)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--ip", required=True)
    parser.add_argument("--password", required=True)
    args = parser.parse_args()
    main()
