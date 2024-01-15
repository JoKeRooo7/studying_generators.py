from itertools import zip_longest


def fix_wiring(cables: list, sockets: list, plugs: list):
    return (f"plug {c} into {s} using {p}"
            if p else f"weld {c} to {s} without plug"
            for c, s, p in zip_longest(
                (cable for cable in cables if isinstance(cable, str)),
                (socket for socket in sockets if isinstance(socket, str)),
                (plug for plug in plugs if isinstance(plug, str)))
            if c and s)


def main() -> None:
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
    print(' ')
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]
    for c in fix_wiring(cables, sockets, plugs):
        print(c)


if __name__ == "__main__":
    main()
