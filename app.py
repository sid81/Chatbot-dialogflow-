from flask import Flask,request,jsonify
import requests

app=Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
    data=request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency1']['currency']
    amount = data['queryResult']['parameters']['unit-currency1']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    print(source_currency,amount,target_currency) 
    cf = fetch_conversion_factor(target_currency,source_currency,amount)
    print(cf)
    response={
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,cf,target_currency)
    }
    return jsonify(response)
def fetch_conversion_factor(target,source,amount):
    url = "https://api.apilayer.com/currency_data/convert?to={}&from={}&amount={}".format(target,source,amount)
    payload = {}
    headers= {
      "apikey": "JD75eOjV3k58NR94iwzff4Nc0IC9OBiI"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    response=response.json()
    print(response['result'])
    res=response['result']
    return res
    


if __name__=="__main__":
    app.run(debug=True)
