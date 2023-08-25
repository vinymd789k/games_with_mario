import pandas as pd
import re

#Extração ( Extract )
videogames_sales = pd.read_csv('vgsales.csv')
videogames_sales_name = videogames_sales['Name']

#Transformação ( Transform )
Mario = re.compile(r'Mario')
Mario_games = [ name for name in videogames_sales_name if Mario.search(str((name))) ]

#Armazenar (Load)
def encontrar_mario(name):
    
    Games_with_mario = pd.DataFrame()

    for x in name:
        
        adicionar_linha = videogames_sales.loc[ videogames_sales[ 'Name' ] == x ]
        Games_with_mario = Games_with_mario.append( adicionar_linha, ignore_index = True )
        print(Games_with_mario)
    
    return Games_with_mario

result = encontrar_mario(Mario_games)

#Armazenar( Load )
result.to_csv('Games_with_mario.csv', index = False)