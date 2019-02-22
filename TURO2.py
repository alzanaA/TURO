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

# game loop
while True:
    my_platinum = int(input())  # your available Platinum

    z_vis_id, z_vis_own, z_vis_p0, z_vis_p1, z_vis_vis, z_vis_plat = [], [], [], [], [], []
    z_pod_id, z_pod_own, z_pod_p0, z_pod_p1, z_pod_vis, z_pod_plat = [], [], [], [], [], []
    pos_move = []
    Number_p1 = []
    count = 0

    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]

        if visible == 1:
            z_vis_id += [z_id]
            z_vis_own += [owner_id]
            z_vis_p0 += [pods_p0]
            z_vis_p1 += [pods_p1]
            z_vis_vis += [visible]
            z_vis_plat += [platinum]

        if owner_id == my_id and pods_p0 > 0:
            z_pod_id += [z_id]
            z_pod_own += [owner_id]
            z_pod_p0 += [pods_p0]
            z_pod_p1 += [pods_p1]
            z_pod_vis += [visible]
            z_pod_plat += [platinum]
        
        Number_p1 += [pods_p1]

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
    #p1
       
    for i in range (len (z_pod_id)):
		for j in pos_move [i]:
			if z_pod_p0 [i] >= Number_p1 [j]:
				zf = j
			else:
				zf = z_pod_id [i]
				
    #move
    move = []
        
    for i in range(len(z_pod_id)):
		if z_pod_p0[i] // 2 > 0:
			pod_move = z_pod_p0[i] // 2
		else:
			pod_move = 1
        move += [pod_move, z_pod_id[i], zf]
        
    for i in move:
        print(i, end = " ")
    print()
    
    print("WAIT")

