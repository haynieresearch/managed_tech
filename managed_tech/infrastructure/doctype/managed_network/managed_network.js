//**********************************************************
//* CATEGORY	SOFTWARE
//* GROUP	ERPNEXT/FRAPPE
//* AUTHOR	LANCE HAYNIE
//**********************************************************
//Copyright Haynie IPHC, LLC
//Developed by Haynie Research & Development, LLC
//Developed for Lance Haynie, LLC
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.#
//You may obtain a copy of the License at
//http://www.apache.org/licenses/LICENSE-2.0
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.
frappe.ui.form.on('Managed Network', 'setup', function(frm) {
  cur_frm.set_query("device_name", "static_ip", function(doc, cdt, cdn) {
    return {
      query: "managed_tech.infrastructure.doctype.managed_device.managed_device.get_devices",
        filters: {
          "company": doc.company
  			}
		}
  });
  cur_frm.set_query("network_id", "devices", function(doc, cdt, cdn) {
	  return {
      query: "managed_tech.infrastructure.doctype.network.network.get_network_ids",
        filters: {
          "company": doc.company
        }
    }
  });
});
