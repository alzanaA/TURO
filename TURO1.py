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
zid = []
ps = []
z1 = []
z2 = []

for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
    zid += [zone_id]
    ps += [platinum_source]

for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    z1 += [zone_1]
    z2 += [zone_2]

# game loop
while True:
    my_platinum = int(input())  # your available Platinum

    zvisid = []
    zvisown = []
    zvisp0 = []
    zvisp1 = []
    zvisvis = []
    zvisplat = []
    
    zpodid = []
    zpodown = []
    zpodp0 = []
    zpodp1 = []
    zpodvis = []
    zpodplat = []
    
    posmove = []
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
            zvisid += [z_id]
            zvisown += [owner_id]
            zvisp0 += [pods_p0]
            zvisp1 += [pods_p1]
            zvisvis += [visible]
            zvisplat += [platinum]

        if pods_p0 > 1:
            zpodid += [z_id]
            zpodown += [owner_id]
            zpodp0 += [pods_p0]
            zpodp1 += [pods_p1]
            zpodvis += [visible]
            zpodplat += [platinum]

            posmove.append([])
            for i in range(len(z1)):
                if z1 [i] == z_id:
                    posmove[count].append(z2 [i])
                if z2 [i] == z_id:
                    posmove[count].append(z1 [i])

            count += 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    
    
    
    # first line for movement commands, second line no longer used (see the protocol in the statement for details)
    move = []

    for i in range(len(zpodid)):
        podval = 1
        if zpodp0 [i] > 1 :
			podval = zpodp0 [i] // 2
        move += [podval, zpodid[i], posmove[i][randint(0, len(posmove[i]) - 1)]]

    for i in move:
        print(i, end = " ")
    print()
    
    print("WAIT")
