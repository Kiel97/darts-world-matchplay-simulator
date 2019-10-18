from argparse import ArgumentParser

from tournament import Tournament


def main():
    parser = ArgumentParser()
    parser.add_argument("--year", help="The year tournament took place.")
    parser.add_argument("--players", help="Amount of players competing, powers of 2 only excluding 1")
    args = parser.parse_args()

    if args.year:
        if args.players:
            tournament = Tournament(players=int(args.players), year=args.year)
        else:
            tournament = Tournament(year=args.year)
    else:
        if args.players:
            tournament = Tournament(players=int(args.players))
        else:
            tournament = Tournament()

    tournament.simulate()


if __name__ == "__main__":
    main()
