from mycroft import MycroftSkill, intent_file_handler
import subprocess


class ControlFurby(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('autumn.adventure.intent')
    def autumn_adventure(self, message):
        self.speak_dialog('autumn.adventure')
        subprocess.call(["aplay", "-q", "/home/pi/mycroft-core/skills/winston-more-cowbell.cdoebler/music/autumn_adventure.mp3"])

    def stop(self):
        pass


def create_skill():
    return ControlFurby()
