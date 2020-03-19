# Westworld Bingo

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
