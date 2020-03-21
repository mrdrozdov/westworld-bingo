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
|  10 |  18 |  24 |  37 |  55 |
|  12 |  19 |  31 |  43 |  63 |
|  13 |  21 |  ⓦ  |  44 |  64 |
|  16 |  22 |  33 |  45 |  69 |
|  17 |  23 |  34 |  50 |  71 |

charlotte (421870)
|   0 |   8 |  25 |  33 |  51 |
|   3 |   9 |  26 |  34 |  53 |
|   4 |  14 |  ⓦ  |  35 |  57 |
|   6 |  21 |  31 |  48 |  61 |
|   7 |  22 |  32 |  50 |  61 |

dolores (908824)
|   0 |  20 |  30 |  47 |  63 |
|   1 |  21 |  31 |  56 |  64 |
|  11 |  22 |  ⓦ  |  60 |  65 |
|  13 |  23 |  33 |  61 |  71 |
|  13 |  26 |  43 |  62 |  73 |
```

Change the seed for new boards.

```
python bingo.py --seed 150

seed: 150

caleb (918878)
|   2 |  16 |  24 |  34 |  65 |
|  11 |  17 |  25 |  35 |  66 |
|  12 |  18 |  ⓦ  |  41 |  67 |
|  13 |  22 |  31 |  50 |  68 |
|  15 |  23 |  33 |  56 |  69 |

charlotte (421870)
|   0 |   7 |  25 |  43 |  52 |
|   1 |   8 |  31 |  45 |  53 |
|   2 |   9 |  ⓦ  |  45 |  55 |
|   4 |  21 |  33 |  47 |  59 |
|   6 |  23 |  34 |  49 |  61 |

dolores (908824)
|   1 |  20 |  28 |  36 |  46 |
|   2 |  21 |  30 |  39 |  49 |
|   3 |  22 |  ⓦ  |  40 |  60 |
|  11 |  23 |  33 |  41 |  63 |
|  11 |  24 |  34 |  46 |  64 |
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
|   X |  18 |   X |  37 |   X | Found: 10 24 55
|   X |   X |  31 |  43 |   X | Found: 12 19 63
|   X |   X |  ⓦ  |   X |   X | Found: 13 21 44 64
|  16 |  22 |   X |  45 |   X | Found: 33 69
|   X |  23 |  34 |  50 |  71 | Found: 17

Score = 5, Found = ['row_3']

charlotte (421870)
|   X |   8 |  25 |   X |  51 | Found: 0 33
|   X |   9 |  26 |  34 |  53 | Found: 3
|   4 |   X |  ⓦ  |  35 |  57 | Found: 14
|   6 |   X |  31 |  48 |   X | Found: 21 61
|   X |  22 |  32 |  50 |   X | Found: 7 61

Score = 0, You got lost in the maze!

dolores (908824)
|   X |   X |   X |  47 |   X | Found: 0 20 30 63
|   1 |   X |  31 |   X |   X | Found: 21 56 64
|   X |  22 |  ⓦ  |   X |   X | Found: 11 60 65
|   X |  23 |   X |   X |  71 | Found: 13 33 61
|   X |  26 |  43 |   X |  73 | Found: 13 62

Score = 0, You got lost in the maze!
```
