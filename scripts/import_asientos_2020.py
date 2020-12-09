#!/usr/bin/env python3
import os
from os import scandir
from os.path import abspath
from os.path import join
import base64
from odoo.exceptions import UserError

from datetime import datetime, date
import pandas
from time import time

session.open(db='JIM_SPORTS')
script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))


excel_file = 'Libro Diario 1º y 2º T 2020.xlsx' 
company_id = 35


lines = []
df = pandas.read_excel(script_path+"/"+excel_file)
asiento_prev = 0
journal_id = 187
for row in df.index:
    asiento = df["Asnto."][row]
    cuenta = int(df["Subcuenta"][row])
        
    print (cuenta)
    account = session.env['account.account'].search([('code', '=', cuenta), ('company_id', '=', company_id )])
    j_id = session.env['account.journal'].search([('default_debit_account_id', '=', account.id)])
    if j_id:
        journal_id = j_id
    
    print(account.name)
    debe = df["Importe Debe"][row]
    haber = df["Importe Haber"][row]
    if pandas.isnull(debe):
        debe =0 
    if pandas.isnull(haber):
        haber =0 
    entidad = df["Entidad"][row]
    nombre = df["Descripción"][row]
    
    fecha = df ["Fecha"][row]
    

    partner = False
        
    if asiento != asiento_prev :
        print("Generando nuevo asiento")
        
        move_id = session.env['account.move'].create(
            {
                'journal_id': journal_move_id.id,
                'date': fecha_move,
                #'company_id', company_id
                'line_ids': lines,
                'ref':ref_move,
            }
        )
        print ("Creado movimiento")
        lines =[]
        asiento_prev = asiento
        if journal_id == journal_move_id:
            journal_id = 187
    
    fecha_date = datetime.strptime(fecha, '%d/%m/%Y')
    date_str = date.strftime(fecha_date, '%Y-%m-%d')
    fecha_move = fecha
    ref_move = ref
    journal_move_id = journal_id
    lines.append(
    (0, 0, {
            'debit': debe,
            'credit': haber,
            'account_id': account.id,
            'partner_id': partner and partner[0].id or False,
            'name': nombre
        })
    )
    
    
    processed += 1
    print("Lineas ejecutadas: %d" % (processed) )
    

move_id = session.env['account.move'].create(
    {
        'journal_id': journal_move_id.id,
        'date': fecha_move,
        #'company_id', company_id
        'line_ids': lines,
        'ref':ref_move,
    }
)

session.cr.commit()
exit()