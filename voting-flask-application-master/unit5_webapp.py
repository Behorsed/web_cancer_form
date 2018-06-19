from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics
from RiskFactorCalculation import risk_factor_calculate
import matplotlib.pyplot as plt
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'

    """
    #To co było w wersji demo, tak wiem, że się nie używa
    do tego tego typu komentarzy
        id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    firstname = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer)
    income = db.Column(db.Integer)
    satisfaction = db.Column(db.Integer)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    """

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    question1 = db.Column(db.String)
    question2 = db.Column(db.String)
    question3 = db.Column(db.String)
    question4 = db.Column(db.String)
    question5 = db.Column(db.String)
    question6 = db.Column(db.String)
    question7 = db.Column(db.String)
    question8 = db.Column(db.String)
    question9 = db.Column(db.String)
    question10 = db.Column(db.String)
    question11 = db.Column(db.String)
    question12 = db.Column(db.String)
    question13 = db.Column(db.Float) #bo waga w kg
    question13_2 = db.Column(db.Integer) #bo wzrost w cm
    question14 = db.Column(db.String)
    question15 = db.Column(db.String)
    question16 = db.Column(db.String)
    question17 = db.Column(db.String)
    chorzyHPV = db.Column(db.String)
    risk = db.Column(db.Float)

    def __init__(self, question1, question2, question3, question4, question5,
                          question6, question7, question8, question9, question10,
                          question11, question12, question13, question13_2,question14,
                          question15, question16, question17, chorzyHPV, risk):
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5
        self.question6 = question6
        self.question7 = question7
        self.question8 = question8
        self.question9 = question9
        self.question10 = question10
        self.question11 = question11
        self.question12 = question12
        self.question13 = question13
        self.question13_2 = question13_2
        self.question14 = question14
        self.question15 = question15
        self.question16 = question16
        self.question17 = question17
        self.chorzyHPV = chorzyHPV
        self.risk = risk


db.create_all()


@app.route("/", )
def welcome():
    return render_template('index.html')

@app.route("/form",methods=['GET','POST','DELETE'])
def show_form():
    return render_template('form.html')

@app.route("/raw",methods=['GET','POST','DELETE'])
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/result")
def show_result():
    # x = [2, 4, 6]
    # y = [1, 3, 5]
    # plt.plot(x, y)
    # plt.show()

    lows = []  # niskie ryzyko
    mediums = []  # srednie ryzyko
    highs = []  # wysokie ryzyko
    fd_list = db.session.query(Formdata).all()

    data1 = []
    for val in fd_list:
        risk = val.risk
        data1.append([(val.id), risk])
        if val.id<27:
            lows.append(1)
        elif val.id <35:
            mediums.append(1)
        else:
            highs.append(1)

    currentAnkieta=fd_list[-1]
    riskAnkietyCurrent=currentAnkieta.risk
    if riskAnkietyCurrent<27:
        variable1='niskiego'
    elif riskAnkietyCurrent<35:
        variable1='średniego'
    else:
        variable1='wysokiego'

    # Sortowanie tablicy po risk faktorze (czyli po kolumnie o indeksie 1)
    #data1 = sorted(data1, key=lambda x: x[1])


    # lows = []  # niskie ryzyko
    # mediums = []  # srednie ryzyko
    # highs = []  # wysokie ryzyko
    wektor = []

    #wartosci risk  factorow
    # medium_risk = 27
    # high_risk = 35

    # for el in fd_list:
    #     wektor = el.risk
    #     if wektor < 27:
    #         lows.append(1)
    #     elif wektor <35:
    #         mediums.append(1)
    #     else:
    #         highs.append(1)

    high = len(highs)
    medium = len(mediums)
    low = len(lows)

    data2 = [
        ['Niskie', low],
        ['Średnie', medium],
        ['Wysokie', high]]


    data = [data1, data2]

    return render_template('result.html', data=data,variable=variable1,variable2=riskAnkietyCurrent)


@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    question1=request.form['antykoncepcja']
    question2=request.form['partnerzy']
    if question2 is None:
        question3 = "-1"
        question4 = "-1"
    else:
        question3 = request.form['sexWiek']
        question4 = request.form['ciaza']
    if question4=="-1":
        question5 = "-1"
    else:
        question5 = request.form['ciazaWiek']

    #question3=request.form['sexWiek']
    #question4=request.form['ciaza']
    #question5=request.form['ciazaWiek']
    question6 = request.form['cytologia']
    question7 = request.form['palenie']
    question8 = request.form['alkohol']
    question9 = request.form['warzywa']
    question10 = request.form['wf']
    question11 = request.form['chorzySM']
    question12 = request.form['chorzyIN']
    chorzyHPV = request.form['chorzyHPV']

    # if chorzyHPV == "Tak":
    #     typHPV = request.form["HPV"]
    # else:
    #     typHPV = "-1"

    question13 = request.form['waga']
    question13_2 = request.form['wzrost']
    question14 = request.form['wiek']
    question15 = request.form['miasto']
    question16 = request.form['praca']
    question17 = request.form['wyksztalcenie']

    #pytania warunkowe
    #if question2 == "0":
    #    question3 = "0"
    #    question4 = "0" #brak dzieci
    #    question5 = "0"
    #elif question4 == "0":
    #    question5 = "0"




    #funkcja obliczajaca risk factor. zwraca risk factor
    risk = risk_factor_calculate(question1, question2, question3, question4, question5,
                          question6, question7, question8, question9, question10,
                          question11, question12, question13, question13_2,question14,
                          question15, question16, question17, chorzyHPV)
    # Save the data
    fd = Formdata(question1, question2, question3, question4, question5,
                          question6, question7, question8, question9, question10,
                          question11, question12, question13, question13_2,question14,
                          question15, question16, question17, chorzyHPV, risk)
    db.session.add(fd)
    db.session.commit()


    return redirect(url_for('show_result', form_id=fd.id))



if __name__ == "__main__":
    app.debug = True
    app.run()
