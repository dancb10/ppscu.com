from models.models import Account

from flask import Blueprint, render_template

accounts_page = Blueprint('accounts_page', __name__)
@accounts_page.route('/accounts_page')
def index():
    all_accounts = (Account.get_all_accounts())
    return render_template('accounts_page.html', title='Accounts page',
                           accounts=all_accounts)
