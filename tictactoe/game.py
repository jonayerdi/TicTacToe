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
        row = int(square)/6
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
                print("dim "+str(d)+"countX: "+str(len(indexX[d])))
                print("dim "+str(d)+"countO: "+str(len(indexO[d])))
                if len(indexX[d])==4:
                    print("4 X in dim "+str(d))
                    for e in indexX[d]:
                        game.state = game.state[:e]+'x'+game.state[e+1:]
                    Game.finish(game,game.user1)
                    return True
                elif len(indexO[d])==4:
                    print("4 O in dim "+str(d))
                    for e in indexO[d]:
                        game.state = game.state[:e]+'o'+game.state[e+1:]
                    Game.finish(game,game.user2)
                    return True
        return False

    def check_diagonal(game,square):
        return False

    def check_square(game,square):
        return False

    def check_diamond(game,square):
        return False

    def check_stalemate(game,square):
        return False