from django.contrib.auth.models import Group, User
from django.db.models import Model, CommaSeparatedIntegerField, ForeignKey, BooleanField


class ChristmasGroup(Model):
    group = ForeignKey(Group, unique=True)
    rotation = CommaSeparatedIntegerField(max_length=256, default='', blank=True)  # 89 guys max…
    closed = BooleanField(default=False)

    def save(self, *args, **kwargs):
        guys = self.group.user_set.order_by('?').values_list('pk', flat=True)
        self.rotation = ','.join(str(i) for i in guys)
        super().save(*args, **kwargs)

    def gift(self, me):
        rot = eval(self.rotation)
        return User.objects.get(pk=rot[(rot.index(me) + 1) % len(rot)])
