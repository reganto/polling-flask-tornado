import random

from flask import Flask, url_for


app = Flask(__name__)


@app.route("/polling/api/v1.0/rndimg")
def api():
    numbers = [str(number) for number in range(1, 52)]
    leading_zero_numbers = []
    for number in numbers:
        leading_zero_numbers.append(number.zfill(len(number)+1))

    random_number = random.choice(leading_zero_numbers)
    image = f"img/{random_number}.png"    
    return {
        "status": "success", 
        "message": url_for(
                       "static", 
                       filename=image,
                       _external=True
        )}

