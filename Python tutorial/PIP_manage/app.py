import requests

#
# python3 -m pipenv shell - uruchomienie srodowiska
# pipenv --venv
# pipenv install
# pipenv install <ad>
# pipenv uninstall <ad>
# pipenv update --outdated


response = requests.get("http://google.com")
print(response)