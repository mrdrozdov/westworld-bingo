# Westworld Bingo

## Rules

It's like Bingo except you accumulate your points. Simple!

*How is your board created?* Each player chooses 20 possible squares. Each time you play, your board will be randomly generated using this list (15 from your pool and 9 from the rest will be chosen). The middle square is always free.

*How do we handle ties?* If there's a tie, the person with the most squares filled wins. Otherwise, the person who earned the most squares earliest wins.

*Which patterns are concerned?* Use the 8 patterns from here: https://i.pinimg.com/564x/f0/24/7d/f0247d6dd31023b9aa7f00c75c6a1834.jpg

1. Full Row
2. Full Column
3. Diagonal
4. Poststamp (four in the top right corner)
5. Outside Four Corners
6. Inside Four Corners
7. Outside Diamond
8. Inside Diamond

Each is worth 5 points.


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
 33. Code appears on screen.
 36. Scene from Park 3: Warworld.
 44. Francis's voice is heard.
 54. New gadget is introduced (such as the tool Ash used to prevent being tracked or the augmented reality glasses).
 55. A host drives a car or flying vehicle.
 56. A character references the special value of the Delos corporation.
 58. A host makes a joke.
 59. A human or host questions if a host is lying.
 60. Someone takes an implant (limbic sedative).
 61. There's fire.
 62. There's opera.
 63. A host talks about the "books".
 64. There's a callback to another sci-fi show: "I'm afraid I can't do that".
 65. There's a slow-mo aerial cinematic shot (a la Bladerunner).
 66. There's a scene in an elevator.
 69. There's a hologram phone call.

caleb (918878)
|  52 |  34 |   X |   X |   X | Found: 66 2 13
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
|   X |   X |  ⓦ  |   X |   9 | Found: 58 13 7
|   6 |   X |  39 |   X |   X | Found: 33 12 24
|   X |   5 |   X |   4 |  25 | Found: 2 3

Score = 5, Found = ['ne_sw_diagonal']
```
