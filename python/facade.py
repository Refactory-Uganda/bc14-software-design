class Display:
    def on(self):
        print("Display is on")

    def off(self):
        print("Display is off")


class DVD:
    def play(self, movie):
        print(f"Playing movie: {movie}")

    def pause(self, movie):
        print(f"Pausing movie: {movie}")

    def stop(self, movie):
        print(f"Stopped movie: {movie}")


class Speakers:
    def up(self, volume):
        print(f"Speaker is on volume: {volume}")

    def down(self, volume):
        print(f"Speaker is off volume: {volume}")


class ComputerFacade:
    def __init__(self, display, dvd, speakers):
        self.display = display
        self.dvd = dvd
        self.speakers = speakers

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.display.on()
        self.dvd.play(movie)
        self.speakers.up("10")

    def pause_movie(self, movie):
        print("Movie paused...")
        self.display.on()
        self.dvd.pause(movie)
        self.speakers.down("0")

    def end_movie(self, movie):
        print("Shutting down the home theater...")
        self.dvd.stop(movie)
        self.speakers.down("0")
        self.display.off()


display1 = Display()
dvd_player1 = DVD()
speaker1 = Speakers()
computer = ComputerFacade(display1, dvd_player1, speaker1)

computer.watch_movie("The Chronicles of the Ground Breakers")
computer.end_movie("The Chronicles of the Ground Breakers")
