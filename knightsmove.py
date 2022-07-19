def solution(src, dest):

    # check if source and destination are the same
    if dest == src:
        return '0'

    import math

    # this dictionary contains the possible moves that can be taken by the knight.
    # the key-value pairs link the moves from a board with squares labelled 0-63 to a board labelled by cartesian coordinates
    comb = {17: [1, 2], -17: [-1, -2], 15: [-1, 2], -15: [1, -2], 10: [2, 1], -10: [-2, -1], 6: [-2, 1], -6: [2, -1]}

    # check if a move from the possible moves dictionary is valid from the knight's current position
    def valid(current, move):

        # convert current position to cartesian coordinates
        x = int(current % 8)
        y = int(math.floor(current / 8))

        a = comb.get(move)

        # if the move is taken, check if the knight is still on the board.
        if((x + a[0]) >= 0 and (x + a[0]) < 8 and (y + a[1]) >= 0  and (y + a[1]) < 8):
            return True
        else:
            return False

    def recurs(step, temp, counter):
        # loop through all of the possible current positions of the knight and the possible moves dictionary.
        for pos in step:
            for num in comb:
                # if a particular move from the current position is possible, add the resulting position to a temp variable.
                if valid(pos,num):
                    temp.append(pos + num)
        # overwite the possible current positions of the knight with those in the temp variable, and then clear temp.
        step = temp.copy()
        temp.clear()
        # from step (the list of all possible positions after a move) check if the destination is found. If so return the number of moves taken.
        if dest in step:
            return counter
        else:
            # take a new move, repeating the process above in the recursive function to see if the destination is found.
            counter +=1
            return recurs(step, temp, counter)

    # call the function that makes a move and identifies all of the possible resulting positions.
    # start at the source with a counter at 1, because if we have reached this statement we know the minimum number of moves to reach the destination is 1.
    return recurs([src], [], 1)

print(solution(0,1))
