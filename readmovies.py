import subprocess
import pandas as pd
import random

script_path = '/home/tambor/recomendations/clover/nfosearch.sh'
output_file = '/home/tambor/recomendations/clover/output.csv'


def getmovies():
    try:
        with open(output_file, 'w') as output:
            subprocess.run(['bash',script_path],stdout=output , check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def selectMovie(nmovies):
    movielist = pd.read_csv('/home/tambor/recomendations/clover/output.csv',
                            sep='@',
                            names=["name","picture", "plot", "year", "title"]
                            )
    movie_q = nmovies
    Movies = []
    Movies_names = []
    Movies_names_date = []
    Movies_selected = pd.read_csv('/home/tambor/recomendations/clover/moviesselected.dataset'
                                  ,sep='@')

    try_value = 0
    repeated_movies = 0

    if try_value  < movie_q and repeated_movies < 3*len(movielist):
        n = random.randint(0, len(movielist)-1)
        if Movies_selected['movies'].eq(movielist.iloc[n]['picture'].lstrip()).any():
            repeated_movies = repeated_movies + 1
        else:
            Movie_selected = pd.DataFrame({'movies':[movielist.iloc[n]['picture'].lstrip()]})
            Movie_plot = movielist.iloc[n]['plot']
            Movies_selected = Movies_selected._append(Movie_selected)
            try_value = try_value +1
            Movies_names_date.append(f"{movielist.iloc[n]['name'].lstrip()} year {movielist.iloc[n]['year']} ")
    Movies_selected.to_csv('/home/tambor/recomendations/clover/moviesselected.dataset',sep='@',index=False)
    return ([Movies_names_date[0],Movie_selected['movies'][0],Movie_plot])
    

    
            
