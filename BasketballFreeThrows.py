#Copyright: These datasets were prepared using publicly available data.
#           However, theses scripts are subject to Copyright Laws. 
#           If you wish to use these Python scripts outside of the Python Programming Course
#           by Kirill Eremenko, you may do so by referencing www.superdatascience.com in your work.

#Comments:
#Seasons are labeled based on the first year in the season
#E.g. the 2012-2013 season is preseneted as simply 2012

#Notes and Corrections to the data:
#Kevin Durant: 2006 - College Data Used
#Kevin Durant: 2005 - Proxied With 2006 Data
#Derrick Rose: 2012 - Did Not Play
#Derrick Rose: 2007 - College Data Used
#Derrick Rose: 2006 - Proxied With 2007 Data
#Derrick Rose: 2005 - Proxied With 2007 Data

import numpy as np 
import matplotlib.pyplot as plt

#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]

#Games 
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

#Free Throws
KobeBryant_FT = [696,667,623,483,439,483,381,525,18,196]
JoeJohnson_FT = [261,235,316,299,220,195,158,132,159,141]
LeBronJames_FT = [601,489,549,594,593,503,387,403,439,375]
CarmeloAnthony_FT = [573,459,464,371,508,507,295,425,459,189]
DwightHoward_FT = [356,390,529,504,483,546,281,355,349,143]
ChrisBosh_FT = [474,463,472,504,470,384,229,241,223,179]
ChrisPaul_FT = [394,292,332,455,161,337,260,286,295,289]
KevinDurant_FT = [209,209,391,452,756,594,431,679,703,146]
DerrickRose_FT = [146,146,146,197,259,476,194,0,27,152]
DwayneWade_FT = [629,432,354,590,534,494,235,308,189,284]
#Matrix 
FreeThrows = np.array([KobeBryant_FT,JoeJohnson_FT,LeBronJames_FT,CarmeloAnthony_FT,DwightHoward_FT,ChrisBosh_FT,ChrisPaul_FT,KevinDurant_FT, DerrickRose_FT,DwayneWade_FT])

#Free Throw Attempts
KobeBryant_FTA = [819,768,742,564,541,583,451,626,21,241]
JoeJohnson_FTA = [330,314,379,362,269,243,186,161,195,176]
LeBronJames_FTA = [814,701,771,762,773,663,502,535,585,528]
CarmeloAnthony_FTA = [709,568,590,468,612,605,367,512,541,237]
DwightHoward_FTA = [598,666,897,849,816,916,572,721,638,271]
ChrisBosh_FTA = [581,590,559,617,590,471,279,302,272,232]
ChrisPaul_FTA = [465,357,390,524,190,384,302,323,345,321]
KevinDurant_FTA = [256,256,448,524,840,675,501,750,805,171]
DerrickRose_FTA = [205,205,205,250,338,555,239,0,32,187]
DwayneWade_FTA = [803,535,467,771,702,652,297,425,258,370]
#Matrix
FreeThrowAttempts = np.array([KobeBryant_FTA, JoeJohnson_FTA,LeBronJames_FTA,CarmeloAnthony_FTA,DwightHoward_FTA,ChrisBosh_FTA,ChrisPaul_FTA,KevinDurant_FTA,DerrickRose_FTA,DwayneWade_FTA])

#Points
KobeBryant_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
JoeJohnson_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
LeBronJames_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
CarmeloAnthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
DwightHoward_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
ChrisBosh_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
ChrisPaul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
KevinDurant_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
DerrickRose_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
DwayneWade_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])

#Field Goals
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]
#Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])

get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.dpi'] = 125


def generateVisuals(data, title,indexes = Players, xaxis = Seasons):
    for i in range(0,len(indexes)):
        c= ["black","blue","red","green","yellow","orange","magenta","cyan","grey","pink"]
        m= [".","o","v","^","s","p","D","P","X","*"]
        plt.plot(data[i], c= c[i], ls = '--',marker=m[i], ms = 4, label=indexes[i])
    plt.xticks(list(range(0,len(xaxis))),xaxis, rotation='vertical')
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.suptitle(title)
    plt.show()



generateVisuals(FreeThrowAttempts / Games,"Free Throws Attempts per Game")


data = np.matrix.round(FreeThrows / FreeThrowAttempts,2)*100
generateVisuals(data,"Accuracy % of Free Throws")


PlayerStyles = Points - FreeThrows
data = PlayerStyles / FieldGoals
generateVisuals(data, "Player Style Preference")

