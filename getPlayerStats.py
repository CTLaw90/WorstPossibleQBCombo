#helper function to read stats from text files and build a dict with each players weekly scores
def getPlayerStats(week):
    wk = week
    playerStats = {}

    for j in range(wk):
        #makes the data easier to be read
        try:
            tmpfile = "stats\wk"+str(j+1)+".txt"
        except:
            print("file for week", wk, "does not exist. Exiting.")
            return(None)
        wkStatsData = open(tmpfile, "r")
        wkStatsData = wkStatsData.read()
        wkStatsData = wkStatsData.replace("\"", "")
        wkStatsData = wkStatsData.split("\n")
        for i in range(len(wkStatsData)):
            wkStatsData[i] = wkStatsData[i].split(",")

        #this loop adds qbs to the dict. I'm taking an additional point from each qbs weekly score for each int, as our league had a 2pt penalty vs the 1 on the data
        for i in wkStatsData:
            if i[1] not in playerStats.keys():
                playerStats[i[1]] = []
                for k in range(wk):
                    playerStats[i[1]].append([0])
            playerStats[i[1]][j] = [float(i[15])-float(i[8])]
    #returns the constructed dict
    return(playerStats)