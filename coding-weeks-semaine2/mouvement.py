def get_empty_tiles_positions(grid):
    empty_tiles=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==' ' or grid[i][j]==0:
                empty_tiles.append((i,j))
    return empty_tiles

def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    if move in ['g','d','h','b']:
        return move
    else:
        print('commande incorrecte')
        read_player_command()


def move_row_left(grid,fusion):
    n=len(grid)
    limite=0
    for j in range(1,n):
        i=1
        while grid[j-i] in [0,' '] and j-i>=0:
            grid[j-i]=grid[j-i+1]
            grid[j-i+1]=0
            i+=1
        if j-i>=0 and fusion and grid[j-i]==grid[j-i+1] and j-i+1>limite:
            grid[j-i]=2*grid[j-i]
            grid[j-i+1]=0
            limite=j-i+1
    return grid

def move_row_right(grid,fusion):
    n=len(grid)
    limite=n-1
    for j in range(n-2,-1,-1):
        i=1
        while j+i<=n-1 and grid[j+i] in [0,' ']:
            grid[j+i]=grid[j+i-1]
            grid[j+i-1]=0
            i+=1

        if j+i<=n-1 and fusion and grid[j+i]==grid[j+i-1] and j+i-1<limite:
            grid[j+i]=2*grid[j+i]
            grid[j+i-1]=0
            limite=j+i-1
    return grid

def rota(grid):
    n=len(grid)
    rot=[[0 for k in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rot[i][j]=grid[j][i]

    return(rot)




def move_grid(grid,d,fusion=False):
    n=len(grid)
    if d=="left":
        for i in range(n):
            grid[i]=move_row_left(grid[i],fusion)
    else:
        if d=="right":
            for i in range(n):
                grid[i]=move_row_right(grid[i],fusion)
        else:
            grid=rota(grid)
            if d=="up":
                for i in range(n):
                    grid[i]=move_row_left(grid[i],fusion)
            else:
                if d=="down":
                    for i in range(n):
                        grid[i]=move_row_right(grid[i],fusion)
            grid=rota(grid)
    return grid
