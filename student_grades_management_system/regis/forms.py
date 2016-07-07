from django import forms


CHOICEPROG=(
    (1,'B.Tech'),
    (2,'M.Tech'),
)

CHOICEDEPT=(
    (1,'CSE'),
    (2,'CIVIL'),
    (3,'MECHANICAL'),
    (4,'ELECTRICAL'),
    (5,'META'),
    (6,'ECE'),
    (7,'PRODUCTION'),
)

CHOICEDEPTT=(
    (1,'CSE'),
    (2,'ECE'),
    (3,'SOFTSKILLS'),
    (4,'MATHEMATICS'),
    (5,'CHEMISTRY'),
    (6,'CIVIL'),
    (7,'ELECTRICAL'),
    (8,'PRODUCTION'),
    (9,'META'),
    (10,'MECHANICAL'),
)


class StudentForm(forms.Form):
    id= forms.CharField(label='stud-id',max_length=12)
    name=forms.CharField(label='stud-name',max_length=50)
    Programme=forms.ChoiceField(label='stud-prog',choices=CHOICEPROG)
    dept=forms.ChoiceField(label='stud-dept',choices=CHOICEDEPT)
    passwd=forms.PasswordInput()

    



class ProfessorsForm(forms.Form):
    id=forms.CharField(label='prof-id',max_length=30)
    name=forms.CharField(label='prof-name',max_length=30)
    dept=forms.ChoiceField(label='prof-dept',choices=CHOICEDEPTT)
    passwd=forms.PasswordInput()
    

    









  
        

