from django.db import models

class Acesso(models.Model):

    cd_acesso = models.IntegerField(db_column='CD_ACESSO', primary_key=True) # Field name made lowercase.
    ds_acesso = models.CharField(db_column='DS_ACESSO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACESSO'

class AssociaProduto(models.Model):
    id_associa_prod = models.AutoField(db_column='ID_ASSOCIA_PROD', primary_key=True) # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_produto_perif = models.CharField(db_column='CD_PRODUTO_PERIF', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASSOCIA_PRODUTO'

class CamarasTermicas(models.Model):
    id_camara = models.IntegerField(db_column='ID_CAMARA', primary_key=True) # Field name made lowercase.
    nro_serie_novus = models.BigIntegerField(db_column='NRO_SERIE_NOVUS', unique=True) # Field name made lowercase.
    data_instalacao = models.DateTimeField(db_column='DATA_INSTALACAO')  # Field name made lowercase.
    data_preventiva = models.DateTimeField(db_column='DATA_PREVENTIVA') # Field name made lowercase.
    data_calibracao = models.DateTimeField(db_column='DATA_CALIBRACAO')  # Field name made lowercase.
    local_fisico = models.CharField(db_column='LOCAL_FISICO', max_length=140, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAMARAS_TERMICAS'

class Cargas(models.Model):
    cd_produto = models.OneToOneField('PvProduto', models.DO_NOTHING, db_column='CD_PRODUTO', primary_key=True) # Field name made lowercase. The composite primary key (CD_PRODUTO, NOME_CARGA) found, that is not supported. The first column is selected.
    nome_carga = models.CharField(db_column='NOME_CARGA', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    caminho_carga = models.CharField(db_column='CAMINHO_CARGA', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    tipo_carga = models.CharField(db_column='TIPO_CARGA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    prefixo_arquivo = models.CharField(db_column='PREFIXO_ARQUIVO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARGAS'
        unique_together = (('cd_produto', 'nome_carga'), ('cd_produto', 'nome_carga'),)

class Chamado(models.Model):
    id_chamado = models.AutoField(db_column='ID_CHAMADO', primary_key=True)  # Field name made lowercase.
    matricula = models.IntegerField(db_column='MATRICULA')  # Field name made lowercase.
    dt_ini = models.DateTimeField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fim = models.DateTimeField(db_column='DT_FIM', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='MOTIVO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    solicitante = models.CharField(db_column='SOLICITANTE', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHAMADO'

class Comunic(models.Model):
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nro_serie = models.IntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    status_teste = models.CharField(db_column='STATUS_TESTE', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMUNIC'

class Confiabilidade(models.Model):
    nr_ocorrencia = models.AutoField(db_column='NR_OCORRENCIA', primary_key=True)  # Field name made lowercase.
    tempo_falha = models.IntegerField(db_column='TEMPO_FALHA')  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    observacao = models.CharField(db_column='OBSERVACAO', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    tempo_parado = models.IntegerField(db_column='TEMPO_PARADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIABILIDADE'

class ConfigServidor(models.Model):
    server_name = models.CharField(db_column='SERVER_NAME', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    ip_interno = models.CharField(db_column='IP_INTERNO', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    ip_externo = models.CharField(db_column='IP_EXTERNO', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIG_SERVIDOR'

class Defeito(models.Model):
    cd_defeito = models.IntegerField(db_column='CD_DEFEITO', primary_key=True) # Field name made lowercase.
    ds_defeito = models.CharField(db_column='DS_DEFEITO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEFEITO'

class DefeitoResultados(models.Model):
    cd_defeito = models.OneToOneField('Defeito', models.DO_NOTHING, db_column='CD_DEFEITO') # Field name made lowercase. The composite primary key (CD_DEFEITO, CD_LOCAL_DEFEITO, INDICE, SEQ_DEFEITOfound, that is not supported. The first column is selected.
    cd_local_defeito = models.ForeignKey('LocalDefeito', models.DO_NOTHING, db_column='CD_LOCAL_DEFEITO')  # Field name made lowercase.
    indice = models.IntegerField(db_column='INDICE')  # Field name made lowercase.
    seq_defeito = models.AutoField(db_column='SEQ_DEFEITO', primary_key=True) # Field name made lowercase.
    sc_defeito = models.CharField(db_column='SC_DEFEITO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modo_defeito = models.IntegerField(db_column='MODO_DEFEITO')  # Field name made lowercase.
    magnus_local = models.CharField(db_column='MAGNUS_LOCAL', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEFEITO_RESULTADOS'
        unique_together = (('cd_defeito', 'cd_local_defeito', 'indice', 'seq_defeito'), ('cd_defeito', 'cd_local_defeito', 'indice', 'seq_defeito'),)

class DefeitoResultados2(models.Model):
    cd_local_defeito = models.OneToOneField('LocalDefeito', models.DO_NOTHING, db_column='CD_LOCAL_DEFEITO') # Field name made lowercase. The composite primary key (CD_LOCAL_DEFEITO, CD_DEFEITO, INDICE, SEQ_DEFEITOfound, that is not supported. The first column is selected.
    cd_defeito = models.ForeignKey(Defeito, models.DO_NOTHING, db_column='CD_DEFEITO') # Field name made lowercase.
    indice = models.ForeignKey('Testesres', models.DO_NOTHING, db_column='INDICE') # Field name made lowercase.
    seq_defeito = models.AutoField(db_column='SEQ_DEFEITO', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True) # Field name made lowercase.
    sc_defeito = models.CharField(db_column='SC_DEFEITO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modo_defeito = models.IntegerField(db_column='MODO_DEFEITO')  # Field name made lowercase.
    magnus_local = models.CharField(db_column='MAGNUS_LOCAL', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEFEITO_RESULTADOS2'
        unique_together = (('cd_local_defeito', 'cd_defeito', 'indice', 'seq_defeito'), ('cd_local_defeito', 'cd_defeito', 'indice', 'seq_defeito'),)

class DefeitoSmp(models.Model):
    cd_defeito_smp = models.IntegerField(db_column='CD_DEFEITO_SMP', primary_key=True)  # Field name made lowercase.
    ds_defeito_smp = models.CharField(db_column='DS_DEFEITO_SMP', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEFEITO_SMP'

class Departamento(models.Model):
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', primary_key=True, max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ds_departamento = models.CharField(db_column='DS_DEPARTAMENTO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPARTAMENTO'

class EquipamentoAfericao(models.Model):
    cd_equip_afer = models.CharField(db_column='CD_EQUIP_AFER', primary_key=True, max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    ds_equip_afer = models.CharField(db_column='DS_EQUIP_AFER', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dt_calibracao = models.DateTimeField(db_column='DT_CALIBRACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EQUIPAMENTO_AFERICAO'

class ErrosMec(models.Model):
    cd_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='CD_PRODUTO')  # Field name made lowercase.
    cd_departamento = models.ForeignKey('Posto', models.DO_NOTHING, db_column='CD_DEPARTAMENTO', to_field='cd_departamento', blank=True, null=True)  # Field name made lowercase.
    cd_setor = models.ForeignKey('Posto', models.DO_NOTHING, db_column='CD_SETOR', to_field='cd_setor', related_name='errosmec_cd_setor_set', blank=True, null=True)  # Field name made lowercase.
    cd_linha = models.ForeignKey('Posto', models.DO_NOTHING, db_column='CD_LINHA', to_field='cd_linha', related_name='errosmec_cd_linha_set', blank=True, null=True)  # Field name made lowercase.
    cd_posto = models.ForeignKey('Posto', models.DO_NOTHING, db_column='CD_POSTO', to_field='cd_posto', related_name='errosmec_cd_posto_set', blank=True, null=True)  # Field name made lowercase.
    nro_serie = models.IntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    nro_pagamento = models.IntegerField(db_column='NRO_PAGAMENTO')  # Field name made lowercase.
    erro = models.CharField(db_column='ERRO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ds_erro = models.CharField(db_column='DS_ERRO', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    dt_erro = models.DateTimeField(db_column='DT_ERRO', blank=True, null=True)  # Field name made lowercase.
    temp = models.DecimalField(db_column='TEMP', max_digits=3, decimal_places=1, blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERROS_MEC'

class ErroTemp(models.Model):
    erro = models.CharField(db_column='ERRO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    ds_erro = models.CharField(db_column='DS_ERRO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    comando = models.CharField(db_column='COMANDO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERRO_TEMP'

class Especificacoes(models.Model):
    magnus = models.OneToOneField('Modelos', models.DO_NOTHING, db_column='MAGNUS', primary_key=True)  # Field name made lowercase. The composite primary key (MAGNUS, COD_PERTO) found, that is not supported. The first column is selected.
    cod_perto = models.CharField(db_column='COD_PERTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    ds_produto = models.CharField(db_column='DS_PRODUTO', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    peso = models.IntegerField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    altura = models.IntegerField(db_column='ALTURA', blank=True, null=True) # Field name made lowercase.
    largura = models.IntegerField(db_column='LARGURA', blank=True, null=True)  # Field name made lowercase.
    profundidade = models.IntegerField(db_column='PROFUNDIDADE', blank=True, null=True) # Field name made lowercase.
    msg = models.CharField(db_column='MSG', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ds_produto_ingles = models.CharField(db_column='DS_PRODUTO_INGLES', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ds_produto_espanhol = models.CharField(db_column='DS_PRODUTO_ESPANHOL', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    msg_ingles = models.CharField(db_column='MSG_INGLES', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    msg_espanhol = models.CharField(db_column='MSG_ESPANHOL', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nro_contrato = models.CharField(db_column='NRO_CONTRATO', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    proc_compra = models.CharField(db_column='PROC_COMPRA', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ativo = models.CharField(db_column='ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    idioma = models.CharField(db_column='IDIOMA', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESPECIFICACOES'
        unique_together = (('magnus', 'cod_perto'),)

class EtiquetaSerie(models.Model):
    id_etiq = models.AutoField(db_column='ID_ETIQ', primary_key=True) # Field name made lowercase.
    magnus = models.ForeignKey('Modelos', models.DO_NOTHING, db_column='MAGNUS') # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    data_etiq = models.DateTimeField(db_column='DATA_ETIQ') # Field name made lowercase.
    matricula = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='MATRICULA', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETIQUETA_SERIE'

class Inspecao(models.Model):
    id_inspecao = models.IntegerField(db_column='ID_INSPECAO', primary_key=True) # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    matricula = models.IntegerField(db_column='MATRICULA', blank=True, null=True) # Field name made lowercase.
    serie = models.IntegerField(db_column='SERIE', blank=True, null=True)  # Field name made lowercase.
    lacre_micro = models.IntegerField(db_column='LACRE_MICRO', blank=True, null=True) # Field name made lowercase.
    dt_ini = models.DateTimeField(db_column='DT_INI', blank=True, null=True) # Field name made lowercase.
    dt_fim = models.DateTimeField(db_column='DT_FIM', blank=True, null=True) # Field name made lowercase.
    resp_montagem = models.IntegerField(db_column='RESP_MONTAGEM', blank=True, null=True)  # Field name made lowercase.
    resp_teste = models.IntegerField(db_column='RESP_TESTE', blank=True, null=True) # Field name made lowercase.
    resp_retsubcj = models.IntegerField(db_column='RESP_RETSUBCJ', blank=True, null=True)  # Field name made lowercase.
    resp_retgeral = models.IntegerField(db_column='RESP_RETGERAL', blank=True, null=True) #) Field name made lowercase.
    observacao = models.CharField(db_column='OBSERVACAO', max_length=2048, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nr_lacre_anti = models.IntegerField(db_column='NR_LACRE_ANTI', blank=True, null=True) # Field name made lowercase.
    nr_anti_painel = models.IntegerField(db_column='NR_ANTI_PAINEL', blank=True, null=True)  # Field name made lowercase.
    nr_cash = models.IntegerField(db_column='NR_CASH', blank=True, null=True) # Field name made lowercase.
    nr_serie_micro = models.IntegerField(db_column='NR_SERIE_MICRO', blank=True, null=True)  # Field name made lowercase.
    nr_serie_depositario = models.IntegerField(db_column='NR_SERIE_DEPOSITARIO', blank=True, null=True) # Field name made lowercase.
    nr_serie_impressora = models.IntegerField(db_column='NR_SERIE_IMPRESSORA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INSPECAO'

class ItensChecklist(models.Model):
    id_item = models.IntegerField(db_column='ID_ITEM', primary_key=True)  # Field name made lowercase.
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=85, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ativo = models.CharField(db_column='ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    cd_periferico = models.BigIntegerField(db_column='CD_PERIFERICO', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITENS_CHECKLIST'

class ItensInspecionados(models.Model):
    id_seq = models.AutoField(db_column='ID_SEQ', primary_key=True) # Field name made lowercase.
    id_inspecao = models.IntegerField(db_column='ID_INSPECAO') # Field name made lowercase.
    id_item = models.IntegerField(db_column='ID_ITEM') # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obs_defeito = models.CharField(db_column='OBS_DEFEITO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITENS_INSPECIONADOS'

class LicencaAtm(models.Model):
    id_lic = models.AutoField(db_column='ID_LIC', primary_key=True) # Field name made lowercase.
    cd_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='CD_PRODUTO') # Field name made lowercase.
    licenca = models.CharField(db_column='LICENCA', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LICENCA_ATM'

class Linha(models.Model):
    cd_departamento = models.OneToOneField('Setor', models.DO_NOTHING, db_column='CD_DEPARTAMENTO', primary_key=True)  # Field name made lowercase. The composite primary key (CD_DEPARTAMENTO, CD_SETOR, CD_LINHA) found, that is not supported. The first column is selected.
    cd_setor = models.OneToOneField('Setor', models.DO_NOTHING, db_column='CD_SETOR', to_field='cd_setor', related_name='linha_cd_setor_set')  # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', unique=True)  # Field name made lowercase.
    ds_linha = models.CharField(db_column='DS_LINHA', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    exige_seq_linha = models.CharField(db_column='EXIGE_SEQ_LINHA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LINHA'
        unique_together = (('cd_departamento', 'cd_setor', 'cd_linha'),)

class LocalDefeito(models.Model):
    cd_local_defeito = models.IntegerField(db_column='CD_LOCAL_DEFEITO', primary_key=True)  # Field name made lowercase.
    ds_local_defeito = models.CharField(db_column='DS_LOCAL_DEFEITO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    aceita_cod = models.CharField(db_column='ACEITA_COD', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCAL_DEFEITO'

class LocalDefeitoSmp(models.Model):
    cd_local_defeito_smp = models.IntegerField(db_column='CD_LOCAL_DEFEITO_SMP', primary_key=True) # Field name made lowercase.
    ds_local_defeito_smp = models.CharField(db_column='DS_LOCAL_DEFEITO_SMP', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCAL_DEFEITO_SMP'

class MacSerie(models.Model):
    cd_produto = models.OneToOneField('Produto', models.DO_NOTHING, db_column='CD_PRODUTO', primary_key=True)  # Field name made lowercase. The composite primary key (CD_PRODUTO, NRO_SERIE, NRO_MACfound, that is not supported. The first column is selected.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    nro_mac = models.CharField(db_column='NRO_MAC', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAC_SERIE'
        unique_together = (('cd_produto', 'nro_serie', 'nro_mac'),)

class Medidas(models.Model):
    id_medida = models.BigAutoField(db_column='ID_MEDIDA', primary_key=True)  # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    ind_prod = models.BigIntegerField(db_column='IND_PROD')  # Field name made lowercase.
    nro_serie = models.IntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    id_tp_medida = models.IntegerField(db_column='ID_TP_MEDIDA')  # Field name made lowercase.
    id_tp_local = models.IntegerField(db_column='ID_TP_LOCAL')  # Field name made lowercase.
    medida = models.FloatField(db_column='MEDIDA', blank=True, null=True) # Field name made lowercase.
    max = models.FloatField(db_column='MAX', blank=True, null=True)  # Field name made lowercase.
    min = models.FloatField(db_column='MIN', blank=True, null=True) # Field name made lowercase.
    dt_medida = models.DateTimeField(db_column='DT_MEDIDA')  # Field name made lowercase.
    resultado = models.CharField(db_column='RESULTADO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDIDAS'

class MedidasSmp(models.Model):
    id_medidas = models.AutoField(db_column='ID_MEDIDAS', primary_key=True) # Field name made lowercase.
    cd_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='CD_PRODUTO') # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    cd_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='CD_DEPARTAMENTO') # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    id_tp_medida = models.ForeignKey('TipoItens', models.DO_NOTHING, db_column='ID_TP_MEDIDA') # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDIDAS_SMP'

class MedidaDuplasMec(models.Model):
    id_medida_dupla = models.AutoField(db_column='ID_MEDIDA_DUPLA', primary_key=True)  # Field name made lowercase.
    cd_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='CD_PRODUTO')  # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE') # Field name made lowercase.
    pmt1 = models.IntegerField(db_column='PMT1') # Field name made lowercase.
    pmt2 = models.IntegerField(db_column='PMT2') # Field name made lowercase.
    temp = models.FloatField(db_column='TEMP') # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA')  # Field name made lowercase.
    pgto = models.IntegerField(db_column='PGTO')  # Field name made lowercase.
    id_camara = models.ForeignKey(CamarasTermicas, models.DO_NOTHING, db_column='ID_CAMARA')  # Field name made lowercase.
    temp2 = models.FloatField(db_column='TEMP2', blank=True, null=True) # Field name made lowercase.
    ref_pmt1 = models.SmallIntegerField(db_column='REF_PMT1', blank=True, null=True) # Field name made lowercase.
    ref_pmt2 = models.SmallIntegerField(db_column='REF_PMT2', blank=True, null=True) # Field name made lowercase.
    ind_prod = models.BigIntegerField(db_column='IND_PROD', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDIDA_DUPLAS_MEC'

class MedidaDuplasMec2(models.Model):
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    pmt1 = models.IntegerField(db_column='PMT1', blank=True, null=True) # Field name made lowercase.
    pmt2 = models.IntegerField(db_column='PMT2', blank=True, null=True)  # Field name made lowercase.
    temp = models.FloatField(db_column='TEMP', blank=True, null=True) # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True) # Field name made lowercase.
    pgto = models.IntegerField(db_column='PGTO', blank=True, null=True)  # Field name made lowercase.
    camara = models.IntegerField(db_column='CAMARA', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEDIDA_DUPLAS_MEC_2'

class Menu(models.Model):
    id_menu = models.AutoField(db_column='ID_MENU', primary_key=True) # Field name made lowercase.
    id_tp_menu = models.ForeignKey('TipoItens', models.DO_NOTHING, db_column='ID_TP_MENU', blank=True, null=True)  # Field name made lowercase.
    ds_menu = models.CharField(db_column='DS_MENU', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    caminho_exe = models.CharField(db_column='CAMINHO_EXE', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    seq = models.BigIntegerField(db_column='SEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MENU'

class Modelo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dt_create = models.DateTimeField(db_column='DT_CREATE') # Field name made lowercase.
    dt_update = models.DateTimeField(db_column='DT_UPDATE')  # Field name made lowercase.
    dt_delete = models.DateTimeField(db_column='DT_DELETE', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', unique=True, max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    id_status = models.BigIntegerField(db_column='ID_STATUS') # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODELO'

class Modelos(models.Model):
    magnus = models.CharField(db_column='MAGNUS', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    exige_serie = models.CharField(db_column='EXIGE_SERIE', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    exige_serie_disp = models.CharField(db_column='EXIGE_SERIE_DISP', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    exige_serie_dep = models.CharField(db_column='EXIGE_SERIE_DEP', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    exige_digito_disp = models.CharField(db_column='EXIGE_DIGITO_DISP', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    exige_digito_dep = models.CharField(db_column='EXIGE_DIGITO_DEP', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    imprime_relatorios = models.CharField(db_column='IMPRIME_RELATORIOS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    exibe_msg_paop = models.CharField(db_column='EXIBE_MSG_PAOP', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    tempo_runin = models.IntegerField(db_column='TEMPO_RUNIN') # Field name made lowercase.
    reinicia_liberacao = models.CharField(db_column='REINICIA_LIBERACAO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    tentativas_liberacao = models.IntegerField(db_column='TENTATIVAS_LIBERACAO') # Field name made lowercase.
    texto_runin = models.CharField(db_column='TEXTO_RUNIN', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    texto_liberacao = models.CharField(db_column='TEXTO_LIBERACAO', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    texto_integracao = models.CharField(db_column='TEXTO_INTEGRACAO', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    in_ativo = models.CharField(db_column='IN_ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODELOS'





class Modtest(models.Model):
    magnus = models.CharField(db_column='MAGNUS', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (MAGNUS, ORDEM) found, that is not supported. The first column is selected.
    ordem = models.IntegerField(db_column='ORDEM')  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODTEST'
        unique_together = (('magnus', 'ordem'),)

class MontaChecklist(models.Model):
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    id_item = models.IntegerField(db_column='ID_ITEM') # Field name made lowercase.
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MONTA_CHECKLIST'

class NivesMenu(models.Model):
    cd_matricula = models.IntegerField(db_column='CD_MATRICULA') # Field name made lowercase.
    id_menu = models.IntegerField(db_column='ID_MENU') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NIVES_MENU'

class Posto(models.Model):
    cd_departamento = models.OneToOneField(Linha, models.DO_NOTHING, db_column='CD_DEPARTAMENTO', primary_key=True) # Field name made lowercase. The composite primary key (CD_DEPARTAMENTO, CD_SETOR, CD_LINHA, CD_POSTOfound, that is not supported. The first column is selected.
    cd_setor = models.OneToOneField(Linha, models.DO_NOTHING, db_column='CD_SETOR', to_field='cd_setor', related_name='posto_cd_setor_set') # Field name made lowercase.
    cd_linha = models.OneToOneField(Linha, models.DO_NOTHING, db_column='CD_LINHA', to_field='cd_linha', related_name='posto_cd_linha_set') # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', unique=True) # Field name made lowercase.
    ds_posto = models.CharField(db_column='DS_POSTO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POSTO'
        unique_together = (('cd_departamento', 'cd_setor', 'cd_linha', 'cd_posto'),)

class PreTeste(models.Model):
    cd_produto = models.CharField(db_column='CD_PRODUTO', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (CD_PRODUTO, IND_TESTE, NRO_SERIEfound, that is not supported. The first column is selected.
    ind_teste = models.IntegerField(db_column='IND_TESTE') # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    cd_local_defeito_smp = models.IntegerField(db_column='CD_LOCAL_DEFEITO_SMP', blank=True, null=True) # Field name made lowercase.
    cd_equip_afer = models.CharField(db_column='CD_EQUIP_AFER', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    matricula = models.IntegerField(db_column='MATRICULA') # Field name made lowercase.
    cd_local_defeito = models.IntegerField(db_column='CD_LOCAL_DEFEITO', blank=True, null=True)  # Field name made lowercase.
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_defeito = models.IntegerField(db_column='CD_DEFEITO', blank=True, null=True) # Field name made lowercase.
    cd_defeito_smp = models.IntegerField(db_column='CD_DEFEITO_SMP', blank=True, null=True)  # Field name made lowercase.
    dt_ini_teste = models.DateTimeField(db_column='DT_INI_TESTE') # Field name made lowercase.
    dt_fim_teste = models.DateTimeField(db_column='DT_FIM_TESTE')  # Field name made lowercase.
    nr_it = models.CharField(db_column='NR_IT', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    obs_pre_teste = models.CharField(db_column='OBS_PRE_TESTE', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    cd_perto_pre_teste = models.CharField(db_column='CD_PERTO_PRE_TESTE', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    pos_componente = models.CharField(db_column='POS_COMPONENTE', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lado_placa = models.CharField(db_column='LADO_PLACA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    firmware = models.CharField(db_column='FIRMWARE', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    nro_lote = models.CharField(db_column='NRO_LOTE', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRE_TESTE'
        unique_together = (('cd_produto', 'ind_teste', 'nro_serie'),)

class Processista(models.Model):
    matricula = models.IntegerField(db_column='MATRICULA', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROCESSISTA'

class Producao(models.Model):
    ind_producao = models.AutoField(db_column='IND_PRODUCAO', primary_key=True)  # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase. The composite primary key (CD_PRODUTO, IND_PRODUCAO, NRO_SERIEfound, that is not supported. The first column is selected.
    nro_serie = models.IntegerField(db_column='NRO_SERIE') # Field name made lowercase.
    matricula = models.IntegerField(db_column='MATRICULA') # Field name made lowercase.
    dt_ini_prod = models.DateTimeField(db_column='DT_INI_PROD')  # Field name made lowercase.
    dt_fim_prod = models.DateTimeField(db_column='DT_FIM_PROD', blank=True, null=True)  # Field name made lowercase.
    modos = models.SmallIntegerField(db_column='MODOS') # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='ESTADO')  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True) # Field name made lowercase.
    extra = models.CharField(db_column='EXTRA', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCAO'
        unique_together = (('cd_produto', 'ind_producao', 'nro_serie'),)

class Produto(models.Model):
    cd_produto = models.CharField(db_column='CD_PRODUTO', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ds_produto = models.CharField(db_column='DS_PRODUTO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    exige_obs_teste = models.CharField(db_column='EXIGE_OBS_TESTE', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    controle_seq_prod = models.CharField(db_column='CONTROLE_SEQ_PROD', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    in_ativo = models.CharField(db_column='IN_ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    in_jiga = models.CharField(db_column='IN_JIGA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    caminho_aplic = models.CharField(db_column='CAMINHO_APLIC', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    exige_com_jiga = models.CharField(db_column='EXIGE_COM_JIGA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    exige_com_periferico = models.CharField(db_column='EXIGE_COM_PERIFERICO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    in_smp = models.CharField(db_column='IN_SMP', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    caminho_aplic_man = models.CharField(db_column='CAMINHO_APLIC_MAN', max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    cd_departamento = models.ForeignKey('Setor', models.DO_NOTHING, db_column='CD_DEPARTAMENTO', to_field='cd_departamento', blank=True, null=True) # Field name made lowercase.
    cd_setor = models.ForeignKey('Setor', models.DO_NOTHING, db_column='CD_SETOR', to_field='cd_setor', related_name='produto_cd_setor_set', blank=True, null=True)  # Field name made lowercase.
    in_param_padrao = models.CharField(db_column='IN_PARAM_PADRAO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    firmware = models.CharField(db_column='FIRMWARE', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'PRODUTO'
        
    

class ProdutoModelo(models.Model):
    magnus = models.CharField(db_column='MAGNUS', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase. The composite primary key (MAGNUS, CD_PRODUTO) found, that is not supported. The first column is selected.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTO_MODELO'
        unique_together = (('magnus', 'cd_produto'), ('magnus', 'cd_produto'),)

class ProdutoPerife(models.Model):
    id_prope = models.AutoField(db_column='ID_PROPE', primary_key=True)  # Field name made lowercase.
    cd_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='CD_PRODUTO')  # Field name made lowercase.
    nro_serie_prod = models.BigIntegerField(db_column='NRO_SERIE_PROD') # Field name made lowercase.
    cd_periferico = models.ForeignKey(Produto, models.DO_NOTHING, db_column='CD_PERIFERICO', related_name='produtoperife_cd_periferico_set') # Field name made lowercase.
    nro_serie_peri = models.BigIntegerField(db_column='NRO_SERIE_PERI', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTO_PERIFE'

class PvConfig(models.Model):
    v_dll_ppay = models.CharField(db_column='V_DLL_PPAY', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    v_dll_pertotalk = models.CharField(db_column='V_DLL_PERTOTALK', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    padrao_barras = models.CharField(db_column='PADRAO_BARRAS', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    padrao_barras_service = models.CharField(db_column='PADRAO_BARRAS_SERVICE', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    padrao_cartao = models.CharField(db_column='PADRAO_CARTAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    limite_bateria = models.DecimalField(db_column='LIMITE_BATERIA', max_digits=4, decimal_places=2, blank=True, null=True) # Field name made lowercase.
    tipo_discagem = models.CharField(db_column='TIPO_DISCAGEM', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tentativas_discagem = models.IntegerField(db_column='TENTATIVAS_DISCAGEM', blank=True, null=True) # Field name made lowercase.
    aplic_remoto = models.CharField(db_column='APLIC_REMOTO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aplic_tcp = models.CharField(db_column='APLIC_TCP', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    aplic_terminal = models.CharField(db_column='APLIC_TERMINAL', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    company_id = models.CharField(db_column='COMPANY_ID', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    aplic_filetran = models.CharField(db_column='APLIC_FILETRAN', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    padrao_atr = models.CharField(db_column='PADRAO_ATR', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_CONFIG'

class PvDefeitoResultados(models.Model):
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    serie_maquina = models.CharField(db_column='SERIE_MAQUINA', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    seq_defeito = models.AutoField(db_column='SEQ_DEFEITO', primary_key=True) # Field name made lowercase.
    cd_local_defeito = models.IntegerField(db_column='CD_LOCAL_DEFEITO') # Field name made lowercase.
    cd_defeito = models.IntegerField(db_column='CD_DEFEITO') # Field name made lowercase.
    sc_defeito = models.CharField(db_column='SC_DEFEITO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_DEFEITO_RESULTADOS'

class PvEstacao(models.Model):
    cd_estacao = models.IntegerField(db_column='CD_ESTACAO', primary_key=True) # Field name made lowercase.
    ds_estacao = models.CharField(db_column='DS_ESTACAO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    in_ativo = models.CharField(db_column='IN_ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    caminho_log = models.CharField(db_column='CAMINHO_LOG', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    com_estacao = models.IntegerField(db_column='COM_ESTACAO', blank=True, null=True)  # Field name made lowercase.
    ramal = models.IntegerField(db_column='RAMAL', blank=True, null=True) # Field name made lowercase.
    ip_maquina = models.CharField(db_column='IP_MAQUINA', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    mascara_ip = models.CharField(db_column='MASCARA_IP', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    gateway = models.CharField(db_column='GATEWAY', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    porta = models.IntegerField(db_column='PORTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_ESTACAO'

class PvFonte(models.Model):
    cd_fonte = models.CharField(db_column='CD_FONTE', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ds_fonte = models.CharField(db_column='DS_FONTE', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    in_ativo = models.CharField(db_column='IN_ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_FONTE'

class PvMac(models.Model):
    nro_mac = models.CharField(db_column='NRO_MAC', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    utilizado = models.CharField(db_column='UTILIZADO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    serie_maquina = models.IntegerField(db_column='SERIE_MAQUINA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_MAC'

class PvModelo(models.Model):
    cd_modelo = models.CharField(db_column='CD_MODELO', primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_MODELO'

class PvModem(models.Model):
    cd_modem = models.IntegerField(db_column='CD_MODEM', primary_key=True) # Field name made lowercase.
    ds_modem = models.CharField(db_column='DS_MODEM', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    param_inicializacao = models.CharField(db_column='PARAM_INICIALIZACAO', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    telefone_renpac = models.CharField(db_column='TELEFONE_RENPAC', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_MODEM'

class PvProduto(models.Model):
    cd_produto = models.CharField(db_column='CD_PRODUTO', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_modelo = models.ForeignKey(PvModelo, models.DO_NOTHING, db_column='CD_MODELO')  # Field name made lowercase.
    cd_caracteristica = models.ForeignKey('PvTipoMaquina', models.DO_NOTHING, db_column='CD_CARACTERISTICA', blank=True, null=True) # Field name made lowercase.
    cd_fonte = models.ForeignKey(PvFonte, models.DO_NOTHING, db_column='CD_FONTE', blank=True, null=True)  # Field name made lowercase.
    cd_modem = models.ForeignKey(PvModem, models.DO_NOTHING, db_column='CD_MODEM', blank=True, null=True) # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    fw_produto = models.CharField(db_column='FW_PRODUTO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_teste = models.CharField(db_column='FW_TESTE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_interface = models.CharField(db_column='FW_INTERFACE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_fiscal = models.CharField(db_column='FW_FISCAL', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_conectividade = models.CharField(db_column='FW_CONECTIVIDADE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_printer = models.CharField(db_column='FW_PRINTER', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    v_pertosys = models.CharField(db_column='V_PERTOSYS', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    v_remoto = models.CharField(db_column='V_REMOTO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    identificacao = models.CharField(db_column='IDENTIFICACAO', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    path_sw = models.CharField(db_column='PATH_SW', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    carregar_remoto = models.CharField(db_column='CARREGAR_REMOTO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    carregar_tcp = models.CharField(db_column='CARREGAR_TCP', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    carregar_terminal = models.CharField(db_column='CARREGAR_TERMINAL', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    tamanho_flash = models.IntegerField(db_column='TAMANHO_FLASH', blank=True, null=True)  # Field name made lowercase.
    tamanho_ram = models.IntegerField(db_column='TAMANHO_RAM', blank=True, null=True) # Field name made lowercase.
    carregar_aplic_cliente = models.CharField(db_column='CARREGAR_APLIC_CLIENTE', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    caminho_aplic_cliente = models.CharField(db_column='CAMINHO_APLIC_CLIENTE', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipo_cpu = models.CharField(db_column='TIPO_CPU', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    testar_guilhotina = models.CharField(db_column='TESTAR_GUILHOTINA', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_PRODUTO'

class PvResult(models.Model):
    seq_result = models.AutoField(db_column='SEQ_RESULT', primary_key=True)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    serie_maquina = models.CharField(db_column='SERIE_MAQUINA', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nro_teste = models.IntegerField(db_column='NRO_TESTE')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_RESULT'

class PvSmart(models.Model):
    caminho_smart = models.CharField(db_column='CAMINHO_SMART', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_SMART'

class PvTestes(models.Model):
    seq = models.IntegerField(db_column='SEQ', primary_key=True)  # Field name made lowercase. The composite primary key (SEQ, CD_PRODUTO, SERIE_MAQUINAfound, that is not supported. The first column is selected.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_fonte = models.CharField(db_column='CD_FONTE', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    serie_maquina = models.CharField(db_column='SERIE_MAQUINA', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    serie_fonte = models.IntegerField(db_column='SERIE_FONTE', blank=True, null=True)  # Field name made lowercase.
    serie_cpu = models.IntegerField(db_column='SERIE_CPU', blank=True, null=True) # Field name made lowercase.
    dt_ini = models.DateTimeField(db_column='DT_INI')  # Field name made lowercase.
    dt_fim = models.DateTimeField(db_column='DT_FIM', blank=True, null=True)  # Field name made lowercase.
    matricula = models.IntegerField(db_column='MATRICULA')  # Field name made lowercase.
    v_pertosys = models.CharField(db_column='V_PERTOSYS', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    v_remoto = models.CharField(db_column='V_REMOTO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_interface = models.CharField(db_column='FW_INTERFACE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_conectividade = models.CharField(db_column='FW_CONECTIVIDADE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_printer = models.CharField(db_column='FW_PRINTER', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_fiscal = models.CharField(db_column='FW_FISCAL', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_teste = models.CharField(db_column='FW_TESTE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fw_produto = models.CharField(db_column='FW_PRODUTO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    in_retrabalho = models.CharField(db_column='IN_RETRABALHO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    serie_modem = models.IntegerField(db_column='SERIE_MODEM', blank=True, null=True) # Field name made lowercase.
    serie_mfd = models.BigIntegerField(db_column='SERIE_MFD', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_TESTES'
        unique_together = (('seq', 'cd_produto', 'serie_maquina'),)

class PvTipoMaquina(models.Model):
    cd_caracteristica = models.CharField(db_column='CD_CARACTERISTICA', primary_key=True, max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PV_TIPO_MAQUINA'

class RecuperaAtm(models.Model):
    indice = models.OneToOneField('Resultados', models.DO_NOTHING, db_column='INDICE', primary_key=True) # Field name made lowercase.
    matricula = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='MATRICULA')  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA') # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECUPERA_ATM'

class Resultados(models.Model):
    indice = models.AutoField(db_column='INDICE', primary_key=True) # Field name made lowercase.
    magnus = models.ForeignKey(Modelos, models.DO_NOTHING, db_column='MAGNUS', blank=True, null=True)  # Field name made lowercase.
    serie = models.BigIntegerField(db_column='SERIE', blank=True, null=True)  # Field name made lowercase.
    seriedisp = models.IntegerField(db_column='SERIEDISP', blank=True, null=True) # Field name made lowercase.
    seriedep = models.IntegerField(db_column='SERIEDEP', blank=True, null=True)  # Field name made lowercase.
    dataini = models.DateTimeField(db_column='DATAINI', blank=True, null=True)  # Field name made lowercase.
    datafim = models.DateTimeField(db_column='DATAFIM', blank=True, null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='ESTADO', blank=True, null=True)  # Field name made lowercase.
    matricula = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='MATRICULA', blank=True, null=True)  # Field name made lowercase.
    temporunin = models.SmallIntegerField(db_column='TEMPORUNIN', blank=True, null=True)  # Field name made lowercase.
    modos = models.SmallIntegerField(db_column='MODOS', blank=True, null=True)  # Field name made lowercase.
    matricula_runin = models.IntegerField(db_column='MATRICULA_RUNIN', blank=True, null=True) # Field name made lowercase.
    matricula_liberacao = models.IntegerField(db_column='MATRICULA_LIBERACAO', blank=True, null=True)  # Field name made lowercase.
    cod_teste_reinicio = models.IntegerField(db_column='COD_TESTE_REINICIO', blank=True, null=True) # Field name made lowercase.
    dataini_runin = models.DateTimeField(db_column='DATAINI_RUNIN', blank=True, null=True) # Field name made lowercase.
    dataini_liberacao = models.DateTimeField(db_column='DATAINI_LIBERACAO', blank=True, null=True) # Field name made lowercase.
    obs_recuperada = models.CharField(db_column='OBS_RECUPERADA', max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESULTADOS'

class ResultadosDadosEntrada(models.Model):
    magnus = models.CharField(db_column='MAGNUS', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    serie_atm = models.BigIntegerField(db_column='SERIE_ATM', primary_key=True) # Field name made lowercase. The composite primary key (SERIE_ATM, MAGNUS, CD_PRODUTOfound, that is not supported. The first column is selected.
    serie = models.CharField(db_column='SERIE', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESULTADOS_DADOS_ENTRADA'
        unique_together = (('serie_atm', 'magnus', 'cd_produto'), ('serie_atm', 'magnus', 'cd_produto'),)

class ResultadosTemp(models.Model):
    indice = models.IntegerField(db_column='INDICE') # Field name made lowercase.
    magnus = models.CharField(db_column='MAGNUS', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    seriedisp = models.IntegerField(db_column='SERIEDISP', blank=True, null=True)  # Field name made lowercase.
    seriedep = models.IntegerField(db_column='SERIEDEP', blank=True, null=True) # Field name made lowercase.
    dataini = models.DateTimeField(db_column='DATAINI', blank=True, null=True) # Field name made lowercase.
    datafim = models.DateTimeField(db_column='DATAFIM', blank=True, null=True) # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='ESTADO', blank=True, null=True) # Field name made lowercase.
    matricula = models.IntegerField(db_column='MATRICULA', blank=True, null=True)  # Field name made lowercase.
    temporunin = models.SmallIntegerField(db_column='TEMPORUNIN', blank=True, null=True)  # Field name made lowercase.
    modos = models.SmallIntegerField(db_column='MODOS', blank=True, null=True)  # Field name made lowercase.
    matricula_runin = models.IntegerField(db_column='MATRICULA_RUNIN', blank=True, null=True) # Field name made lowercase.
    matricula_liberacao = models.IntegerField(db_column='MATRICULA_LIBERACAO', blank=True, null=True)  # Field name made lowercase.
    cod_teste_reinicio = models.IntegerField(db_column='COD_TESTE_REINICIO', blank=True, null=True) # Field name made lowercase.
    dataini_runin = models.DateTimeField(db_column='DATAINI_RUNIN', blank=True, null=True) # Field name made lowercase.
    dataini_liberacao = models.DateTimeField(db_column='DATAINI_LIBERACAO', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESULTADOS_TEMP'

class SeqProd(models.Model):
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', primary_key=True, max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase. The composite primary key (CD_DEPARTAMENTO, CD_SETOR, CD_LINHA, CD_POSTO, CD_PRODUTOfound, that is not supported. The first column is selected.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    seq_producao = models.IntegerField(db_column='SEQ_PRODUCAO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEQ_PROD'
        unique_together = (('cd_departamento', 'cd_setor', 'cd_linha', 'cd_posto', 'cd_produto'),)

class SerieMec(models.Model):
    serie_presenter = models.IntegerField(db_column='SERIE_PRESENTER', blank=True, null=True) # Field name made lowercase.
    serie_placa_presenter = models.IntegerField(db_column='SERIE_PLACA_PRESENTER', blank=True, null=True)  # Field name made lowercase.
    serie_dupla_detec = models.IntegerField(db_column='SERIE_DUPLA_DETEC', blank=True, null=True) # Field name made lowercase.
    serie_modulo_duplo = models.IntegerField(db_column='SERIE_MODULO_DUPLO', blank=True, null=True)  # Field name made lowercase.
    serie_modulo_simples = models.IntegerField(db_column='SERIE_MODULO_SIMPLES', blank=True, null=True) # Field name made lowercase.
    serie_cpu = models.IntegerField(db_column='SERIE_CPU', blank=True, null=True)  # Field name made lowercase.
    serie_mecanismo = models.IntegerField(db_column='SERIE_MECANISMO', primary_key=True)  # Field name made lowercase. The composite primary key (SERIE_MECANISMO, COD_MECANISMOfound, that is not supported. The first column is selected.
    cod_mecanismo = models.CharField(db_column='COD_MECANISMO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    serie_extensor = models.IntegerField(db_column='SERIE_EXTENSOR', blank=True, null=True) # Field name made lowercase.
    serie_placa_pot = models.IntegerField(db_column='SERIE_PLACA_POT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERIE_MEC'
        unique_together = (('serie_mecanismo', 'cod_mecanismo'), ('serie_mecanismo', 'cod_mecanismo'),)

class SeriePerifericos(models.Model):
    cd_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='CD_PRODUTO')  # Field name made lowercase.
    matricula = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='MATRICULA') # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERIE_PERIFERICOS'

class Setor(models.Model):
    cd_departamento = models.OneToOneField(Departamento, models.DO_NOTHING, db_column='CD_DEPARTAMENTO', primary_key=True) # Field name made lowercase. The composite primary key (CD_DEPARTAMENTO, CD_SETORfound, that is not supported. The first column is selected.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', unique=True) # Field name made lowercase.
    ds_setor = models.CharField(db_column='DS_SETOR', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SETOR'
        unique_together = (('cd_departamento', 'cd_setor'),)

class TempMec(models.Model):
    id_teme = models.AutoField(db_column='ID_TEME', primary_key=True) # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    nro_serie = models.BigIntegerField(db_column='NRO_SERIE') # Field name made lowercase.
    cd_departamento = models.CharField(db_column='CD_DEPARTAMENTO', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_linha = models.CharField(db_column='CD_LINHA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    cd_posto = models.CharField(db_column='CD_POSTO', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    id_tp_mec = models.IntegerField(db_column='ID_TP_MEC') # Field name made lowercase.
    valor = models.IntegerField(db_column='VALOR') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMP_MEC'

class Terminal(models.Model):
    nome = models.CharField(db_column='NOME', primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_departamento = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_DEPARTAMENTO', to_field='cd_departamento') # Field name made lowercase.
    cd_setor = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_SETOR', to_field='cd_setor', related_name='terminal_cd_setor_set')  # Field name made lowercase.
    cd_linha = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_LINHA', to_field='cd_linha', related_name='terminal_cd_linha_set') # Field name made lowercase.
    cd_posto = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_POSTO', to_field='cd_posto', related_name='terminal_cd_posto_set')  # Field name made lowercase.
    in_ativo = models.CharField(db_column='IN_ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TERMINAL'

class Testes(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modo = models.IntegerField(db_column='MODO', blank=True, null=True) # Field name made lowercase.
    aplicativo = models.CharField(db_column='APLICATIVO', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    parametro = models.CharField(db_column='PARAMETRO', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    observacao = models.CharField(db_column='OBSERVACAO', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    possui_runin = models.CharField(db_column='POSSUI_RUNIN', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    param_runin = models.CharField(db_column='PARAM_RUNIN', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TESTES'

class Testesres(models.Model):
    indice = models.AutoField(db_column='INDICE', primary_key=True) # Field name made lowercase.
    indiceres = models.IntegerField(db_column='INDICERES', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True) # Field name made lowercase.
    modo = models.IntegerField(db_column='MODO', blank=True, null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='ESTADO', blank=True, null=True)  # Field name made lowercase.
    extra = models.CharField(db_column='EXTRA', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TESTESRES'

class TesteDec(models.Model):
    tem = models.DecimalField(db_column='TEM', max_digits=5, decimal_places=1, blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TESTE_DEC'

class TesteSmc(models.Model):
    id_tesmc = models.AutoField(db_column='ID_TESMC', primary_key=True) # Field name made lowercase.
    turno = models.IntegerField(db_column='TURNO') # Field name made lowercase.
    cd_matricula = models.IntegerField(db_column='CD_MATRICULA') # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA')  # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    montador = models.IntegerField(db_column='MONTADOR') # Field name made lowercase.
    projeto = models.CharField(db_column='PROJETO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_setor = models.CharField(db_column='CD_SETOR', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TESTE_SMC'

class TesteTeclados(models.Model):
    magnus = models.CharField(db_column='MAGNUS', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='C¾digo do ATM')  # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', db_comment='C¾digo do PerifÚrico (produto)')  # Field name made lowercase.
    serie_atm = models.IntegerField(db_column='SERIE_ATM', primary_key=True, db_comment='N·mero de sÚrie do ATM') # Field name made lowercase. The composite primary key (SERIE_ATM, MAGNUS, CD_PRODUTOfound, that is not supported. The first column is selected.
    serie = models.BigIntegerField(db_column='SERIE', db_comment='nro de serie do perifÚrico a s')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TESTE_TECLADOS'
        unique_together = (('serie_atm', 'magnus', 'cd_produto'),)

class Tipos(models.Model):
    id_tipo = models.AutoField(db_column='ID_TIPO', primary_key=True)  # Field name made lowercase.
    ds_tipo = models.CharField(db_column='DS_TIPO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    nm_campo = models.CharField(db_column='NM_CAMPO', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS'

class TipoItens(models.Model):
    id_tp_item = models.AutoField(db_column='ID_TP_ITEM', primary_key=True) # Field name made lowercase.
    id_tipo = models.ForeignKey(Tipos, models.DO_NOTHING, db_column='ID_TIPO') # Field name made lowercase.
    cd_item = models.IntegerField(db_column='CD_ITEM') # Field name made lowercase.
    ds_item = models.CharField(db_column='DS_ITEM', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    sigla = models.CharField(db_column='SIGLA', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_ITENS'

class Usuarios(models.Model):
    matricula = models.IntegerField(db_column='MATRICULA', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    acesso = models.IntegerField(db_column='ACESSO', blank=True, null=True)  # Field name made lowercase.
    cd_acesso = models.ForeignKey(Acesso, models.DO_NOTHING, db_column='CD_ACESSO') # Field name made lowercase.
    in_ativo = models.CharField(db_column='IN_ATIVO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS'

class UsuarioPosto(models.Model):
    matricula = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='MATRICULA')  # Field name made lowercase.
    cd_departamento = models.OneToOneField(Posto, models.DO_NOTHING, db_column='CD_DEPARTAMENTO', primary_key=True) # Field name made lowercase. The composite primary key (CD_DEPARTAMENTO, CD_SETOR, CD_LINHA, MATRICULA, CD_POSTO) found, that is not supported. The first column is selected.
    cd_setor = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_SETOR', to_field='cd_setor', related_name='usuarioposto_cd_setor_set') # Field name made lowercase.
    cd_linha = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_LINHA', to_field='cd_linha', related_name='usuarioposto_cd_linha_set')  # Field name made lowercase.
    cd_posto = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_POSTO', to_field='cd_posto', related_name='usuarioposto_cd_posto_set') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIO_POSTO'
        unique_together = (('cd_departamento', 'cd_setor', 'cd_linha', 'matricula', 'cd_posto'),)

class ValoresTestes(models.Model):
    cd_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='CD_PRODUTO')  # Field name made lowercase.
    nro_serie = models.IntegerField(db_column='NRO_SERIE')  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True) # Field name made lowercase.
    grandeza = models.CharField(db_column='GRANDEZA', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    cd_departamento = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_DEPARTAMENTO', to_field='cd_departamento', blank=True, null=True) # Field name made lowercase.
    cd_setor = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_SETOR', to_field='cd_setor', related_name='valorestestes_cd_setor_set', blank=True, null=True)  # Field name made lowercase.
    cd_linha = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_LINHA', to_field='cd_linha', related_name='valorestestes_cd_linha_set', blank=True, null=True) # Field name made lowercase.
    cd_posto = models.ForeignKey(Posto, models.DO_NOTHING, db_column='CD_POSTO', to_field='cd_posto', related_name='valorestestes_cd_posto_set', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status_nr = models.IntegerField(db_column='STATUS_NR', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VALORES_TESTES'

class DefeitoResultadosBackup(models.Model):
    cd_defeito = models.IntegerField(blank=True, null=True)
    cd_local_defeito = models.IntegerField(blank=True, null=True)
    indice = models.IntegerField(blank=True, null=True)
    seq_defeito = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    sc_defeito = models.CharField(max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    modo_defeito = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    magnus_local = models.CharField(max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'defeito_resultados_backup'

class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS')
    value = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    uvalue = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)

class IndicesTmp(models.Model):
    indice = models.IntegerField(blank=True, null=True)
    magnus = models.CharField(max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    serie = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indices_tmp'

class Rastreabilidade(models.Model):
    cd_pai = models.CharField(db_column='CD_PAI', primary_key=True, max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase. The composite primary key (CD_PAI, CD_FILHO, SERIE_PAI) found, that is not supported. The first column is selected.
    cd_filho = models.CharField(db_column='CD_FILHO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    serie_pai = models.IntegerField(db_column='SERIE_PAI') # Field name made lowercase.
    serie_filho = models.IntegerField(db_column='SERIE_FILHO') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rastreabilidade'
        unique_together = (('cd_pai', 'cd_filho', 'serie_pai'),)

class SubProduto(models.Model):
    cd_pai = models.OneToOneField(Produto, models.DO_NOTHING, db_column='CD_PAI', primary_key=True) # Field name made lowercase. The composite primary key (CD_PAI, CD_FILHO) found, that is not supported. The first column is selected.
    cd_filho = models.CharField(db_column='CD_FILHO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_produto'
        unique_together = (('cd_pai', 'cd_filho'),)

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

class Tabelaresult(models.Model):
    seq = models.IntegerField(db_column='SEQ') # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    serie_maquina = models.CharField(db_column='SERIE_MAQUINA', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    seq_defeito = models.AutoField(db_column='SEQ_DEFEITO', primary_key=True)  # Field name made lowercase.
    cd_local_defeito = models.IntegerField(db_column='CD_LOCAL_DEFEITO')  # Field name made lowercase.
    cd_defeito = models.IntegerField(db_column='CD_DEFEITO')  # Field name made lowercase.
    sc_defeito = models.CharField(db_column='SC_DEFEITO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabelaRESULT'

class Tabelacop(models.Model):
    seq = models.IntegerField(db_column='SEQ') # Field name made lowercase.
    cd_produto = models.CharField(db_column='CD_PRODUTO', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    cd_fonte = models.CharField(db_column='CD_FONTE', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    serie_maquina = models.IntegerField(db_column='SERIE_MAQUINA')  # Field name made lowercase.
    serie_fonte = models.IntegerField(db_column='SERIE_FONTE', blank=True, null=True) # Field name made lowercase.
    serie_cpu = models.IntegerField(db_column='SERIE_CPU', blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateTimeField(db_column='DT_INI') # Field name made lowercase.
    dt_fim = models.DateTimeField(db_column='DT_FIM', blank=True, null=True) # Field name made lowercase.
    matricula = models.IntegerField(db_column='MATRICULA') # Field name made lowercase.
    v_pertosys = models.CharField(db_column='V_PERTOSYS', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    v_remoto = models.CharField(db_column='V_REMOTO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    fw_interface = models.CharField(db_column='FW_INTERFACE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    fw_conectividade = models.CharField(db_column='FW_CONECTIVIDADE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    fw_printer = models.CharField(db_column='FW_PRINTER', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    fw_fiscal = models.CharField(db_column='FW_FISCAL', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    fw_teste = models.CharField(db_column='FW_TESTE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    fw_produto = models.CharField(db_column='FW_PRODUTO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True) # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    in_retrabalho = models.CharField(db_column='IN_RETRABALHO', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS') # Field name made lowercase.
    serie_modem = models.IntegerField(db_column='SERIE_MODEM', blank=True, null=True)  # Field name made lowercase.
    serie_mfd = models.BigIntegerField(db_column='SERIE_MFD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tabelacop'