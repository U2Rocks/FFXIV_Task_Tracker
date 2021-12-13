from DutyList import app
from flask.templating import render_template
from flask import render_template, redirect, url_for
from DutyList import db
from DutyList.models2 import ExpansionStatus, Duty


@app.route("/")
@app.route("/home")
def index_page():
    exp_rows_hev = Duty.query.filter_by(duty_expansion="HEV").all()
    exp_rows_sto = Duty.query.filter_by(duty_expansion="STO").all()
    exp_rows_shb = Duty.query.filter_by(duty_expansion="SHB").all()
    exp_rows_end = Duty.query.filter_by(duty_expansion="END").all()
    exp_rows_arr = Duty.query.filter_by(duty_expansion="ARR").all()
    exp_data = ExpansionStatus.query.all()
    return render_template("index.html", 
    exp_data=exp_data,
    exp_rows_arr=exp_rows_arr,
    exp_rows_end=exp_rows_end,
    exp_rows_hev=exp_rows_hev,
    exp_rows_shb=exp_rows_shb,
    exp_rows_sto=exp_rows_sto)

@app.route("/ARR")
def realm_page():
    exp_status_arr = ExpansionStatus.query.filter_by(exp_name="A Realm Reborn").first()
    if exp_status_arr.exp_status == 'active':
        exp_status_arr.exp_status = 'disabled'
        db.session.commit()
    elif exp_status_arr.exp_status == 'disabled':
        exp_status_arr.exp_status = 'active'
        db.session.commit()
    else:
        print('Something went wrong with ARR')
    
    print('realm route activated')
    return redirect(url_for('index_page', _anchor="arr_spot")) 

@app.route("/HEV")
def heavensward_page():
    exp_status_hev = ExpansionStatus.query.filter_by(exp_name="Heavensward").first()
    if exp_status_hev.exp_status == 'active':
        exp_status_hev.exp_status = 'disabled'
        db.session.commit()
    elif exp_status_hev.exp_status == 'disabled':
        exp_status_hev.exp_status = 'active'
        db.session.commit()
    else:
        print('Something went wrong with HEV')
    
    print('heavensward route activated')
    return redirect(url_for('index_page', _anchor="hev_spot")) 

@app.route("/STO")
def stormblood_page():
    exp_status_sto = ExpansionStatus.query.filter_by(exp_name="Stormblood").first()
    if exp_status_sto.exp_status == 'active':
        exp_status_sto.exp_status = 'disabled'
        db.session.commit()
    elif exp_status_sto.exp_status == 'disabled':
        exp_status_sto.exp_status = 'active'
        db.session.commit()
    else:
        print('Something went wrong with STO')
    
    print('stormblood route activated')
    return redirect(url_for('index_page', _anchor="sto_spot")) 

@app.route("/SHB")
def shadowbringers_page():
    exp_status_shb = ExpansionStatus.query.filter_by(exp_name="Shadowbringers").first()
    if exp_status_shb.exp_status == 'active':
        exp_status_shb.exp_status = 'disabled'
        db.session.commit()
    elif exp_status_shb.exp_status == 'disabled':
        exp_status_shb.exp_status = 'active'
        db.session.commit()
    else:
        print('Something went wrong with SHB')
    
    print('shadowbringers route activated')
    return redirect(url_for('index_page', _anchor="shb_spot")) 

@app.route("/END")
def endwalker_page():
    exp_status_end = ExpansionStatus.query.filter_by(exp_name="Endwalker").first()
    if exp_status_end.exp_status == 'active':
        exp_status_end.exp_status = 'disabled'
        db.session.commit()
    elif exp_status_end.exp_status == 'disabled':
        exp_status_end.exp_status = 'active'
        db.session.commit()
    else:
        print('Something went wrong with END')
    
    print('endwalker route activated')
    return redirect(url_for('index_page', _anchor="end_spot")) 

@app.route("/COMP/<int:row_id>")
def complete_page(row_id):
    duty_complete_status = Duty.query.filter_by(id=row_id).first()
    expansion = duty_complete_status.duty_expansion
    expansion_placement = row_id
    page_anchor = ""
    if expansion == "ARR":
        if expansion_placement > 10 and expansion=="ARR":
            page_anchor="arr_spot2"
        else:
            page_anchor="arr_spot"
    elif expansion == "HEV":
        if expansion_placement > 29 and expansion=="HEV":
            page_anchor="hev_spot2"
        else:
            page_anchor="hev_spot"
    elif expansion == "STO":
        if expansion_placement > 43 and expansion=="STO":
            page_anchor="sto_spot2"
        else:
            page_anchor="sto_spot"
    elif expansion == "SHB":
        if expansion_placement > 55 and expansion=="SHB":
            page_anchor="shb_spot2"
        else:
            page_anchor="shb_spot"
    elif expansion == "END":
        page_anchor="end_spot"
    else:
        page_anchor="shb_spot"
    if duty_complete_status.duty_complete == "Incomplete":
        duty_complete_status.duty_complete = "Complete"
        db.session.commit()
    elif duty_complete_status.duty_complete == "Complete":
        duty_complete_status.duty_complete = "Incomplete"
        db.session.commit()
    else:
        print("Something went wrong with COMP")

    
    
    return redirect(url_for('index_page', _anchor=page_anchor)) 