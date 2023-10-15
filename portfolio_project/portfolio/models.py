from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_name=models.CharField(max_length=50)
    experience=models.PositiveIntegerField()
    icon=models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name
class Project(models.Model):
    project_name=models.CharField(max_length=50)
    project_img=models.URLField(null=False)
    project_link=models.URLField(null=True,default="#")
    project_code=models.URLField(null=True,default="#")
    skill_used=models.ManyToManyField(Skill,related_name="project_skill")
    def __str__(self):
        return self.project_name
