frappe.query_reports["Employee Payroll"] = {
	"filters": [
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.add_days( frappe.datetime.month_start() , new Date().getDate() <= 15 ?   -15: 0),
			reqd: 1
		}
	]
}