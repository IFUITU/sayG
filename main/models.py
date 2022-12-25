from django.db import models


class Message(models.Model):
    room = models.ForeignKey("Room", related_name='messages', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey("client.User", on_delete=models.CASCADE, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        ordering = ('created_at',)


class Room(models.Model):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=13, unique=True, null=True)

    def __str__(self):
        return self.name



#_________SIGNALS___________
import tempfile
from random import randint
from datetime import datetime
from config.settings import MEDIA_ROOT
from django.core.files import File

from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from pydub.playback import play



@receiver(pre_save, sender=Message)
def tts_stt_signal(sender, instance, **kwargs):
    if instance.pk:
        
        # if instance.text != None:
        #     audio_name = "{}_{}.mp3".format(datetime.now(), randint(0, 1000))
        #     audio = gTTS(text=instance.text, lang="en", slow=False)

        #     with open(audio_name, 'rb') as f:
        #         audio.write_to_fp(f)
        #         instance.audio.save(audio_name, File(file=f))

        #     fp = BytesIO()
        #     audio.write_to_fp(fp)
        #     # fp.seek(0)
        #     instance.save()
            
        if instance.audio != None:
            # print(prev_obj.audio.path)
            audio_name = "{}_{}.mp3".format(datetime.now(), randint(0, 1000))
            sound = AudioSegment.from_mp3(instance.audio.path)
            sound.export(audio_name, format="wav")

            r = sr.Recognizer()
            with sr.AudioFile(audio_name) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                
                # # recognize (convert from speech to text)
                text = r.recognize_google(audio_data, language='uz')
                instance.text = text
        
            