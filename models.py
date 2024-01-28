from django.db import models
from django.core.validators import ValidationError
import json


class MySmallIntegerField(models.SmallIntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [self.validate_range]
        super().__init__(*args, **kwargs)

    def validate_range(self, value):
        if not (0 <= value <= 5):
            raise ValidationError('Wartość musi być między 0 a 6')





class players(models.Model):
    playerslist = {
        0 : "Kopek",
        1 : "Lipek",
        2 : "Niemys",
        3 : "Chojnas",
        4 : "Floro"
    }



class game(models.Model):
    name = models.CharField(unique=True,blank=False,max_length=64)
    date = models.DateField(null=True,blank=True)
    #playersnr = MySmallIntegerField(default= 5)
    playersnr = MySmallIntegerField(default=0)
    testg = models.OneToOneField("Test", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nazwaZdata()

    def nazwaZdata(self):
        return "{} {} ".format(self.name, self.date)


class Test(models.Model):
    dynamic_field = models.TextField()

    def set_dynamic_field(self, data):
        self.dynamic_field = json.dumps(data)



"""
    def To_Json(self):
        return {'name':self.name, 'date':self.date ,'playersnr':self.playersnr}


class position(models.Model):
    Positions = models.OneToOneField(game, on_delete=models.CASCADE, null=True, blank=True)

    def places(self,Positions):
        for i in range(len(game.playersnr)):
            source = "pos{}".format(i)
            place = models.SmallIntegerField(default=0, choices=players.playerslist)
            self.add_dynamic_field(source, place)

class Test(models.Model):
    Position = models.PositiveSmallIntegerField()
    User = models.CharField(max_length= 250 )

"""
