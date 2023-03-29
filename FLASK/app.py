from flask import Flask,render_template,jsonify,request

app = Flask(__name__)



@app.route('/',methods = ['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route("/math",methods = ['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        if (ops == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + str(num2) + 'is ' + str(r)
        return render_template('results.html',result = result)
        
        if (ops == 'subtract'):
            r = num1 - num2
            result = 'the minues of ' + str(num1) + str(num2) + 'is ' + str(r)
        return render_template('results.html',result = result)
        
        if (ops == 'multiply'):
            r = num1 * num2
            result = 'the multiply of ' + str(num1) + str(num2) + 'is ' + str(r)
        return render_template('results.html',result = result)
    
            
            
        

if __name__=="__main__":
    app.run(host="0.0.0.0")