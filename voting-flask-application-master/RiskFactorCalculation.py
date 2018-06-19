def risk_factor_calculate(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13,
                          q13_2, q14, q15, q16, q17, chHPV):
    """

    :param q1:
    :param q2:
    :param q3:
    :param q4:
    :param q5:
    :param q6:
    :param q7:
    :param q8:
    :param q9:
    :param q10:
    :param q11:
    :param q12:
    :param q13:
    :param q14:
    :param q15:
    :param q16:
    :param q17:
    :return:
    """
    risk=0
    ##q1
    if q1=="0":
        risk=risk+1
    elif q1=="5+":
        risk=risk+1.3
    elif q1=="5-":
        risk=risk+2.9
    elif q1=="10+":
        risk=risk+1.95
        ##q2
    if q2=="10+":
        risk=risk+3.12
    elif q2=="5to9":
        risk=risk+3.22
    elif q2=="3to4":
        risk=risk+2.6
    elif q2=="2":
        risk=risk+1.81
    elif q2 == "1":
        risk = risk + 1
    elif q2 == "0":
        risk = risk
    ##q3
    if q3=="16-":
        risk=risk+4.6
    elif q3=="16-17":
        risk=risk+4.24
    elif q3=="18-19":
        risk=risk+2.88
    elif q3=="20-21":
        risk=risk+1.93
    elif q3 == "22+":
        risk = risk + 1
    elif q3 == "-1":
        risk = risk
    ##q4
    if q4=="0":
        risk=risk+1
    elif q4=="1":
        risk=risk+1.35
    elif q4=="2":
        risk=risk+1.17
    elif q4=="3":
        risk=risk+1.25
    elif q4 == "4":
        risk = risk + 2.13
    elif q4 == "5+":
        risk = risk + 2.20
    elif q4 == "-1":
        risk = risk
        ##q5
    if q5=="18-":
        risk=risk+1.56
    elif q5=="18-19":
        risk=risk+1.74
    elif q5=="20-21":
        risk=risk+1.44
    elif q5=="22+":
        risk=risk+1
    elif q5 == "-1":
        risk = risk
    ##q6 cytologia
    if q6 == "0":
        risk = risk + 5.05
    elif q6 == "1-2":
        risk = risk + 1
    elif q6 == "3-4":
        risk = risk + 2
    elif q6 == "5-6":
        risk = risk + 2.68
    elif q6 == "7-9":
        risk = risk + 3.2
    elif q6 == "10+":
        risk = risk + 6.2
    elif q6 =="np":
        risk = risk+1.87
    ##q7
    if q7 == "0":
        risk = risk + 1
    elif q7 == "1-10":
        risk = risk + 1.16
    elif q7 == "11-20":
        risk = risk + 1.4
    elif q7 == "20-30":
        risk = risk + 1.72
    elif q7 == "30+":
        risk = risk + 1.93

    ##q8
    if q8 == "oncelow":
        risk = risk + 1 #fuck logic
    elif q8 == "somepwk":
        risk = risk+0.49
    ##q9 warzywa
    if q9 == "everyday":
        risk = risk + 1
    elif q9 == "less":
        risk = risk + 3.67
    ##q10
    if q10 == "1pwk":
        risk = risk + 1
    elif q10 == "less":
        risk = risk+1.62
    ##q11
    if q11 == "Tak":
        risk = risk + 2.88
    elif q11=="Nie":
        risk = risk+1
    else:
        risk=risk+2; ## Konrad dodal
    ##q12 co tutaj?
    if q12 == "Tak":
        risk = risk + 2.55
    elif q12 == "Nie":
        risk = risk+1
    else:
        risk=risk+2;##Konrad dodal

    ##q13 to waga a q13_2 to wzrost
    bmi= int(q13) / (int(q13_2)/ 100) **2
    if bmi<25:
        #risk=risk+0.55
        risk=risk+3.03
    elif bmi<29:
        #risk=risk+1.05
        risk=risk+3.03
    else:
        risk=risk+3.03

    ##q14
    if q14 == "poniżej 25 lat":
        risk = risk + 0.46
    elif q14 == "25 - 40 lat":
        risk = risk + 0.46
    elif q14 == "40 – 50 lat":
        risk = risk + 0.72
    elif q14 == "powyżej 50 lat":
        risk = risk + 3.35

    ##q15
    if q15 == "wies":
        risk = risk + 3.42
    else:
        risk=risk+0.9

        ##q16 nie ma znaczenia
        ##q17 nie ma znaczenia

        #chora na HPV
    if chHPV == "Nie":
        risk = risk+1
        # else:
        #     if tHPV == "0": #typ 6, 11 lub 42
        #         risk = risk+6.4
        #     elif tHPV=="1": #typ 31 33 35 itd
        #         risk = risk + 21
        #     elif tHPV == "2": #typ 16 18
        #         risk += 33
        #     elif tHPV =="3":
        #         risk = risk+6.4
        #TODO trzeba dodac obliczenia risk faktora
    return risk
