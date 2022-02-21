# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import cint


def execute(filters=None):

    columns = get_columns()
    data = get_data(filters)

    return columns, data, None, None,  None, {"company": frappe.defaults.get_user_default("Company") }


def get_data(filters):

    # frappe.msgprint("mensaje")
    from_date = filters.from_date

    sql = """ SELECT
        DATE_FORMAT(tss.start_date , '%d/%m/%Y' ) as start_date ,
        DATE_FORMAT(tss.end_date , '%d/%m/%Y' ) as end_date ,
        te.last_name, 
        CONCAT(te.first_name , ' '   , te.middle_name)  as first_name, 
        te.dni ,
        tsd.amount  as 'fortnightly_salary',
        tss.gross_pay - tsd.amount as 'assignment', 
        tss.total_deduction as 'deduction',
        tss.net_pay 'total',
        COALESCE(   tss.number_of_banknotes,'-') as number_of_banknotes, 
        COALESCE(   tss.code_bill_transfer_reference,'-') as code_bill_transfer_reference 
	
    from
        `tabSalary Slip` tss 
        
        join `tabEmployee` te ON te.name  = tss.employee 
        
       join `tabSalary Detail` tsd ON tsd.parent = tss.name and tsd.abbr = 'SQ1'
        where tss.status = 'Submitted'
        AND tss.start_date = '{0}'
    """.format(from_date)

    return frappe.db.sql(sql)


def get_columns():
    return [
        {
            "label": _("Start Date"),
            "fieldname": "start_date",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("End Date"),
            "fieldname": "end_date",
            "fieldtype": "Data",
            "width": 150
        },

        {
            "label": _("Last Name"),
            "fieldname": "last_name",
            "fieldtype": "Data",
            "width": 400
        },

        {
            "label": _("First Name"),
            "fieldname": "first_name",
            "fieldtype": "Data",
            "width": 400
        },

        {
            "label": _("DNI"),
            "fieldname": "dni",
            "fieldtype": "Data",
            "width": 200
        },

        {
            "label": _("Fortnightly Salary"),
            "fieldname": "fortnightly_salary",
            "fieldtype": "Currency",
            "width": 200
        },

           {
            "label": _("Assignment"),
            "fieldname": "assignment",
            "fieldtype": "Currency",
            "width": 200
        },

           {
            "label": _("Deduction"),
            "fieldname": "deduction",
            "fieldtype": "Currency",
            "width": 200
        },

           {
            "label": _("Total"),
            "fieldname": "total",
            "fieldtype": "Currency",
            "width": 200
        },

           {
            "label": _("number_of_banknotes"),
            "fieldname": "number_of_banknotes",
            "fieldtype": "Data",
            "width": 200
        },

           {
            "label": _("code_bill_transfer_reference"),
            "fieldname": "code_bill_transfer_reference",
            "fieldtype": "Data",
            "width": 200
        },


    ]
