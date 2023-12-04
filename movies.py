import pandas as pd
from mocks import MOVIE_DATA_MOCK

df_movies = pd.DataFrame(MOVIE_DATA_MOCK)

def display_menu(movies):
    print("\n=== MENU ===")
    for i, (_, movie) in enumerate(movies.iterrows()):
        print(f"{i + 1}. {movie['Title']} ({movie['Genre']})")

def display_movie_summary(movie):
    print("\n=== RESUMO ===")
    print(f"Título: {movie['Title']}")
    print(f"Gênero: {movie['Genre']}")
    print(f"Resumo: {movie['Summary']}")
    print(f"Visualizações: {movie['Views']}")

user_genre = input("Digite um gênero para recomendação: ")
user_genre_lower = user_genre.lower()

genre_movies = df_movies[df_movies['Genre'].str.contains(user_genre_lower, case=False)]
genre_movies_sorted = genre_movies.sort_values(by='Views', ascending=False)

while True:
    display_menu(genre_movies_sorted[['Title', 'Genre', 'Views']])
    
    selected_index = input("\nDigite o número do filme para ver o resumo (ou 's' para sair): ")
    
    if selected_index.lower() == 's':
        break  # Saia do loop se o usuário digitar 's' para sair
    elif selected_index.isdigit():
        selected_index = int(selected_index) - 1

        if 0 <= selected_index < len(genre_movies_sorted):
            selected_movie = genre_movies_sorted.iloc[selected_index]
            display_movie_summary(selected_movie)
        else:
            print("Índice selecionado inválido. Tente novamente.")
    else:
        print("Entrada inválida. Tente novamente.")