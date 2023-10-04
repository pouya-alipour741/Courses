import requests
import json
import time

t1 = time.perf_counter()
r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()

results = []
for package in packages_json[:50]:
    package_name = package['name']
    package_desc = package['desc']
    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"      ### analytic data does not exist in first json so we have to make this url

    r = requests.get(package_url)
    package_json  = r.json()

    package_install30 = package_json["analytics"]["install_on_request"]["30d"][package_name]
    package_install90 = package_json["analytics"]["install_on_request"]["90d"][package_name]
    package_install365 = package_json["analytics"]["install_on_request"]["365d"][package_name]

    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            '30d': package_install30,
            '90d': package_install90,
            '365d': package_install365,
        }
    }

    results.append(data)

    # time.sleep(r.elapsed.total_seconds())

    print(f'Got {package_name} in {r.elapsed.total_seconds()} seconds')


t2 = time.perf_counter()
print(f"took total of {t2-t1} seconds")
with open('homebrew.json',mode='w') as file:
    json.dump(results,file,indent=2)


