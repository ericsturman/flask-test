from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/clicked/", methods=["POST"])
def hello_world_clicked():
    if request.method == 'POST':
        some_number_doubled = int(request.form["some_number"]) * 2
        some_number_quadrupled = some_number_doubled * 2
        return render_template("result.html", some_number_doubled=some_number_doubled, some_number_quadrupled=some_number_quadrupled)
    

@app.route("/getCSV/", methods=["GET","POST"])
def getPlotCSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()

    data = request.form["data"]
    return Response(
        data,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=mydata.csv"})
