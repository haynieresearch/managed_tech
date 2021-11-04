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
from frappe.model.document import Document
import frappe

class ManagedDevice(Document):
	pass

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_devices(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select name, device_name
		from `tabManaged Device`
		where
			parent = {parent}"""
		.format(parent = frappe.db.escape(filters.get("parent"))
		))
