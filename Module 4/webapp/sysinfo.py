import router
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def sysinfo():
    r1 = router.Router('198.51.100.1', 'icanhasnetworkaccess')
    hostname = r1.get_hostname()
    contact = r1.get_contact()
    location = r1.get_location()
    return render_template('router.html', hostname=hostname, contact=contact,
                            location=location)

@app.route("/update", methods=['POST'])
def update():
    r1 = router.Router('198.51.100.1', 'supersecretpasswordyoullneverguess')
    new_hostname = request.form['hostname']
    print new_hostname
    r1.set_hostname(new_hostname)
    return redirect(url_for('sysinfo'))

if __name__ == '__main__':
    app.run(debug=True)
