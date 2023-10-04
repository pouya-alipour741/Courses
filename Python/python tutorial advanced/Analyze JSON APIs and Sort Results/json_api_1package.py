import requests
import json

r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()
print(len(packages_json))      ####include 6506 packages upto now
# package_str = json.dumps(package_json[0],indent=2)
# print(package_str)

package_name = packages_json[0]['name']
package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"


r = requests.get(package_url)
package_json  = r.json()

package_desc = package_json['desc']

package_install30 = package_json["analytics"]["install_on_request"]["30d"][package_name]
package_install90 = package_json["analytics"]["install_on_request"]["90d"][package_name]
package_install365 = package_json["analytics"]["install_on_request"]["365d"][package_name]

# package_str = json.dumps(package_json,indent=2)
# print(package_str)

print(package_name,package_url,package_desc,package_install30,package_install90,package_install365)



