r0='       '
r1='  ***  '
r2=' *   * '
r3='  * *  '
r4='   *   '
r5='_______'
rr='|'
draw={'X':[r0,r2,r3,r4,r3,r2], 'O':[r0,r1,r2,r2,r2,r1]}
middles=['   1   ','   2   ','   3   ','   4   ','   5   ','   6   ','   7   ','   8   ','   9   ']

players=['X','O']
o_turn=False

scoreboard={}
tile_list=[]
def reset_score():
    global scoreboard, tile_list, o_turn
    o_turn=False
    tile_list=[]
    for i in range(9):
        tile_list.append([r0,r0,r0,middles[i],r0,r0])
    scoreboard={
        0:'',1:'',2:'',
        3:'',4:'',5:'',
        6:'',7:'',8:''}

lines_check=[]
def check_ending():
    global lines_check, scoreboard
    lines_check=[
        [scoreboard[0],scoreboard[4],scoreboard[8]],
        [scoreboard[2],scoreboard[4],scoreboard[6]]]
    for i in [0,1,2]:
        lines_check.extend(([
        scoreboard[3*i],
        scoreboard[3*i+1],
        scoreboard[3*i+2]],[
        scoreboard[i],
        scoreboard[3+i],
        scoreboard[6+i]]))
    if ['X','X','X'] in lines_check:
        return True, True, 'X'
    elif ['O','O','O'] in lines_check:
        return True, True, 'O'
    elif '' not in scoreboard.values():
        return True, False, ''
    else:
        return False, False, ''

def set_tile():
    global tile_list, scoreboard, o_turn, players
    i='0'
    while True:
        while i not in ['1','2','3','4','5','6','7','8','9']:
            i = input(f'Jogador {players[int(o_turn)]}, faça sua jogada: (1-9) ')
        i = int(i)-1
        if scoreboard[i] == '':
            break
    scoreboard[i]=players[int(o_turn)]
    tile_list[i]=draw[scoreboard[i]]
    o_turn = not o_turn

def draw_board():
    for i in range(3):
        for j in range(7):
            if (j == 6 and i == 2) or j == 0:
                print(r0+rr+r0+rr+r0)
            elif j == 6:
                print(r5+rr+r5+rr+r5)
            else:
                print(tile_list[3*i][j]+rr+tile_list[3*i+1][j]+rr+tile_list[3*i+2][j])


reset_score()
draw_board()
while not check_ending()[0]:
    set_tile()
    draw_board()
if not check_ending()[1]:
    print('Deu velha!')
else:
    print(f'Vencedor: {check_ending()[2]}')