# [AoC 2023](https://adventofcode.com/2023)

## [Day 1](https://adventofcode.com/2023/day/1) :star: :star:

Is it really only Day 1? This is a trickier than I remember.

Part 1 was trivial enough, if not inelegant -- basically iterated though the string, found all of the numbers and got out the first and last ones, as requested. 

I tried using a similar naive method for part 2, which was just Straight Up Bad News (process was promptly killed) so it had to be somewhat cleverer than that. After some googling, I found the regex library `re`. For each digit, it uses `finditer()` to get the indeces of each occurence. Then it takes the first and last index that was found. 

I'm pretty sure there's a better way to use `re` for this problem (iterating through the digits is unneccesary, right?), but I think learning regexes is a project for another day.

## [Day 2](https://adventofcode.com/2023/day/2) :star: :star:

Today was a pretty simple parsing and counting problem. The code speaks for itself, mostly. 

## [Day 3](https://adventofcode.com/2023/day/3)

## [Day 4](https://adventofcode.com/2023/day/4) :star:

## [Day 5](https://adventofcode.com/2023/day/5) :star:

This one started out quite fun, actually, but I haven't found the time to properly look at part 2. Part 1 went off smoothly with the help of a few hashmaps, but part 2 can't be solved the same way in any reasonable amount of time. I left the process running for an hour while I was cramming for exams, but no dice. Need to find a cleverer way to go about it, clearly. 

## [Day 6](https://adventofcode.com/2023/day/6) :star: :star:

This one is a math problem, isn't it? I see that other people did the algebra for this, which would have been smart, but I just wanted to get it done with and semi-brute-forced my way through it. 

It starts with holding the boat for 1 ms and increases the time until it finds the first time that will win the race (the `min_t`). It does the same thing from the max time, this time reducing the time until it finds the max number of milliseconds that will win the race. Get the difference. Done. 

## [Day 7](https://adventofcode.com/2023/day/7) :star: :star:

Today's problem seemed to involve a bit of sorting, and since I really need to be reviewing for my data structures exam, I thought I would try to implement a reasonable sorting algorithm for it. 

After a cursory glance it seemed like radix/bucket sort was the way to go. It took some time to get part 1 working (more code, more problems...), and part 2 creates a bit of a branching nightmare when determining the type of hand. I'm sure it can be refactored a bit more elegantly, but I think this is enough excitement for one day...
