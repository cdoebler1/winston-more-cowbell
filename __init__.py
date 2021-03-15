from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService


class ControlFurby(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.audio_service = AudioService(self.bus)

    @intent_file_handler('autumn.adventure.intent')
    def autumn_adventure(self, message):
        self.speak_dialog('autumn.adventure')
        story = "skills/winston-more-cowbell.cdoebler1/music/autumn_adventure.mp3"
        self.audio_service.play(story)

    def stop(self):
        pass


def create_skill():
    return ControlFurby()
