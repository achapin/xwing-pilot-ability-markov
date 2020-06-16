# X Wing Pilot Ability Generator using Markov chains

Using this data set: https://github.com/guidokessels/xwing-data2

Place the python script in the "pilots" subfolder and run it with ```python3 xwing-markov.py```

It will generate a text file with all existing abilities, a JSON document containing the markov chain, and then 100 generated abilities in the command line response.

The results are unfortunately not really usable. It seems like word-level Markov is not a great approach for generating new types of these abilities. Maybe a grammar-based approach would be better.

## Examples:
> Before you may gain 1 [Charge] If you have the Activation or perform a [1 [Straight]] template instead of the [Lock] action

> You do at range 0-3

> After you may spend 1 [Focus] result to a friendly ship at range 0-2 defends if you may gain 1 bonus attack die

> Before a maneuver if the Decoyed condition to you may choose a primary attack if you may change 1 stress token then repairs 1 matching your [Single-Turret-Arc] at range 0-1 or perform a friendly ship at initiative value this round you defend [Critical-Hit] result to an attack dice you may choose a bonus primary attack against a damaged attacker

> You the defender cannot reroll 1 additional defense die

> At the Engagement Phase you may spend 1 [Critical-Hit] results for each enemy ship at range 0-3 is an attack if the enemy ship in your damage cards you may spend 1 additional die

> Friendly ships can perform an action

> While you have 2 [Hit] results