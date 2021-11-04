#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	ERPNEXT/FRAPPE
#* AUTHOR	LANCE HAYNIE
#**********************************************************
#Copyright Haynie IPHC, LLC
#Developed by Haynie Research & Development, LLC
#Developed for Lance Haynie, LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.#
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
from . import __version__ as app_version

app_name = "managed_tech"
app_title = "Managed Technology"
app_publisher = "Haynie Research & Development, LLC"
app_description = "Managed Technology System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@haynieresearch.us"
app_license = "Apache 2.0"

fixtures = [
    {"doctype":"Custom Field", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Property Setter", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Opportunity", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Customer", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Expense Claim", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Purchase Order", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Purchase Receipt", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Purchase Invoice", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Sales Order", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Sales Invoice", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Delivery Note", "filters": [["_user_tags", "like", ("%managed_tech%")]]},
    {"doctype":"Role", "filters": [["_user_tags", "like", ("%managed_tech%")]]}
]

calendars = ["Production", "Production Music Project"]

domains = {
	'Managed Technology': 'managed_tech.domains.managed_tech'
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/managed_tech/css/managed_tech.css"
# app_include_js = "/assets/managed_tech/js/managed_tech.js"

# include js, css files in header of web template
# web_include_css = "/assets/managed_tech/css/managed_tech.css"
# web_include_js = "/assets/managed_tech/js/managed_tech.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "managed_tech/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "managed_tech.utils.jinja_methods",
# 	"filters": "managed_tech.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "managed_tech.install.before_install"
# after_install = "managed_tech.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "managed_tech.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"managed_tech.tasks.all"
# 	],
# 	"daily": [
# 		"managed_tech.tasks.daily"
# 	],
# 	"hourly": [
# 		"managed_tech.tasks.hourly"
# 	],
# 	"weekly": [
# 		"managed_tech.tasks.weekly"
# 	],
# 	"monthly": [
# 		"managed_tech.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "managed_tech.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "managed_tech.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "managed_tech.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"managed_tech.auth.validate"
# ]
