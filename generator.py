import sys
import csv
import random
import string

def random_movie_title(remaining_movies, selected_movies):
    while remaining_movies:
        random_movie = random.choice(list(remaining_movies))
        if(random_movie not in selected_movies):
            selected_movies.add(random_movie)
            remaining_movies.remove(random_movie)
            return random_movie

def fake_movie_title():
    min_value = 8
    max_value = 32
    peak_value = 15
    mode = peak_value

    letters = string.ascii_lowercase * 20 + string.ascii_uppercase * 4 + string.digits + ' ' * 4 * 26
    length = int(random.triangular(min_value, max_value, mode))
    random_string = ''.join(random.choice(letters) for _ in range(length))

    # Remove adjacent spaces
    random_string = ' '.join(random_string.split())

    # Remove leading and trailing spaces
    random_string = random_string.strip()

    return ''.join(random.choice(letters) for _ in range(length))

def main():
    numMovies = int(sys.argv[1])
    numUsers = int(sys.argv[2])

    filename = 'movie_titles.csv' # comma-sanitized values

    with open(filename, 'r') as movie_file:
        csv_reader = csv.reader(movie_file)
        csv_lines = [line for line in csv_reader if line]  # Skip empty lines

        selected_movies = set()
        remaining_movies = set(line[0] for line in csv_lines if line)  # Skip lines without any columns

        with open(f'{numMovies}movies_{numUsers}users.txt', 'a') as file:
            for _ in range(numMovies):
                line = ''
                line += random_movie_title(remaining_movies, selected_movies) + ','

                ratings = []
                for _ in range(numUsers):
                    rating = random.randint(-3, 5) # negatives to increase the odds of blank ratings
                    if rating <= 0:
                        ratings.append('')
                    else:
                        ratings.append(str(rating))
                line += ','.join(ratings)

                line += '\n'

                file.write(line)
        
if __name__ == "__main__":
    main()
