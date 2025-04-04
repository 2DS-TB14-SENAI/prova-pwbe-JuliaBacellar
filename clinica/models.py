from django.db import models


class Medico(models.Model):
    
    ESPECIALIDADES = {
        ( "CARDIO", "CARDIOLOGISTA"),
        ( "ONCO", "ONCOLOGISTA"),
        ( "CLI" , "CLINICO"),
    }
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=40, choices= ESPECIALIDADES)
    crm = models.CharField(max_length=80)
    email = models.EmailField(blank = True, null=True )



    def __str__(self):
        return self.nome


class Consulta(models.Model):
    
    STATUS = {
        ( "AGEND", "AGENDADO"),
        ( "REA", "REALIZADO"),
        ( "CANCEL" , "CANCELADO"),
    }
 
    paciente = models.CharField(max_length=80)
    data = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE )
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status 