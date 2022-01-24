from getPlayerStats import getPlayerStats

wk = 6
unique = False
s1 = 0.683
s2 = 0.954
s3 = 0.997


target = '[\'Matt Ryan (ATL)\', \'Mac Jones (NE)\', \'Teddy Bridgewater (DEN)\', \'Kirk Cousins (MIN)\', \'Sam Darnold (CAR)\', \'Taylor Heinicke (WAS)\']'
#target = '[\'Matt Ryan (ATL)\', \'Mac Jones (NE)\']'
excused = ["Kyler Murray (ARI)", "Patrick Mahomes II (KC)", "Jared Goff (DET)", "Tom Brady (TB)", "Jalen Hurts (PHI)", "Dak Prescott (DAL)", "Russell Wilson (SEA)", "Matthew Stafford (LAR)", "Lamar Jackson (BAL)", "Josh Allen (BUF)", "Aaron Rodgers (GB)"]

playerStats = getPlayerStats(wk)

if playerStats == None:
    quit()

def collectInfo(totals, totLen):
    writefile = open('stats\standarddeviation2.txt', 'w')
    writefile.write(str(('min:', totals[0][0], 'max:', totals[-1][0], '\n')))
    writefile.write(str(('median:', totals[int(totLen/2)][0], '\n')))
    writefile.write(str(('1st sigmas:', totals[int((1-s1)*totLen)][0], totals[int(s1*totLen)][0], '\n')))
    writefile.write(str(('2nd sigmas:', totals[int((1-s2)*totLen)][0], totals[int(s2*totLen)][0], '\n')))
    writefile.write(str(('3rd sigmas:', totals[int((1-s3)*totLen)][0], totals[int(s3*totLen)][0], '\n')))
    writefile.close()

    points = []
    for x in range(int(totLen/10000)):
        points.append(totals[x*10000][0])
    writefile = open('stats\curve2.txt', 'w')
    writefile.write(str(points))
    writefile.close()
    return()
		
def findCombos(checkedNames, week, curList, curTotal):
    totals = []
    for i in playerStats.keys():
        if ((i in checkedNames) and unique) or (i in excused) or ((playerStats[i][week][0]) == 0):
            continue
        else:
            if week < wk-1:	
                totals += (findCombos(checkedNames+[i], week+1, curList+[(i)], curTotal+float(playerStats[i][week][0])))
            else:
                totals.append([curTotal+float(playerStats[i][week][0]), curList+[(i)]])
    return(totals)

def findWorst():
    totals = findCombos([],0,[],0)
    totals.sort()
    totLen = len(totals)

    collectInfo(totals, totLen)

    y = 1
    for z in range(len(totals)):
        if str(totals[z][1]) == target:
            print('Target is the '+str(y)+' worst pick of '+str(totLen)+' permutations with points:', totals[z][0])
            return(y)
        else:
            y+=1         
    print('must not have found anything')


findWorst()