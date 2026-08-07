from flask import Blueprint, render_template, request, flash

logic_bp = Blueprint('logic_shop', __name__, template_folder='../templates/logic_shop', url_prefix='/logic_shop')

@logic_bp.route('/', methods=['GET', 'POST'])
def index():
    balance = 100
    message = None
    flag = None
    
    if request.method == 'POST':
        item = request.form.get('item', 'flag')
        try:
            quantity = int(request.form.get('quantity', '1'))
            unit_price = 1000  # Flag costs $1000
            
            total_cost = unit_price * quantity
            
            # Logic Flaw: Allowing negative quantity or price tampering
            if quantity < 0:
                # User gains money by buying negative items!
                balance = balance - total_cost
                message = f"Logic Flaw Triggered! Refund credited. New Balance: ${balance}"
                if balance >= 1000:
                    flag = "CTF{l0g1c_fl4w_pr1c3_m4n1pul4710n_2026}"
            elif total_cost <= balance:
                balance -= total_cost
                flag = "CTF{l0g1c_fl4w_pr1c3_m4n1pul4710n_2026}"
                message = "Purchase successful! Here is your Flag item."
            else:
                message = f"Insufficient Funds! Total cost is ${total_cost}, but your balance is only ${balance}."
        except ValueError:
            message = "Invalid quantity value!"
            
    return render_template('logic_shop/index.html', balance=balance, message=message, flag=flag)
