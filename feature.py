from flask import Flask, render_template

FAI = Flask(__name__)


@FAI.route('/send_data')
def send_data():
    return render_template('send_data.html', name='Likith')





if __name__=='__main__':
    FAI.run(debug=True)