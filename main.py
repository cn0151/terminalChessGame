from ChessGameModule import ChessGame

def start_game():
    print "1. New game \t 2. Load game"
    response = raw_input("Enter choice: ")
    response = response.strip()

    while((response != "1") and (response != "2")):
        print "Error: incorrect response"
        print "1. New game \t 2. Load game"
        response = raw_input("Enter choice: ")


    return int(response)




def load_game(game_obj, file_handler):
    move = file_handler.readline()
    player_num = 1
    line_read = 0
    
    while(move):
        line_read = 1
        move_token = move.split(':')
        player_num = int(move_token[0])
        game_obj.is_valid_user_input(player_num, move_token[1])
        move = file_handler.readline()

    file_handler.seek(0, 2)
    if(line_read and player_num == 1):
        return 2
    elif(line_read and player_num == 2):
        return 1
    else:
        return player_num

    

def play_game(player, game_obj, file_handler):
    while(1):
        game_obj.display_board()
        user_move = (raw_input(("player %d move: " % (player)))).strip()
        if(user_move.lower() == 'stop'):
            return

        
        is_good = game.is_valid_user_input(player, user_move)
        while(not is_good):
            print "Error: Incorrect move"
            user_move = raw_input(("player %d move: " % (player)))
            if(user_move.lower() == 'stop'):
                return
            is_good = game.is_valid_user_input(player, user_move)

        if(is_good):
            file_handler.write(str(player) + ":" + user_move + '\n')

        if(player == 1):
            player = 2
        else:
            player = 1

        


            

game = ChessGame()
if(start_game() == 1):
    file_open = open("savedgame.txt","w")
    player = 1
else:
    file_open = open("savedgame.txt","a+")
    player = load_game(game, file_open)


play_game(player, game, file_open)


file_open.close()

