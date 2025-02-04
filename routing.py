from libraries.libraries import *

from views.login.views import login_main

app = Flask(__name__)
app.debug = True
app.secret_key = "lUn0Pr0dUcT10n@pplic@t10n"

app.register_blueprint(login_main, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)