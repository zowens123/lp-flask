from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return "This is routing test"

@app.route("/firezach")
def fire():
	return render_template('testindex.html')

@app.route("/demo")
def demo():
    return render_template('lpdemo.html')

@app.route("/demo2")
def demo2():
    return render_template('lppage2.html')

if __name__ == '__main__':
	app.run()
