class Display:
    def on(self):
        print("Display is ON")

    def off(self):
        print("Display is OFF")

class DVD:
    def play(self):
        print("DVD is playing movies")

    def pause(self):
        print("DVD is pausing movie")

    def stop(self):
        print("DVD is stopping the movie")

class Speaker:
    def up(self):
        print("Speaker's volume is up")

    def down(self):
        print("Speaker's volume is down")

class ComputerFacade:
    def __init__(self,display:Display,dvd:DVD,speaker:Speaker):
        self._display = display
        self._dvd = dvd
        self._speaker = speaker

    def watch_movie(self,movie:str):
        self._display.on()
        self._dvd.play()
        self._speaker.up()

    def pause_movie(self,movie:str):
        self._display.off()
        self._dvd.pause()
        self._speaker.down()
    
    def stop_movie(self,movie:str):
        self._display.off()
        self._dvd.stop()
        self._speaker.down()

display1 = Display()

dvd1 = DVD()

speaker1 = Speaker()

computer1 = ComputerFacade(display1,dvd1,speaker1)

computer1.watch_movie("The Chronicles of Ground Breakers")

computer1.pause_movie("The Chronicles of Ground Breakers")

computer1.stop_movie("The Chronicles of Ground Breakers")
