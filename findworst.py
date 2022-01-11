wk = 6
playerStats = {}

for j in range(wk):
	tmpfile = "stats\wk"+str(j+1)+".txt"
	wkStatsData = open(tmpfile, "r")
	wkStatsData = wkStatsData.read()
	wkStatsData = wkStatsData.replace("\"", "")
	wkStatsData = wkStatsData.split("\n")
	for i in range(len(wkStatsData)):
		wkStatsData[i] = wkStatsData[i].split(",")

	for i in wkStatsData:
		if i[1] not in playerStats.keys():
			playerStats[i[1]] = [i[15]]
		else:
			playerStats[i[1]].append(i[15])
		

excused = ["Kyler Murray (ARI)", "Patrick Mahomes II (KC)", "Jared Goff (DET)", "Tom Brady (TB)", "Jalen Hurts (PHI)", "Dak Prescott (DAL)", "Russell Wilson (SEA)", "Matthew Stafford (LAR)", "Lamar Jackson (BAL)", "Josh Allen (BUF)", "Aaron Rodgers (GB)"]
totals = []

def findWorst(checkedNames, week, curList, curTotal):
	global totals
	for i in playerStats.keys():
		if i in checkedNames or i in excused or float(playerStats[i][week]) <= 5:
			continue
		else:
			if week < wk-1:	
				findWorst(checkedNames+[i], week+1, curList+[(i)], curTotal+float(playerStats[i][week]))
			else:
				totals.append([curTotal+float(playerStats[i][week]), [curList+[(i)]]])
	
findWorst([],0,[],0)

totals.sort()

totLen = len(totals)

target = '[\'Matt Ryan (ATL)\', \'Mac Jones (NE)\', \'Teddy Bridgewater (DEN)\', \'Kirk Cousins (MIN)\', \'Sam Darnold (CAR)\', \'Taylor Heinicke (WAS)\']'

y = 1
for z in range(len(totals)):
    if str(totals[z][1][0]) == target:
        print('Target is the '+str(y)+' worst pick of '+str(totLen)+' permutations')
        quit()
    else:
        y+=1
        
print('must not have found anything')

# y = 1
# resultData = open("results.txt", "w")
# for x in totals:
    # resultData.write(str(y)+' - '+str(x)+'\n')
    # y += 1

# print('\n'+str(totals[0])+' is the worst possible combination\n')
# print('Complete, '+str(y)+' total permutations')
