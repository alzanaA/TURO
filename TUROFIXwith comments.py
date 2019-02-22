import sys
import math
from random import randint

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
l_zone_id, l_platinum_source = [], []
l_zone_1, l_zone_2 = [], []

for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
    l_zone_id += [zone_id]
    l_platinum_source += [platinum_source]

for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    l_zone_1 += [zone_1]
    l_zone_2 += [zone_2]

def f (L,x):
	for i in range (len (L)):
		if L [i] == x and L [0] != x :
			L [i] = L [0]
		if L [i] != x and L [0] == x :
			L [0] = L [i]
	return L

# game loop
while True:
    my_platinum = int(input())  # your available Platinum

    z_vis_id, z_vis_own, z_vis_p0, z_vis_p1, z_vis_vis, z_vis_plat = [], [], [], [], [], []
    z_pod_id, z_pod_own, z_pod_p0, z_pod_p1, z_pod_vis, z_pod_plat = [], [], [], [], [], []
    pos_move = []
    count = 0

    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        
        #all visible zones
        if visible == 1:
            z_vis_id += [z_id]
            z_vis_own += [owner_id]
            z_vis_p0 += [pods_p0]
            z_vis_p1 += [pods_p1]
            z_vis_vis += [visible]
            z_vis_plat += [platinum]

        #location of the pods
        if owner_id == my_id and pods_p0 > 0:
            z_pod_id += [z_id]
            z_pod_own += [owner_id]
            z_pod_p0 += [pods_p0]
            z_pod_p1 += [pods_p1]
            z_pod_vis += [visible]
            z_pod_plat += [platinum]
            

            #all possible moves of every pods
            pos_move.append([])
            for i in range(len(l_zone_1)):
                if l_zone_1[i] == z_id:
                    pos_move[count].append(l_zone_2[i])
                if l_zone_2[i] == z_id:
                    pos_move[count].append(l_zone_1[i])

            count += 1
            
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    
    # avoid enemies
    for i in range (len (z_pod_id)):
        for j in range(len (pos_move [i])):
            for k in range (len (z_vis_id)):
                if pos_move [i] [j] == z_vis_id [k]:
                    if z_vis_p1 [j] > z_pod_p0 [i]:
                        pos_move = f (pos_move [i], pos_move [i] [j])
    
    # move (in 2 pods)
    move = []
        
    for i in range(len(z_pod_id)):
        if z_pod_p0 [i] > 3:
            pod_move = z_pod_p0[i] // 2
        if z_pod_p0 [i] > 1:
            pod_move = 2
        else:
            pod_move = 1
        move += [pod_move, z_pod_id[i], pos_move [i] [randint (0, len (pos_move [i]) - 1)]]
    
    for i in move:
        print(i, end = " ")
    print()
    
    print("WAIT")
