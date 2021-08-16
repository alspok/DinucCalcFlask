"""Routes and views for the flask application."""

from flask import Flask, request, render_template, redirect

from datetime import datetime
from flask import render_template, request
from DinucCalcFlask import app
from DinucCalcFlask.DinucFrqTable import DinucFrqTable
from DinucCalcFlask.DinucCalculation import DinucCalculation
from DinucCalcFlask.RandomSeq import RandomSeq
from DinucCalcFlask.GCCalculation import GCCalculation
from DinucCalcFlask.DinucData import DinucData
from DinucCalcFlask.SeqList import SeqList
from DinucCalcFlask.GBEntrez import GBEntrez

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/seqinput')
def seqinput():
    """Console input seq dinuc calculation."""
    dinucFrqTable = DinucCalculation('no seq')
    return render_template(
        'seqinput.html',
        diTableLength = len(dinucFrqTable.dinuc_table),
        dinucFrqTable = dinucFrqTable.dinuc_table
    )

@app.route('/seqfrqtable', methods=['post'])
def seqtextarea():
    seq = request.form['seq']
    gcCalculation = GCCalculation(seq)
    dinucFrqTables = DinucCalculation(seq)
    dinucTableLength = len(dinucFrqTables.dinuc_table)
    if len(seq) <= 2000:
        printSeq = seq
    else:
        printSeq = seq[:60] + '....' + seq[len(seq)-60:]
    return render_template(
        'seqfrqtable.html',
        printSeq = printSeq,
        gcCalculation = round(gcCalculation.gcCount, 2),
        seqLength = len(seq),
        dinucTableLength = dinucTableLength,
        dinucFrqTables = dinucFrqTables.dinuc_table,
        dinucFrqDiffSum = round(dinucFrqTables.dinuc_frq_diff_sum, 4),
        showTable = True
        )

@app.route('/seqrandom')
def seqrandom():
    """Random seq dinuc calculation."""
    return render_template('seqrandom.html')

@app.route('/makerandom', methods=['post'])
def seqrandommake():
    seqLength = int(request.form.get('seqlength'))
    gcPercentage = int(request.form.get('gcpercentage'))
    if seqLength <= 2000 and (gcPercentage >= 1 and gcPercentage < 100):
        randomSeq = RandomSeq(seqLength, gcPercentage)
        randSeq = randomSeq.randSeq()
        gcCalculation = GCCalculation(randSeq)
        dinucFrqTables = DinucCalculation(randSeq)
        if len(randSeq) <= 1000:
            printSeq = randSeq
        else:
            printSeq = randSeq[:60] + '....' + randSeq[len(randSeq)-60:]
        return render_template(
            'seqrandfrqtable.html',
            printSeq = printSeq,
            seqLength = seqLength,
            dinucTableLength = len(dinucFrqTables.dinuc_table),
            dinucFrqTables = dinucFrqTables.dinuc_table,
            dinucFrqDiffSum = round(dinucFrqTables.dinuc_frq_diff_sum, 4),
            showTable = True,
            gcCalculation = round(gcCalculation.gcCount, 2),
            randSeq = randSeq)
    else:
        return render_template(
            'seqrandom.html',
            inputError = False)

#
@app.route('/seqinputlist')
def seqinputlist():
    """Dinuc calculation of seq from list"""
    seqList = SeqList()
    return render_template(
        'seqinputlist.html',
        seq1 = seqList.seq1,
        seq2 = seqList.seq2,
        seq3 = seqList.seq3,
        seq4 = seqList.seq4,
        seq5 = seqList.seq5,
        seq6 = seqList.seq6,
        seq7 = seqList.seq7)

@app.route('/seqlistcalc', methods=['post'])
def seqlistcalc():
    """ """
    listSeq = request.form.get('seq')
    gcCalculation = GCCalculation(listSeq)
    dinucFrqTables = DinucCalculation(listSeq)
    return render_template(
        'seqlistfrqtable.html',
        dinucTableLength = len(dinucFrqTables.dinuc_table),
        dinucFrqTables = dinucFrqTables.dinuc_table,
        dinucFrqDiffSum = round(dinucFrqTables.dinuc_frq_diff_sum, 4),
        gcCalculation = round(gcCalculation.gcCount, 2),
        seqLength = len(listSeq),
        listSeq = listSeq)

@app.route('/seqinputgb')
def seqinputgb():
    """Template to input """
    return render_template('seqinputgb.html')

@app.route('/seqgbsearch', methods = ['post'])
def seqgbsearch():
    gbsearchkey = request.form['gbsearch']
    gbentrez = GBEntrez(gbsearchkey)
    gbrecord = gbentrez.gbSearchResult()
    #gbresult = "<br />".join(gbresult.split("\n"))
    nucs = 100
    gbrecord_seq = [str(gbrecord.seq[i:i+nucs].lower()) for i in range(0, len(str(gbrecord.seq)), nucs)]
    
    dinucData = DinucData(gbrecord.seq)
    #dinucData.dinucTableComplete()
    dinucFrqTables = dinucData.dinuc_table
    dinucFrqDiffSum = dinucData.dinuc_frq_diff_sum

    return render_template('gbentrez.html',
        gbrecord_id = gbrecord.id,
        gbrecord_description = gbrecord.description,
        gbrecord_seq = gbrecord_seq,
        dinucTableLength = len(dinucData.dinuc_table),
        dinucFrqTables = dinucFrqTables,
        dinucFrqDiffSum = dinucFrqDiffSum)
