def solution(src, dest):
    #create a code which uses the 8 coordinate transformations
    #to go from one number to another
    import math

    comb = [17, -17, 15, -15, 10, -10, 6, -6]

    def valid(current, move):
        x = int(math.floor(current / 8))
        y = int(current % 8)
        x1 = 0
        y1 = 0
        if move == 17:
            x1 = 2
            y1 = 1
        if move == -17:
            x1 = -2
            y1 = -1
        if move == 15:
            x1 = 2
            y1 = -1
        if move == -15:
            x1 = -2
            y1 = 1
        if move == 10:
            x1 = 1
            y1 = 2
        if move == -10:
            x1 = -1
            y1 = -2
        if move == 6:
            x1 = 1
            y1 = -2
        if move == -6:
            x1 = -1
            y1 = 2
        if((x + x1) >= 0 and (x + x1) < 8 and (y + y1) >= 0  and (y + y1) < 8):
            return True
        else:
            return False

    #check if you are already at destination square
    if dest == src:
        return '0'

    #check if target is a number in the list
    pos = src
    for num in comb:
        if valid(pos, num) == True and (pos + num) == dest:
            return '1'
    #check if target can be found using a pair of numbers
    for num2 in comb:
        for num3 in comb:
            pos = src
            if valid(pos, num2) == True:
                pos = pos + num2
                if valid(pos, num3) == True and (pos + num3) == dest:
                    print(src, num2, num3, dest, pos)
                    return '2'
    #check if target can be found using three numbers
    for num4 in comb:
        for num5 in comb:
            for num6 in comb:
                pos = src
                if valid(pos, num4) == True:
                    pos = pos + num4
                    if valid(pos, num5) == True:
                        pos = pos + num5
                        if valid(pos, num6) == True and (pos + num6) == dest:
                            print(src, num4, num5, num6, dest, pos)
                            return '3'
    #check if target can be found using 4 numbers
    for num7 in comb:
        for num8 in comb:
            for num9 in comb:
                for num10 in comb:
                    pos = src
                    if valid(pos, num7) == True:
                        pos = pos + num7
                        if valid(pos, num8) == True:
                            pos = pos + num8
                            if valid(pos, num9) == True:
                                pos = pos + num9
                                if valid(pos, num10) == True and (pos + num10) == dest:
                                    print(src, num7, num8, num9, num10, dest, pos)
                                    return '4'
    #check if target can be found using 5 numbers
    for num11 in comb:
        for num12 in comb:
            for num13 in comb:
                for num14 in comb:
                    for num15 in comb:
                        pos = src
                        if valid(pos, num11) == True:
                            pos = pos + num11
                            if valid(pos, num12) == True:
                                pos = pos + num12
                                if valid(pos, num13) == True:
                                    pos = pos + num13
                                    if valid(pos, num14) == True:
                                        pos = pos + num14
                                        if valid(pos, num15) == True and (pos + num15) == dest:
                                            print(src, num11, num12, num13, num14, num15, dest, pos)
                                            return '5'
    #check if target can be found using 6 numbers
    for num16 in comb:
        for num17 in comb:
            for num18 in comb:
                for num19 in comb:
                    for num20 in comb:
                        for num21 in comb:
                            pos = src
                            if valid(pos, num16) == True:
                                pos = pos + num16
                                if valid(pos, num17) == True:
                                    pos = pos + num17
                                    if valid(pos, num18) == True:
                                        pos = pos + num18
                                        if valid(pos, num19) == True:
                                            pos = pos + num19
                                            if valid(pos, num20) == True:
                                                pos = pos + num20
                                                if valid(pos, num21) == True and (pos + num21) == dest:
                                                    print(src, num16, num17, num18, num19, num20, num21, dest, pos)
                                                    return '6'

print(solution(0, 1))
