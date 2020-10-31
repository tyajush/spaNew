from django.shortcuts import render
import pickle
def home(request):
    return render(request,'index.html')

def result(request):
    age = request.GET['age']
    medu = request.GET['medu']
    fedu = request.GET['fedu']
    travelTime = request.GET['travelTime']
    studyTime = request.GET['studyTime']
    failures = request.GET['failures']
    familyRel = request.GET['familyRel']
    freetime = request.GET['freetime']
    goOut = request.GET['goOut']
    workdayALC = request.GET['workdayALC']
    weekendALC = request.GET['weekendALC']
    health = request.GET['health']
    g1 = request.GET['g1']
    g2 = request.GET['g2']

    gender = request.GET['gender']
    if(gender.lower()=='m'):
        sex_M=1
        sex_F=0
    elif(gender.lower()=='f'):
        sex_F=1
        sex_M=0
    else:
        None

    address = request.GET['address']
    if(address.lower()=='u'):
        address_U=1
        address_R=0
    elif(address.lower()=='r'):
        address_R=1
        address_U=0
    else:
        None

    pstatus = request.GET['pstatus']
    if(pstatus.lower()=='living together'):
        Pstatus_A=0
        Pstatus_T=1
    elif(pstatus.lower()=='apart'):
        Pstatus_A=1
        Pstatus_T=0
    else:
        None

    mjob = request.GET['mjob']
    if(mjob.lower()=='other'):
        Mjob_other=1
        Mjob_sevices=0
        Mjob_at_home=0
        Mjob_teacher=0
        Mjob_health=0
    elif(mjob.lower()=='services'):
        Mjob_other=0
        Mjob_sevices=1
        Mjob_at_home=0
        Mjob_teacher=0
        Mjob_health=0
    elif(mjob.lower()=='at home'):
        Mjob_other=0
        Mjob_sevices=0
        Mjob_at_home=1
        Mjob_teacher=0
        Mjob_health=0
    elif(mjob.lower()=='teacher'):
        Mjob_other=0
        Mjob_sevices=0
        Mjob_at_home=0
        Mjob_teacher=1
        Mjob_health=0
    elif(mjob.lower()=='health'):
        Mjob_other=0
        Mjob_sevices=0
        Mjob_at_home=0
        Mjob_teacher=0
        Mjob_health=1
    else:
        None

    fjob = request.GET['fjob']
    if(fjob.lower()=='other'):
        Fjob_other=1
        Fjob_services=0
        Fjob_at_home=0
        Fjob_teacher=0
        Fjob_health=0
    elif(fjob.lower()=='services'):
        Fjob_other=0
        Fjob_services=1
        Fjob_at_home=0
        Fjob_teacher=0
        Fjob_health=0
    elif(fjob.lower()=='at home'):
        Fjob_other=0
        Fjob_services=0
        Fjob_at_home=1
        Fjob_teacher=0
        Fjob_health=0
    elif(fjob.lower()=='teacher'):
        Fjob_other=0
        Fjob_services=0
        Fjob_at_home=0
        Fjob_teacher=1
        Fjob_health=0
    elif(fjob.lower()=='health'):
        Fjob_other=0
        Fjob_services=0
        Fjob_at_home=0
        Fjob_teacher=0
        Fjob_health=1
    else:
        None

    absent = request.GET['absent']

    reason = request.GET['reason']
    if(reason.lower() =='course'):
        reason_course=1
        reason_home=0
        reason_reputation=0
        reason_other=0
    elif(reason.lower() =='near home'):
        reason_course=0
        reason_home=1
        reason_reputation=0
        reason_other=0
    elif(reason.lower() =='reputation'):
        reason_course=0
        reason_home=0
        reason_reputation=1
        reason_other=0
    elif(reason.lower() =='other'):
        reason_course=0
        reason_home=0
        reason_reputation=0
        reason_other=1
    else:
        None

    guardian = request.GET['guardian']
    if(guardian.lower()=='father'):
        guardian_mother=0
        guardian_father=1
        guardian_other=0
    elif(guardian.lower()=='mother'):
        guardian_mother=1
        guardian_father=0
        guardian_other=0
    elif(guardian.lower()=='other'):
        guardian_mother=0
        guardian_father=0
        guardian_other=1
    else:
        None

    schoolSupport = request.GET['schoolSupport']
    if(schoolSupport.lower()=='yes'):
        schoolsup_no=0
        schoolsup_yes=1
    elif(schoolSupport.lower()=='no'):
        schoolsup_no=1
        schoolsup_yes=0
    else:
        None

    familySupport = request.GET['familySupport']
    if(familySupport.lower()=='yes'):
        famsup_yes=1
        famsup_no=0
    elif(familySupport.lower()=='no'):
        famsup_yes=0
        famsup_no=1
    else:
        None

    paidClass = request.GET['paidClass']
    if(paidClass.lower()=='yes'):
        paid_no=0
        paid_yes=1
    elif(paidClass.lower()=='no'):
        paid_no=1
        paid_yes=0
    else:
        None

    activities = request.GET['activities']
    if(activities.lower()=='yes'):
        activities_yes=1
        activities_no=0
    elif(activities.lower()=='no'):
        activities_yes=0
        activities_no=1
    else:
        None

    nursery = request.GET['nursery']
    if(nursery.lower()=='yes'):
        nursery_yes=1
        nursery_no=0
    elif(nursery.lower()=='no'):
        nursery_yes=0
        nursery_no=1
    else:
        None

    higherEdu = request.GET['higherEdu']
    if(higherEdu.lower()=='yes'):
        higher_yes=1
        higher_no=0
    elif(higherEdu.lower()=='no'):
        higher_yes=0
        higher_no=1
    else:
        None

    internet = request.GET['internet']
    if(internet=='yes'):
        internet_yes=1
        internet_no=0
    elif(internet=='no'):
        internet_yes=0
        internet_no=1
    else:
        None

    romantic = request.GET['romantic']
    if(romantic.lower()=='yes'):
        romantic_no=0
        romantic_yes=1
    elif(romantic.lower()=='no'):
        romantic_no=0
        romantic_yes=1
    else:
        None

    school = request.GET['school']
    if(school.lower()=='gp'):
        school_GP=1
        school_MS=0
    elif(school.lower()=='ms'):
        school_GP=0
        school_MS=1
    else:
        None

    fams = request.GET['fams']
    if(fams=='LE3'):
        fams=1
    elif(fams=='GT3'):
        fams=2
    else:
        None

    #loading the SGD model
    SGD = pickle.load(open('MODEL_SGD', 'rb'))
    X = [[age, medu, fedu, travelTime, studyTime, failures, familyRel, freetime, goOut, workdayALC, weekendALC, health, absent,
        g1, g2,sex_F,sex_M,address_U,address_R,Pstatus_T,Pstatus_A, Mjob_other, Mjob_sevices, Mjob_at_home,
         Mjob_teacher, Mjob_health, Fjob_other, Fjob_services, Fjob_teacher, Fjob_at_home, Fjob_health,
         reason_course, reason_home, reason_reputation, reason_other,guardian_mother,guardian_father,
         guardian_other,schoolsup_no,schoolsup_yes,famsup_yes,famsup_no,paid_no,paid_yes,activities_yes,
         activities_no,nursery_yes,nursery_no,higher_yes,higher_no, internet_yes, internet_no,  romantic_no,
          romantic_yes,  school_GP,school_MS, fams]]
    result = SGD.predict(X)
    if(result>20.0):
        result = 20.0
    if(result<0):
        result = 0

    result = (result/20)*100


    if(result!=100 and result!=0):
        result = round(result[0])

    return render(request,'result.html',{'result':result})
