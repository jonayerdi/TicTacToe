from .models import Game

class GameLogic:

    def check_finish(game,square):
        if GameLogic.check_line(game,square): 
            return True
        elif GameLogic.check_diagonal(game,square): 
            return True
        elif GameLogic.check_square(game,square): 
            return True
        elif GameLogic.check_diamond(game,square): 
            return True
        elif GameLogic.check_stalemate(game,square): 
            return True
        else:
            return False
            
    def check_line(game,square):
        row = int(square/6)
        col = square%6
        indexX = [[],[]]
        indexO = [[],[]]
        for i in range(6):
            index = [int(6*i+col),int(6*row+i)]
            for d in range(2):
                if game.state[index[d]]=='X':
                    indexX[d].append(index[d])
                    indexO[d]=[]
                elif game.state[index[d]]=='O':
                    indexX[d]=[]
                    indexO[d].append(index[d])
                else:
                    indexX[d]=[]
                    indexO[d]=[]
                if len(indexX[d])==4:
                    for e in indexX[d]:
                        game.state = game.state[:e]+'x'+game.state[e+1:]
                    Game.finish(game,game.user1)
                    return True
                elif len(indexO[d])==4:
                    for e in indexO[d]:
                        game.state = game.state[:e]+'o'+game.state[e+1:]
                    Game.finish(game,game.user2)
                    return True
        return False

    def check_diagonal(game,square):
        return False

    def check_square(game,square):
        value = game.state[square]
        row = int(square/6)
        col = square%6
        for i in [-1,1]:
            for j in [-1,1]: 
                index=[int(square),int(6*(row+i)+col),int(6*row+col+j),int(6*(row+i)+col+j)]
                formSquare = True
                for k in range(4):
                    if index[k]<0 or index[k]>35 or game.state[index[k]]!=value:
                        formSquare = False
                        break
                if formSquare:
                    winner = game.user1
                    newValue = 'x'
                    if value=='O':
                        winner = game.user2
                        newValue = 'o'
                    for e in index:
                        game.state = game.state[:e]+newValue+game.state[e+1:]
                    Game.finish(game,winner)
                    return True
        return False

    def check_diamond(game,square):
        value = game.state[square]
        row = int(square/6)
        col = square%6
        for i in [-1,1]:
            for j in [-1,1]:
                p = i*j
                i2 = i*p
                j2 = j*-p
                index=[int(square),int(6*(row+i)+col+j),int(6*(row+i2)+col+j2),int(6*(row+i+i2)+col+j+j2)]
                formDiamond = True
                for k in range(4):
                    if index[k]<0 or index[k]>35 or game.state[index[k]]!=value:
                        formDiamond = False
                        break
                if formDiamond:
                    winner = game.user1
                    newValue = 'x'
                    if value=='O':
                        winner = game.user2
                        newValue = 'o'
                    for e in index:
                        game.state = game.state[:e]+newValue+game.state[e+1:]
                    Game.finish(game,winner)
                    return True
        return False

    def check_stalemate(game,square):
        for i in range(36):
            if game.state[i]!='X' and game.state[i]!='O':
                return False
        Game.finish(game,None)
        return True