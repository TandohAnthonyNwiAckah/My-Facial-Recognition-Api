
import json
import time
import image_verify
from flask import Flask, request
from werkzeug.utils import secure_filename

api = Flask(__name__)
 
@api.route('/api/v1/image_verify', methods=['POST'])
def verify_image():

    target = request.files['target']

    src =  request.files.getlist("src")

    target_filename=secure_filename(target.filename)
    
    response=[]

    for srcs in src:

        start = time.time()
        
        end=time.time()

        result = image_verify.onCreate(target,srcs)

        json_contect={
                'result':str(result),
                'time_taken':round(end-start,3),
                'target':target_filename,
                'src':secure_filename(srcs.filename)
            }

        response.append(json_contect)

    json_response = json.dumps(response)

    return api.response_class(json_response, content_type='application/json') 


if __name__ == "__main__":
    api.run(debug=True)
    # api.run(debug=True,host="0.0.0.0",port=8050)