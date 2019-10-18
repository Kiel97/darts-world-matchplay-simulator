# Darts World Matchplay Simulator
Simple 1KO Tournament simulator prototype made with Python 3.6.8

This prototype is an imitation of PDC World Matchplay tournament.
32 players (16 seeds and 16 qualifiers) are taking part in 5-round competition.
Every seed plays one randomly chosen qualifier in first round. First one of pair reaching 10 legs levels up to round two.
To reach quarter final players have to win 13 legs in round two, semi final - 16 legs, final - 17 and to become Champion - 18 legs.
Check out `example.txt` to see example output of this tournament.

# How to simulate tournament?
Download it and then run main.py with Python 3+ like `python3 main.py`. You can also pass desired year with --year argument, like `python3 main.py --year 2020`. Or pass --players to choose amount of players competing. Powers of 2 are working fine excluding 1.
`python3 main.py --year 2020 --players 128`
