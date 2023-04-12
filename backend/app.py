from .constants import *
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import logging
from bs4 import BeautifulSoup
import requests

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/amazon_search', methods=['GET'])
@cross_origin()
def amazon_search():
    keyword = request.args.get(KEYWORD)
    url = AMAZON_URL + keyword
    headers = AMAZON_API_HEADER
    response = requests.post(url, headers=headers)
    app.logger.info(f'Response: {response.status_code}')
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    for item in soup.select('.s-result-item'):
        try:
            product = {
                TITLE: item.select_one('.a-size-medium.a-color-base.a-text-normal').text.strip(),
                PRICE: item.select_one('.a-price .a-offscreen').text.strip(),
                RATING: item.select_one('.a-icon-star-small .a-icon-alt').text.strip(),
                URL: item.select_one('.a-link-normal')['href']
            }
            products.append(product)
        except Exception as e:
            app.logger.info(f'Exception: {e}')
            pass
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
