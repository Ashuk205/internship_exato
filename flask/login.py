# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        age = request.form.get("age")
        address = request.form.get("address")
        return "Your name is " + first_name + " " + last_name + "  " + age + "  " + address
    return render_template("form.html")
 
if __name__ == '__main__':
    app.run()
 