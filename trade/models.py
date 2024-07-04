from django.db import models


# class User(models.Model):
#     # Field name made lowercase.
#     imie = models.CharField(db_column='Imie', blank=True, null=True)
#     # Field name made lowercase.
#     nazwisko = models.CharField(db_column='Nazwisko', blank=True, null=True)
#     # Field name made lowercase.
#     saldo = models.CharField(db_column='Saldo', blank=True, null=True)
#     # Field name made lowercase.
#     id_akcji = models.CharField(db_column='ID_akcji', blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'User'


class Operation(models.Model):
    id_operacji = models.AutoField(primary_key=True)
    ilosc = models.CharField(blank=True, null=True)
    nazwa = models.CharField(blank=True, null=True)
    cena = models.CharField(blank=True, null=True)
    wlasciciel = models.CharField(blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    zakup_sprzedaz = models.CharField(
        db_column='zakup/sprzedaz', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Operation'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    saldo = models.IntegerField(default=10000, blank=True, null=True)
    id_akcji = models.CharField(blank=True, null=True)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user'
