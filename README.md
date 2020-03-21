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

Found:
  0. Bernard's secret revealed.
  2. Host gets repaired.
  3. There's a flashback.
  7. A character gets redemption.
 10. Dolores turn a human into a host.
 11. Dolores hacks a machine (not another host).
 12. Dolores loses conciousness.
 13. Bernard switches personalities.
 14. Bernard resentfully fights someone.
 17. Charlotte pitches a business idea.
 19. Caleb takes a gig.
 21. Same scene plays out more than once.
 24. A human finds out another human is actually a host.
 27. A character has a fast wardrobe change.
 28. A character is seen in more than 3 outfits in one episode.
 29. Someone swims.
 30. A religious reference is made by a character (e.g. comparing hosts to higher beings).
 36. Scene from Park 3: Warworld.
 44. Francis's voice is heard.
 54. New gadget is introduced (such as the tool Ash used to prevent being tracked or the augmented reality glasses).
 55. A host drives a car or flying vehicle.
 56. A character references the special value of the Delos corporation.
 59. A human or host questions if a host is lying.
 60. Someone takes an implant (limbic sedative).
 61. There's fire.
 62. There's opera.
 63. A host talks about the "books".
 64. There's a callback to another sci-fi show: "I'm afraid I can't do that".
 65. There's a slow-mo aerial cinematic shot (a la Bladerunner).
 69. There's a hologram phone call.

caleb (918878)
|  52 |  34 |  66 |   X |   X | Found: 2 13
|  15 |   X |   X |   X |  16 | Found: 10 36 29
|  22 |   X |  ⓦ  |   9 |   X | Found: 24 11
|   X |  25 |  31 |  23 |   X | Found: 30 65
|  35 |   X |   X |   X |   X | Found: 14 21 17 12

Score = 0, You got lost in the maze!

charlotte (421870)
|   X |  49 |   X |   X |   X | Found: 3 12 36 2
|   9 |   X |   X |   X |  42 | Found: 54 21 0
|   X |  50 |  ⓦ  |   X |  35 | Found: 30 63
|  32 |  22 |  31 |   8 |   4 |
|   1 |  25 |  37 |   X |   X | Found: 65 24

Score = 0, You got lost in the maze!

dolores (908824)
|  31 |   X |  32 |  35 |   X | Found: 62 21
|   X |   8 |   1 |   X |  23 | Found: 65 64
|  58 |   X |  ⓦ  |   X |   9 | Found: 13 7
|   6 |  33 |  39 |   X |   X | Found: 12 24
|   X |   5 |   X |   4 |  25 | Found: 2 3

Score = 0, You got lost in the maze!
```
