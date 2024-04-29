# flask_app.py
from flask import Flask, request, jsonify
from my_streamlit_app import main, main1
from chatbot_app import check, llm_pipeline_using_deepset

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    # You can customize this function to accept parameters
    # from the request and return data accordingly
    main()  # Run your Streamlit app
    # Here, you would collect data from your Streamlit app
    # and return it as JSON
    input_param = request.args.get('input')
    google_places_api_key = request.args.get('key')
    types_param = request.args.get('types')
    print("REcieved params ", input_param)
    data = {'message':  llm_pipeline_using_deepset(input_param, "")}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
