# 完整版网页银行 APP（登录 + 余额 + 转账）
from flask import Flask, request, render_template_string

app = Flask(__name__)

# 账户数据（和你原来项目一致）
users = {
    "Alice": "1234",
    "Bob": "5678",
    "Tom": "9012"
}

balances = {
    "Alice": 10000,
    "Bob": 10000,
    "Tom": 10000
}

# 登录页
@app.route('/')
def index():
    return render_template_string('''
    <h1>🏦 简易银行系统（网页版 APP）</h1>
    <form action="/login" method="POST">
        用户名：<input name="username"><br><br>
        密码：<input type="password" name="password"><br><br>
        <button>登录</button>
    </form>
    ''')

# 登录后功能页
@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pwd = request.form['password']

    if user in users and users[user] == pwd:
        return render_template_string('''
            <h2>欢迎，{{user}}！</h2>
            <h3>💰 当前余额：{{bal}} 元</h3>
            <hr>
            <h3>💸 我要转账</h3>
            <form action="/transfer" method="POST">
                <input type="hidden" name="from_user" value="{{user}}">
                转给：<input name="to_user"><br><br>
                金额：<input name="amount"><br><br>
                <button>确认转账</button>
            </form>
            <br>
            <a href="/">退出登录</a>
        ''', user=user, bal=balances[user])
    else:
        return "<h3>登录失败</h3><a href='/'>返回</a>"

# 转账功能
@app.route('/transfer', methods=['POST'])
def transfer():
    from_user = request.form['from_user']
    to_user = request.form['to_user']
    amount = int(request.form['amount'])

    if to_user not in balances:
        return "<h3>对方账户不存在</h3><a href='/'>返回</a>"

    if balances[from_user] >= amount:
        balances[from_user] -= amount
        balances[to_user] += amount
        return f'''
            <h2>✅ 转账成功！</h2>
            <h3>你转给 {to_user} {amount} 元</h3>
            <a href="/">返回登录</a>
        '''
    else:
        return "<h3>❌ 余额不足</h3><a href='/'>返回</a>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)