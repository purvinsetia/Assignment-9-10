class MovieDetails:
    def __init__(self,MovNa,ArtNa,YOR,Rat):
        self.MovieName = MovNa
        self.ArtistName = ArtNa
        self.YearOfRelease = YOR
        self.Ratings = Rat
    def display(self):
        print("Movie Name-> %s\nArtist Name-> %s\nYear Of Release-> %d\nRatings-> %d"%(self.MovieName,self.ArtistName,self.YearOfRelease,self.Ratings))
    def update(self,MNa,ANa,YR,R):
        self.MovieName = MNa
        self.ArtistName = ANa
        self.YearOfRelease = YR
        self.Ratings = R

movie = MovieDetails("Batman","bat",2008,10)
movie.display()
movie.update("superman","Super",2009,10)
movie.display()
