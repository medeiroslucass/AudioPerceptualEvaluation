from django.db import models
import uuid
import os
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


SEX_CHOICES = (("F", "Feminino"), ("M", "Masculino"))

@deconstructible
class MaxSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, file):
        if file.size > self.max_size:
            raise ValidationError(f'O arquivo é muito grande (tamanho máximo é {self.max_size/1024/1024:.2f} MB)')

@deconstructible
class ExtensionValidator:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file):
        ext = file.name.split('.')[-1].lower()
        if ext not in self.extensions:
            raise ValidationError(f'O arquivo deve ter uma das extensões seguintes: {", ".join(self.extensions)}')



class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Usuario(Base):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(choices=SEX_CHOICES)

    def __str__(self):
        return self.name


class Experimento(Base):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Audio(Base):
    archive = models.FileField(upload_to='audio/%Y/%m/%d', validators=[MaxSizeValidator(10*1024*1024), ExtensionValidator(['wav'])])
    category = models.ForeignKey(Experimento, on_delete=models.CASCADE, related_name='experimento_audios')
    def generate_filename(self, filename):
        ext = filename.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return os.path.join('audio', filename)

    def __str__(self):
        return os.path.basename(self.archive.name)


class Evaluation(Base):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name='audio_evaluations')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario_evaluations')
    score = models.IntegerField()
    def __str__(self):
        return   f"{self.usuario.name} - {self.usuario.age} - {self.usuario.sex} ----> {self.score}"