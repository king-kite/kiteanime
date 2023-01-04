from django.db import models
from django.utils.timezone import now
from embed_video.fields import EmbedVideoField



# Create your models here.


class VideoUpload(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, default='Unknown')
    cover = models.ImageField(upload_to='video/cover', null=True, blank=True)
    ongoing = models.BooleanField(default=True)
    date = models.DateTimeField(default=now, editable=False)
    date_of_release = models.DateField(default=now)

    action = models.BooleanField(default=False)
    adventure = models.BooleanField(default=False)
    comedy = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)
    ecchi = models.BooleanField(default=False)
    fantasy = models.BooleanField(default=False)
    harem = models.BooleanField(default=False)
    horror = models.BooleanField(default=False)
    isekai = models.BooleanField(default=False)
    magic = models.BooleanField(default=False)
    martial_arts = models.BooleanField(default=False)
    mecha = models.BooleanField(default=False)
    military = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    mystery = models.BooleanField(default=False)
    psychological = models.BooleanField(default=False)
    romance = models.BooleanField(default=False)
    school = models.BooleanField(default=False)
    sci_fi = models.BooleanField(default=False)
    slice_of_life = models.BooleanField(default=False)
    shounen = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    supernatural = models.BooleanField(default=False)
    tragedy = models.BooleanField(default=False)



    class Meta:
        verbose_name_plural = 'VideoUpload'
        

    def __str__(self):
        return "%s, %s" %(self.name, self.author)

class UploadVideo(models.Model):
    foreign = models.ForeignKey(VideoUpload, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    embedvideo = EmbedVideoField(default='', null=True, blank=True)
    vdate = models.DateTimeField(default=now, editable=False)

    class Meta:
        verbose_name_plural = 'Upload Videos'
        ordering = ('vdate', 'title', 'pk')

    def __str__(self):
        return self.title

class Comment(models.Model):
    foreign = models.ForeignKey(VideoUpload, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    


class UploadAnime(VideoUpload):

    class Meta:
        verbose_name_plural = 'Upload Animes'

class UploadMovie(VideoUpload):

    class Meta:
        verbose_name_plural = 'Upload Movies'

