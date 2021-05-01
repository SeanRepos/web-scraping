from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

URL = "https://www.trianglemtb.com/mobiletrailstatus.php"


def main():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    trs = soup.find_all("tr")
    data_rows = trs[1:-2]
    texts = [
        tuple(data_row.find_all(text=True)[:-1]) for data_row in data_rows
    ]
    texts = [text for text in texts if text]
    data = [(str(entry[0]).strip(), str(entry[1]).strip()) for entry in texts]

    for trail, status in data:
        print(f"\"{trail}\" - \"{status}\"")

    return data


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', methods=['GET'])
def api():
    trail_status = main()
    trail_status = [{
        'trail_name': trail_name,
        'status': status
    } for trail_name, status in trail_status]

    return jsonify(trail_status)


if __name__ == "__main__":
    main()
    app.run(threaded=True, port=5000)