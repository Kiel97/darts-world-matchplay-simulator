from argparse import ArgumentParser

from tournament import Tournament


def main():
    parser = ArgumentParser()
    parser.add_argument("--year")
    args = parser.parse_args()

    if args.year:
        tournament = Tournament(year=args.year)
    else:
        tournament = Tournament()

    tournament.simulate()


if __name__ == "__main__":
    main()
