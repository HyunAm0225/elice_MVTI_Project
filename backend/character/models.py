from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField('character name', max_length=100)
    wc_url = models.URLField('wordcloud url', null=True)
    bar_url = models.URLField('barchart url', null=True)
    character_img_url = models.URLField('character img url', default='', null=True)
    count = models.IntegerField('count', default=0, null=True)
    rival = models.CharField('rival', max_length=100, null=True)
    partner = models.CharField('partner', max_length=100, null=True)
    MVTI_NSAF = 'NSAF'
    MVTI_NSAA = 'NSAA'
    MVTI_NSTF = 'NSTF'
    MVTI_NSTA = 'NSTA'
    MVTI_NJAF = 'NJAF'
    MVTI_NJAA = 'NJAA'
    MVTI_NJTF = 'NJTF'
    MVTI_NJTA = 'NJTA'
    MVTI_PSAF = 'PSAF'
    MVTI_PSAA = 'PSAA'
    MVTI_PSTF = 'PSTF'
    MVTI_PSTA = 'PSTA'
    MVTI_PJAF = 'PJAF'
    MVTI_PJAA = 'PJAA'
    MVTI_PJTF = 'PJTF'
    MVTI_PJTA = 'PJTA'
    CHOICES_MVTI = (
        (MVTI_NSAF, 'NSAF'),
        (MVTI_NSAA, 'NSAA'),
        (MVTI_NSTF, 'NSTF'),
        (MVTI_NSTA, 'NSTA'),
        (MVTI_NJAF, 'NJAF'),
        (MVTI_NJAA, 'NJAA'),
        (MVTI_NJTF, 'NJTF'),
        (MVTI_NJTA, 'NJTA'),
        (MVTI_PSAF, 'PSAF'),
        (MVTI_PSAA, 'PSAA'),
        (MVTI_PSTF, 'PSTF'),
        (MVTI_PSTA, 'PSTA'),
        (MVTI_PJAF, 'PJAF'),
        (MVTI_PJAA, 'PJAA'),
        (MVTI_PJTF, 'PJTF'),
        (MVTI_PJTA, 'PJTA')
    )
    mvti_type = models.CharField('MVTI_Type', choices=CHOICES_MVTI, null=True, max_length=12)
    sentiment = models.JSONField('sentiment json', null=True)
    best_talk = models.CharField('best_talk', null=True, max_length=100)

    class Meta:
        db_table = 'Characters'

    def add_count(self):
        self.count += 1
