#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(db_column='ID_Cliente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'


class Colaborador(models.Model):
    id_colabor = models.IntegerField(db_column='ID_Colabor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Colaborador'


class Entrada(models.Model):
    id_entrada = models.IntegerField(db_column='ID_Entrada', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=10)  # Field name made lowercase.
    id_evento = models.ForeignKey('Evento', models.DO_NOTHING, db_column='ID_Evento')  # Field name made lowercase.
    tipo_entrada_id_tipo_entrada = models.ForeignKey('TipoEntrada', models.DO_NOTHING, db_column='Tipo_Entrada_ID_Tipo_Entrada')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Entrada'


class EntradaXClientes(models.Model):
    id_entrada = models.ForeignKey(Entrada, models.DO_NOTHING, db_column='ID_Entrada', primary_key=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ID_Cliente')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Entrada_X_Clientes'
        unique_together = (('id_entrada', 'id_cliente'),)


class Evento(models.Model):
    id_evento = models.IntegerField(db_column='ID_Evento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500)  # Field name made lowercase.
    id_promotor = models.ForeignKey('Promotor', models.DO_NOTHING, db_column='ID_Promotor')  # Field name made lowercase.
    id_colaborades = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='ID_Colaborades')  # Field name made lowercase.
    id_patrocinador = models.ForeignKey('Patrocinador', models.DO_NOTHING, db_column='ID_Patrocinador')  # Field name made lowercase.
    id_lugar_evento = models.ForeignKey('LugarEvento', models.DO_NOTHING, db_column='ID_Lugar_Evento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Evento'


class LugarEvento(models.Model):
    id_lugar_evento = models.IntegerField(db_column='ID_Lugar_Evento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=40)  # Field name made lowercase.
    capacidad = models.IntegerField(db_column='Capacidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lugar_Evento'


class Patrocinador(models.Model):
    id_patrocinador = models.IntegerField(db_column='ID_Patrocinador', primary_key=True)  # Field name made lowercase.
    nombre_empresa = models.CharField(db_column='Nombre_Empresa', max_length=30)  # Field name made lowercase.
    ruc = models.IntegerField(db_column='RUC')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patrocinador'

class Promotor(models.Model):
    id_promotor = models.IntegerField(db_column='ID_Promotor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Promotor'


class PromotorXEntrada(models.Model):
    promotor_id_promotor = models.ForeignKey(Promotor, models.DO_NOTHING, db_column='Promotor_ID_Promotor', primary_key=True)  # Field name made lowercase.
    entrada_id_entrada = models.ForeignKey(Entrada, models.DO_NOTHING, db_column='Entrada_ID_Entrada')  # Field name made lowercase.
    ganancia_promotor = models.FloatField(db_column='Ganancia_Promotor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Promotor_X_Entrada'
        unique_together = (('promotor_id_promotor', 'entrada_id_entrada'),)


class TipoEntrada(models.Model):
    id_tipo_entrada = models.IntegerField(db_column='ID_Tipo_Entrada', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=15)  # Field name made lowercase.
    precio_entrada = models.FloatField(db_column='Precio_Entrada')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Entrada'


class Valoracion(models.Model):
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ID_Cliente', primary_key=True)  # Field name made lowercase.
    id_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='ID_Evento')  # Field name made lowercase.
    valoracion = models.IntegerField(db_column='Valoracion')  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Valoracion'
        unique_together = (('id_cliente', 'id_evento'),)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        
class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
        
class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'