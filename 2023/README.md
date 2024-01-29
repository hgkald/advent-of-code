# [AoC 2023](https://adventofcode.com/2023)

## [Day 15](https://adventofcode.com/2023/day/15) :star: :star:

I'm now done my exams! And still a few days behind. After skimming through the other problems, decided to do day 15 today, since part 1 at least seemed pretty straightforward. 

Part 2 wasn't exactly hard, but it was finicky, and I was hemming and hawing about which data structure to use. At first linked lists seemed like the obvious solution, but deletion and more importantly indexing had to be supported (or at least a way to find a certain value without having to traverse the whole list, because I had a feeling that would be a Bad Idea).

Eventually I ended up with a hashmap of arrays, where I stored the indexes of the items in the arrays in _another_ hashmap so they could be found easier. Deletions were just setting the array values to None so as not to mess up the indexing. I'm sure someone else has done this in like three lines in Haskell or something, but I am not one of those people...

Anyway, the point is that it works, so that's that for today. 


## [Day 9](https://adventofcode.com/2023/day/9) :star: :star:

When I saw this problem I thought immediately that it could be done with one recursive function, though I was wooly on the details. Even now, just after writing it, it still feels a bit wibbly-wobbly, timey-wimey. 

Once I got the first part done, the second part was pretty trivial (just switching some signs around basically). 

Because of some nasty winter flu and an exam I just wrote this morning (one more to go...), I actually completed this one on the 13th, so I'm a bit behind, but will see how much I can do for the rest of the month.

## [Day 8](https://adventofcode.com/2023/day/8) :star:

Another fairly straightforward one for part 1 and some kind of optimization problem (I think?) for part 2. I tried to do something fancy with node objects in part 1 in case there would be more complicated graph traversals for part 2, but the problem statement didn't change all that much. So I changed it to the simpler thing (an adjacency list as a dict). 

Currently part 2 seems to work on the small test case, but it's taking way too much time to run on the bigger test input.

## [Day 7](https://adventofcode.com/2023/day/7) :star: :star:

Today's problem seemed to involve a bit of sorting, and since I really need to be reviewing for my data structures exam, I thought I would try to implement one of the sorting algorithms we learned this semester. 

After a cursory glance it seemed like a radix/bucket sort was a reasonable way to go. It took some time to get part 1 working (more code, more problems...), and part 2 creates a bit of a branching nightmare when determining the type of hand. I'm sure it can be refactored a bit more elegantly, but I think this is enough excitement for one day...

## [Day 6](https://adventofcode.com/2023/day/6) :star: :star:

This one is a math problem, isn't it? I see that other people did the algebra for this, which would have been smart, but I just wanted to get it done with and semi-brute-forced my way through it. 

It starts with holding the boat for 1 ms and increases the time until it finds the first time that will win the race (the `min_t`). It does the same thing from the max time, this time reducing the time until it finds the max number of milliseconds that will win the race. Get the difference. Done. 

## [Day 5](https://adventofcode.com/2023/day/5) :star:

This one started out quite fun, actually, but I haven't found the time to properly look at part 2. Part 1 went off smoothly with the help of a few hashmaps, but part 2 can't be solved the same way in any reasonable amount of time. I left the process running for an hour while I was cramming for exams, but no dice. 

## [Day 4](https://adventofcode.com/2023/day/4) :star:

## [Day 3](https://adventofcode.com/2023/day/3)

## [Day 2](https://adventofcode.com/2023/day/2) :star: :star: 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Kotlin](https://img.shields.io/badge/Kotlin-0095D5?&style=for-the-badge&logo=kotlin&logoColor=white)

Today was a pretty straightforward parsing and counting problem. 

This is also the first time I've tried this in Kotlin, and I tried to do a more functional style instead of just copying the exact thing I did in Python. It's not perfect, but it works! 

## [Day 1](https://adventofcode.com/2023/day/1) :star: :star:

Is it really only Day 1? This is a trickier than I remember.

Part 1 was trivial enough, if not inelegant -- basically iterated though the string, found all of the numbers and got out the first and last ones, as requested. 

I tried using a similar naive method for part 2, which was just Straight Up Bad News (process was promptly killed) so it had to be somewhat cleverer than that. After some googling, I found the regex library `re`. For each digit, it uses `finditer()` to get the indeces of each occurence. Then it takes the first and last index that was found. 

I'm pretty sure there's a better way to use `re` for this problem (iterating through the digits is unneccesary, right?), but I think learning regexes is a project for another day.


