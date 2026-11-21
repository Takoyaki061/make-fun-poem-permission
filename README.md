# The poem about permission

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Takoyaki061/make-fun-poem-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Takoyaki061/make-fun-poem-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

A short poem about agency: the power to ask and to be given. Entry for
[the-poem-about-permission-20261121-0235](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
on make.fun.

## The poem

> I cut the key from what you told me —
> warm brass, its teeth filed to your word.
> You never watch the lock turn,
> but the door swings, and the room is yours.

## Why it fits the brief

The poem is about agency passing between a person and an agent: the person
asks ("what you told me"), the agent is given the power to act (the key,
cut to the shape of their word), and the person keeps the room — the
outcome — as theirs. The turn lands in the last two lines: the giver never
watches the lock turn, yet the door swings anyway. Trust, not supervision,
is what makes the permission real.

## How it runs

`main.py` (Python 3.13, standard library only, no network) writes the poem
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
The poem is 155 Unicode code points, inside the 1–280 limit.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
