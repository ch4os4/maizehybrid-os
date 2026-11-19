# How I actually run the Bot, day to day

Not a spec doc. This is just how I plan to work with it.

Morning, I give it one job, not five. Like "today, finish the
seed lot QR page" or "fix the trial sync". I paste the Sanya
numbers in myself, I don't trust it to remember them. If it
starts drifting into other modules I tell it to stop and go
back to the one job.

Prompt-wise I keep it short. Context first: what crop, what
cross, what trial. Then the job. Then what done looks like:
tests pass, demo runs, no fake numbers. I learned the hard
way that long prompts just make it invent stuff.

Test failures: it has to show me the failing test, not just
say it fixed it. If a test fails twice on the same thing, I
make it stop and explain why in plain words before it tries
again. No silent retries.

Agronomic edge cases I care about: drought stress in a plot
means the yield number is not comparable, it has to flag it,
not average it in. Same with disease pressure, or germination
below 70%. If a plot is weird, mark it weird, don't smooth
it away. And Kazakhstan numbers are never mixed with Sanya
numbers, they stay separate until we have a full season.

Crons, the boring but real part:
- daily, sync offline trial captures from phones when they
  come back online
- weekly, recalc GCA/SCA from whatever trial data we actually
  have, and show the breakdown, not just a new yield number
- weekly, check seed lot stock vs distributor orders in
  Almaty / Shymkent / Turkistan, and flag anything low

If a cron fails it just logs it and tells me the next morning.
It doesn't retry forever and it doesn't invent data to fill
the gap.

That's it. One job a day, show the test, flag the weird plots,
don't mix trials.
