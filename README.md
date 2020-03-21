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
|  31 |  17 |  44 |  22 |  55 |
|  18 |  21 |  10 |  23 |  43 |
|  50 |  34 |  ⓦ  |  19 |  12 |
|  32 |  64 |  16 |  24 |  69 |
|  45 |  13 |  71 |  37 |  63 |

charlotte (421870)
|  50 |  53 |  57 |  48 |   7 |
|  22 |  26 |   9 |  51 |  33 |
|  34 |  32 |  ⓦ  |   0 |  61 |
|   4 |  35 |  21 |   3 |   6 |
|  14 |  29 |   8 |  61 |  31 |

dolores (908824)
|  32 |   0 |  47 |  65 |  73 |
|  26 |  21 |  13 |  56 |  23 |
|  31 |   1 |  ⓦ  |  63 |  43 |
|  13 |  60 |  71 |  61 |  22 |
|  33 |  62 |  20 |  30 |  64 |
```

Change the seed for new boards.

```
python bingo.py --seed 150

seed: 150

caleb (918878)
|  67 |  33 |  56 |  24 |  13 |
|  66 |  11 |   2 |  16 |  22 |
|  23 |  41 |  ⓦ  |  15 |  68 |
|  25 |  50 |  17 |  31 |  35 |
|  34 |  69 |  28 |  18 |  12 |

charlotte (421870)
|   0 |   9 |  59 |  49 |  33 |
|  34 |   6 |   8 |   7 |   4 |
|  23 |   2 |  ⓦ  |  31 |  32 |
|   1 |  45 |  52 |  55 |  53 |
|  45 |  43 |  21 |  25 |  47 |

dolores (908824)
|  23 |  49 |  46 |  20 |  34 |
|  40 |   2 |  64 |  46 |  60 |
|  22 |  28 |  ⓦ  |  33 |  24 |
|  32 |  21 |  36 |  63 |  39 |
|  30 |   3 |  41 |   1 |  11 |
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
 20. There's a four-legged animal (dog, elephant, horse, buffalo, etc.).
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
|  31 |   X |   X |  22 |   X | Found: 17 44 55
|  18 |   X |   X |  23 |  43 | Found: 21 10
|  50 |  34 |  ⓦ  |   X |   X | Found: 19 12
|  32 |   X |  16 |   X |   X | Found: 64 24 69
|  45 |   X |  71 |  37 |   X | Found: 13 63

Score = 0, You got lost in the maze!

charlotte (421870)
|  50 |  53 |  57 |  48 |   X | Found: 7
|  22 |  26 |   9 |  51 |   X | Found: 33
|  34 |  32 |  ⓦ  |   X |   X | Found: 0 61
|   4 |  35 |   X |   X |   6 | Found: 21 3
|   X |   X |   8 |   X |  31 | Found: 14 29 61

Score = 0, You got lost in the maze!

dolores (908824)
|  32 |   X |  47 |   X |  73 | Found: 0 65
|  26 |   X |   X |   X |  23 | Found: 21 13 56
|  31 |   1 |  ⓦ  |   X |  43 | Found: 63
|   X |   X |  71 |   X |  22 | Found: 13 60 61
|   X |   X |   X |   X |   X | Found: 33 62 20 30 64

Score = 15, Found = ['column_4', 'inside_four_corners', 'row_5']
```
