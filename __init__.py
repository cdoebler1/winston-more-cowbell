from mycroft import MycroftSkill, intent_file_handler
import subprocess


class ControlFurby(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('furby.tell.intent')
    def handle_furby_tell(self, message):
        self.speak_dialog('furby.tell')

    @intent_file_handler('furby.dance.intent')
    def handle_furby_dance(self, message):
        self.speak_dialog('furby.dance')

    @intent_file_handler('furby.sing.intent')
    def handle_furby_sing(self, message):
        self.speak_dialog('furby.sing')
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "/home/pi/Hacksby/bin/furby-send.pl", "868"])

    @intent_file_handler('more.cowbell.intent')
    def handle_more_cowbell(self, message):
        self.speak_dialog('more.cowbell')
        subprocess.call(["aplay", "-q", "/home/pi/mycroft-core/skills/control-furby.cdoebler/music/dftr.wav"])

    @intent_file_handler('autumn.adventure.intent')
    def autumn_adventure(self, message):
        self.speak_dialog('autumn.adventure')
        subprocess.call(["aplay", "-q", "/home/pi/mycroft-core/skills/winston-more-cowbell.cdoebler/music/autumn_adventure.mp3"])

    def stop(self):
        pass


def create_skill():
    return ControlFurby()
