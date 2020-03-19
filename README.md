# Westworld Bingo

## Rules

1. Choose 20 "options" from the pool. Options are equivalent to squares on the bingo board.
2. Every episode, 15 of your options will be randomly chosen, and 9 options from the remaining pool will be chosen.
3. These 24 options will be shuffled to build your board. The center is free.
4. Throughout the episode, call out "options" as they occur in the show.
5. The winner is the one with the most points! Ties are broken by who had that number of points first. Harder ties will look at the history of points.
6. Games are decided by the end of the episode! If no one calls out an option, then it is ignored. To provide some leniency, we give 24h to add anything missed, but points earned this way are only worth half. Note: We may revisit this rule if it's too strict.
7. Points are awarded in the order they are called out. Not necessarily in the order it appears in the episode.
8. If you call out an option, and it is later refuted, you receive -1 point.
9. Point distribution: Each completion is worth 5 points. Unlike regular bingo which stops when there is a winner, we keep playing and continue to accumulate points. A pattern can be claimed by more than one player. We consider these 8 patterns: https://i.pinimg.com/564x/f0/24/7d/f0247d6dd31023b9aa7f00c75c6a1834.jpg
10. Based on difficulty of the game, we may decide to give players more than one board, and to increase/decrease the available patterns. Any decision like this will be made before the episode start.


## Creating boards.

Creates random bingo boards.

```
$ python bingo.py --players ./players --options options.txt --seed 149 --chosen ./empty.txt

seed: 149

./players/dolores.txt (448179)
|  17 |   7 |  23 |  21 |   9 |
|  14 |  12 |   4 |   6 |  20 |
|   0 |  10 |  ⓦ  |  18 |  33 |
|   2 |  24 |  29 |   1 |  16 |
|   3 |   8 |   5 |  31 |  11 |

./players/charlotte.txt (443434)
|   7 |   4 |  18 |  14 |   8 |
|  13 |  23 |  29 |  32 |   3 |
|  22 |  21 |  ⓦ  |   6 |  15 |
|   1 |  31 |  33 |  16 |   9 |
|   5 |  28 |   2 |  12 |  20 |

./players/caleb.txt (970437)
|  15 |  23 |  18 |   2 |   8 |
|   7 |  14 |  24 |   5 |   1 |
|  12 |  19 |  ⓦ  |  13 |  26 |
|  30 |  33 |  16 |  11 |  28 |
|  17 |   4 |  31 |  10 |  27 |
```

Change the seed for new boards.

```
python bingo.py --players ./players --options options.txt --seed 150 --chosen ./empty.txt

seed: 150

./players/dolores.txt (448179)
|  33 |  28 |   8 |   1 |  17 |
|  19 |   3 |  27 |  26 |   2 |
|   9 |  13 |  ⓦ  |   7 |  16 |
|  15 |   4 |  21 |   6 |   0 |
|   5 |  22 |  20 |  29 |  23 |

./players/charlotte.txt (443434)
|   8 |  10 |  15 |  18 |   2 |
|  12 |  32 |  11 |  29 |   5 |
|  20 |   6 |  ⓦ  |  19 |  33 |
|   9 |  23 |   3 |   1 |  16 |
|   7 |  14 |  22 |   0 |  30 |

./players/caleb.txt (970437)
|  10 |  27 |  20 |  23 |   2 |
|  13 |  28 |  14 |  17 |  29 |
|   0 |  12 |  ⓦ  |   3 |  32 |
|  15 |   8 |  25 |  26 |  21 |
|  16 |   5 |  31 |  19 |  18 |
```

Fill out boards by changing the chosen flag.

```
$ python bingo.py --players ./players --options options.txt --seed 149 --chosen ./chosen/ep1.txt

seed: 149

./players/dolores.txt (448179)
|  17 |   7 |  23 |  21 |   9 |
|  14 |  12 |   X |   6 |  20 | Found: 4
|   0 |  10 |  ⓦ  |  18 |  33 |
|   2 |  24 |  29 |   1 |  16 |
|   X |   8 |   5 |  31 |  11 | Found: 3

./players/charlotte.txt (443434)
|   7 |   X |  18 |  14 |   8 | Found: 4
|  13 |  23 |  29 |  32 |   X | Found: 3
|  22 |  21 |  ⓦ  |   6 |  15 |
|   1 |  31 |  33 |  16 |   9 |
|   5 |  28 |   2 |  12 |  20 |

./players/caleb.txt (970437)
|  15 |  23 |  18 |   2 |   8 |
|   7 |  14 |  24 |   5 |   1 |
|  12 |  19 |  ⓦ  |  13 |  26 |
|  30 |  33 |  16 |  11 |  28 |
|  17 |   X |  31 |  10 |  27 | Found: 4
```
