from django.db import models

# Create your models here.


class SampleInf(models.Model):
    sample_id = models.CharField(max_length=200)
    tissue = models.CharField(max_length=200)

    def __str__(self):
        return f'<{self.sample_id} {self.tissue}>'


class Gene(models.Model):
    gene_id = models.CharField(max_length=200)

    def __str__(self):
        return f'<{self.gene_id}>'


class GeneExp(models.Model):
    sample_id = models.ForeignKey(SampleInf, on_delete=models.CASCADE)
    gene_id = models.ForeignKey(Gene, on_delete=models.CASCADE)
    tpm = models.FloatField(default=0)

    def __str__(self):
        return f'<{self.sample_id} {self.gene_id} {self.tpm}>'
