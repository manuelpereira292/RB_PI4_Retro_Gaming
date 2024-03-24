# 3dmap module for AmazeBalls
import json
import os

real_folder = "/media/manuelpereira292/4716-5624/VS_Code/RB_PI4_Retro_Gaming/Part 09 - AmazeBalls 2/"

def loadmap(mp):
    with open(mp) as json_data:
        d = json.load(json_data)
    mapdata = {"width":d["width"], "height":d["height"]}
    rawdata = d["layers"][0]["data"]
    mapdata["data"] = []
    for x in range(0, mapdata["width"]):
        st = x*mapdata["width"]
        mapdata["data"].append(rawdata[st:st+mapdata["height"]])

    tileset = real_folder + "maps/" + d["tilesets"][0]["source"].replace(".tsx",".json")
    with open(tileset) as json_data:
        t = json.load(json_data)
    
    mapdata["tiles"] = t["tiles"]
    for tile in range(0,len(mapdata["tiles"])):
        path = mapdata["tiles"][tile]["image"]
        mapdata["tiles"][tile]["image"] = os.path.basename(path)
        mapdata["tiles"][tile]["id"] = mapdata["tiles"][tile]["id"]+1
    return mapdata
