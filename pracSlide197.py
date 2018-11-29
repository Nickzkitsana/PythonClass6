import DicLibrary as DicL

def stat_point_goalID():
    DicL.line60()
    for i in range(len(premier_league_2017_2018)):
        sum = (premier_league_2017_2018[i]["W"] * 3) + (premier_league_2017_2018[i]["D"] * 1)
        gd = premier_league_2017_2018[i]["GF"] - premier_league_2017_2018[i]["GA"]
        print("{0:5} {1:25} Pts:{2:3}  GD:{3:3}".format(i+1,premier_league_2017_2018[i]["Team"].lower(),sum,gd))
        if i == 3:
            DicL.line60()
        if i == 16:
            DicL.line60()
        if i == 20:
            DicL.line60()

def stat_percentages():
    DicL.line80()
    print("                           Stat Percentages")
    DicL.line80()
    for i in range(len(premier_league_2017_2018)):
        win = (premier_league_2017_2018[i]["W"]*0.4)
        draw = (premier_league_2017_2018[i]["D"] * 0.4)
        lose = (premier_league_2017_2018[i]["L"] * 0.4)
        print("{0:5} {1:25} Win[{2:3.2f}%] Draw[{3:3.2f}%] Lose[{4:3.2f}%] ".format(i+1,premier_league_2017_2018[i]["Team"],win,draw,lose))
        if i == 3:
            DicL.line80()
        if i == 16:
            DicL.line80()
        if i == 20:
            DicL.line80()


premier_league_2017_2018 = [{"Pos":1,"Team":"Manchester City (C)","W":32,"D":4,"L":2,"GF":106,"GA":27},
                            {"Pos":2,"Team":"ManchesterUnited","W":25,"D":6,"L":7,"GF":68,"GA":28},
                            {"Pos":3,"Team":"TottenhamHotspur","W":23,"D":8,"L":7,"GF":74,"GA":36},
                            {"Pos":4,"Team":"Liverpool","W":21,"D":12,"L":5,"GF":84,"GA":38},
                            {"Pos":5,"Team":"Chelsea","W":21,"D":7,"L":10,"GF":62,"GA":38},
                            {"Pos":6,"Team":"Arsenal","W":19,"D":6,"L":13,"GF":74,"GA":51},
                            {"Pos":7,"Team":"Burnley","W":14,"D":12,"L":12,"GF":36,"GA":39},
                            {"Pos":8,"Team":"Everton","W":13,"D":10,"L":15,"GF":44,"GA":58},
                            {"Pos":9,"Team":"LeicesterCity","W":12,"D":11,"L":15,"GF":56,"GA":60},
                            {"Pos":10,"Team":"Newcastle United","W":12,"D":8,"L":18,"GF":39,"GA":47},
                            {"Pos":11,"Team":"CrystalPalace","W":11,"D":11,"L":16,"GF":45,"GA":55},
                            {"Pos":12,"Team":"Bournemouth","W":11,"D":11,"L":16,"GF":45,"GA":61},
                            {"Pos":13,"Team":"West HamUnited","W":10,"D":12,"L":16,"GF":48,"GA":68},
                            {"Pos":14,"Team":"Watford","W":11,"D":8,"L":19,"GF":44,"GA":64},
                            {"Pos":15,"Team":"Brighton & HoveAlbion","W":9,"D":13,"L":16,"GF":34,"GA":54},
                            {"Pos":16,"Team":"HuddersfieldTown","W":9,"D":10,"L":19,"GF":28,"GA":58},
                            {"Pos":17,"Team":"Southampton","W":7,"D":15,"L":16,"GF":37,"GA":56},
                            {"Pos":18,"Team":"Swansea City(R)","W":8,"D":9,"L":21,"GF":28,"GA":56},
                            {"Pos":19,"Team":"Stoke City (R)","W":7,"D":12,"L":19,"GF":35,"GA":68},
                            {"Pos":20,"Team":"West BromwichAlbion (R)","W":6,"D":13,"L":19,"GF":31,"GA":56}]

stat_point_goalID()
stat_percentages()
