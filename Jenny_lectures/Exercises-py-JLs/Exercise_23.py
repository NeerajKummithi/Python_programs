marks_dict={
    'Neeraj':96,
    'Stuart':97,
    'Thulasidhar':85,
    'Venu Gopal':56,
    'Mythri':76,
    'Gows':82,
    'Mahendra':42,
    'Devendra':32
}

grades_dict={}

for i in marks_dict:
    if marks_dict[i] >= 91 and marks_dict[i]<=100:
        grades_dict[i]='A+'
    if marks_dict[i] >= 81 and marks_dict[i]<=90:
        grades_dict[i]='A'
    if marks_dict[i] >= 71 and marks_dict[i]<=80:
        grades_dict[i]='B'
    if marks_dict[i] >= 61 and marks_dict[i]<=70:
        grades_dict[i]='C'
    if marks_dict[i] >= 51 and marks_dict[i]<=60:
        grades_dict[i]='D'
    if marks_dict[i] >= 41 and marks_dict[i]<=50:
        grades_dict[i]='E'
    if marks_dict[i] <=40:
        grades_dict[i]='F'

print(grades_dict)        