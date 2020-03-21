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
$ python bingo.py --seed 149

seed: 149

caleb (918878)
|  52 |  34 |  66 |   2 |  13 |
|  15 |  10 |  36 |  29 |  16 |
|  22 |  24 |  ⓦ  |   9 |  11 |
|  30 |  25 |  31 |  23 |  65 |
|  35 |  14 |  21 |  17 |  12 |

charlotte (421870)
|   3 |  49 |  12 |  36 |   2 |
|   9 |  54 |  21 |   0 |  42 |
|  30 |  50 |  ⓦ  |  63 |  35 |
|  32 |  22 |  31 |   8 |   4 |
|   1 |  25 |  37 |  65 |  24 |

dolores (908824)
|  31 |  62 |  32 |  35 |  21 |
|  65 |   8 |   1 |  64 |  23 |
|  58 |  13 |  ⓦ  |   7 |   9 |
|   6 |  33 |  39 |  12 |  24 |
|   2 |   5 |   3 |   4 |  25 |
```

Change the seed for new boards.

```
python bingo.py --seed 150

seed: 150

caleb (918878)
|  17 |  25 |  13 |  15 |  51 |
|  16 |   0 |  24 |  69 |  64 |
|  31 |  33 |  ⓦ  |  43 |  38 |
|  35 |  23 |  19 |  34 |  73 |
|  32 |  11 |  39 |  14 |   8 |

charlotte (421870)
|  37 |  13 |  32 |  35 |  25 |
|  24 |   0 |  34 |  28 |  23 |
|  31 |   9 |  ⓦ  |   8 |   5 |
|  33 |  58 |  27 |  22 |  62 |
|   7 |   6 |  16 |  69 |  38 |

dolores (908824)
|   7 |   4 |  65 |   8 |  36 |
|   5 |  64 |   1 |   0 |  70 |
|  35 |  44 |  ⓦ  |  23 |  33 |
|  34 |  38 |   3 |  32 |   2 |
|  69 |  62 |  24 |  31 |   6 |
```

Score boards by changing the chosen flag.

```
$ python bingo.py --seed 149 --chosen ./chosen/ep1.txt

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
