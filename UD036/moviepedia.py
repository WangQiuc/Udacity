import movie

kubo = movie.Movie(
        'Kubo and the Two Strings',
        'A young boy named Kubo must locate a magical suit of armour worn by his late father in order to defeat a vengeful spirit from the past.',
        'http://www.imdb.com/title/tt4302938/mediaviewer/rm2153911296',
        'http://www.imdb.com/title/tt4302938/videoplayer/vi2096412441?ref_=tt_ov_vi')

guardians = movie.Movie(
        'Guardians of the Galaxy Vol.2',
        "The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill's true parentage.",
        'http://www.imdb.com/title/tt3896198/mediaviewer/rm911094272',
        'http://www.imdb.com/title/tt3896198/videoplayer/vi3076896281?ref_=tt_ov_vi')

movies = [kubo, guardians]

while True:
    print('Choose the movie:\n1. Kubo\n2. Guardians\n')
    m = int(input()) - 1
    print('Choose the section:\n1. Movie Title\n2. Storyline\n3. Poster\n4. Trailer\n0. Return\n')
    while True:
        i = int(input())
        if i == 1:
            print(movies[m].title)
        elif i == 2:
            print(movies[m].storyline)
        elif i == 3:
            movies[m].open_poster()
        elif i == 4:
            movies[m].open_trailer()
        elif i == 0:
            break
        else:
            print('Please check your choice')
