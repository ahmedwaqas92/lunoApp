import sys
sys.path.append('../../')
from libraries.libraries import *

login_main = Blueprint('login_main', __name__, static_folder='static', template_folder='templates')

@login_main.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for('login_main.login'))

@login_main.route('/login', methods=['GET', 'POST'])
def login():    
    return render_template('login.html')