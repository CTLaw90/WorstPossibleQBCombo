# WorstPossibleQBCombo
Just how bad were my first 6 weeks of fantasy qb selection? Lets find out!

## Introduction
This year (2021) was my first year participating in a NFL fanatsy leauge. I have only vaguely paid attention to the NFL in the past so going into this year I had a lot of figuring out to do. I prioritized basically everything except a QB during the draft and grabbed a handful of mid-tier QBs... 
I ended up rotating through a good number of QBs through the early part of the season.... each week electing to pick someone new in hopes that they would bring greater fortune. By week 3 rumors of a curse had begun. By week 5 it seemed all but assured. People were reaching out to me to start their NFL teams opponents in hopes it would bring their team victory.
After another upsetting week 6, I decided I needed to know how bad my choices were. Surely something magical has happened. How could someone, actually trying quite hard to pick correctly, pick so bad so consistantly? By this week I had played 6 different QBs. 5 weeks had been each QBs worst week so far and the last week was only that QBs second worst week...

I deceided I needed some numbers to illustrate just how bad I had been so far. So I wrote some code!

## My Team
Before diving into the code, here is the team I ran for the first 6 weeks and the points they accrued:

1)Matt Ryan - 7.36pts&emsp;&emsp;ESPN Projected - 16.5

2)Mac Jones - 7.44pts&emsp;&emsp;ESPN Projected - 16.3

3)Teddy Bridgewater - 11.8pts&emsp;&emsp;ESPN Projected - 18.1

4)Kirk Cousins - 10.12pts&emsp;&emsp;ESPN Projected - 17.8

5)Sam Darnold - 6.08pts&emsp;&emsp;ESPN Projected - 19.2

6)Taylor Heineke - 9.28pts&emsp;&emsp;ESPN rojected - 20.3

Total accrued QB pts through week6 - 52.16
An average of 8.69 per week

## The Code
Ok to prefece this a bit my code was written in haste. I had been working long hours during this time and I know this can be refined. But this worked for a quick answer. A couple of things:
- I ignored any QB that one of the other teams in the league had rostered to start. For these first 6 weeks all 11 other teams used the same 11 starting QBs, so excused are the names to be removed from consideration
- I ignored QBs that ended with less than 5 points. This was a quick method to remove from consideration any QB that I would likely never select. The data sheet I am using contains the names of all 128 1st-4th string QB for each team. Obviously there are many on here I do not need to waste time looking at, but I dont want to completely ignore the possibility of picking a dark horse. This way is much quicker than going week by week and picking QBs I would have possible considered.
- I only considered unique combinations of QBs, not allowing combinations of QBs throughout weeks.

I downloaded data for the total points per QB from a website week by week. The code first imports these files and creates a dict to store the data by player name (playerStats).

The main function of the script is findWorst, which recursevly calls itself to iterate through the weeks and search for the worst possible combination. The totals are added to a list (totals) when it reaches the target number of weeks.

The list totals is then sorted using .sort() to oranize them by ascending point totals.

The final loop searches totals for our target combination (target) and returns the index of where in the list that item exists compared to the total length of the totals list. This lets us know where our selection ranks.

## Result
Based on the code, my selection was the 91,906th worst possible combination of a total 49,850,590 total possible selections.
This puts it as a top (or bottom) ~0.2% of worst possible picks.

Remarkable.

## Analysis
There are obviously a number of issues with the code. First and foremost, the runtime. It is abysmally slow. I am certain using a tree and a tree-seacrh can give much better than O(qbs^wks). Greater fidelity with regards to QB selection could also speed things up a bit.

It is not pretty. In reality, it should be structured into a class and allowed to be called by passing it just a couple of arguments such as the team... Not just have the searched for argument hardcoded into itself.

The algoritm could sort itself as items are found preventing the need for the .sort() call after the totals are calculated. 

The point totals in the data I pulled from the web are slightly differnt than the point totals in the leauge i was in. Our league had a -2 int penalty vs the -1 pentalty present in the point totals in the data. This is impactful in a number of situations, most notibly Sam Darnolds wk 5 in which he through 3 ints. My end result would definitly be higher if these totals were included. The data also includes data rounding to the nearest tenth, rather than hundreth present on the ESPN data. 

## Final Thoughts
I picked bad. I used ESPN projected points as the biggest guidepost with who to pick each week. Some minor deviations based on matchups and input from r/fantasyfootball... Im willing to wager if I calculated the highest descreptancies between projected and actual points for the QBs available to me for the first 6 weeks, I would have the highest total making my selection technically the worst possible choice. Also as stated earlier, the weeks I had run Ryan, Jones, Cousins, Darnold, and Heineke had been their worst result within those 6 weeks, and Bridgewater only had 1 week that was worse than the one I had played him. The chances of me doing this alone are 0.0043%

My total points through the first 6 weeks was 52.16, averaging 8.69 per week. No QB that started the first 6 weeks put up fewer points than that. In fact the lowest point average any of the QBs I had started was Mac Jones who averaged 13.91 over the first 6 weeks. Only one other QB started all 6 games for a lower average, Ben Rothlisberger at 13.20 (who I had actually drafted...). If I had started any QB consecutively I would have done about 60% better than my jumping through QBs...

The season did not improve much after this. Our regular season concluded at wk14. After that week I had an aveage of 11pts per week for my QB role which is worse than the average of any QB who played 10 or more games. 

My ultimate take away for next season: Stick with one QB!

