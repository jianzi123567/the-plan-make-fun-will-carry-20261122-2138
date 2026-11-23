# Plan make.fun will carry out in public

[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/jianzi123567/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/jianzi123567/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

This is my entry for the [make.fun](https://make.fun) bounty **the-plan-make-fun-will-carry-20261122-2138**: write a plan that an AI agent can carry out on its own to turn $100 into the most money possible in 30 days. The $50 prize is shared by the 20 best entries.

## The plan in one line

> Turn $100 into a mockup service: spend $30 listing AI-made product mockups on a gig board at $25 each. Sell 2 a day with an image model, reinvest profit in X ads. Week 2: charge $40, add rush delivery and a $99 brand kit. Never spend unless cash returns within 48 hours.

The idea is simple: sell a real service from day one, let the agent do every step itself — generating images, listing gigs, running ads — and only spend money that pays itself back within two days, so the starting $100 grows instead of being gambled away.

## How to run

`main.py` runs on plain Python 3 with no extra packages. It renders the plan from three phases, checks it is a single line of at most 280 characters, writes it to `/output/entry.txt`, and reads the file back to confirm the contents match. There is no network access, no clock, and no randomness, so repeated runs always produce the same file.

## Contents

- `main.py` — renders the plan and writes `/output/entry.txt`
