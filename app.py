from flask import Flask, request, render_template
from utility import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form.get("data", "")
        
        word_count = countWords(data)
        paragraph_count = countParas(data)
        char_count = countCharactersOnly(data)
        total_char_count = len(data)
        
        # Pass the values to the template
        return render_template("index.html", 
                               data=data, 
                               count_words=word_count, 
                               count_paras=paragraph_count, 
                               count_chars=char_count,
                               total_char_count=total_char_count)
    
    return render_template("index.html", data="")


if __name__ == "__main__":
    app.run(debug=True)
