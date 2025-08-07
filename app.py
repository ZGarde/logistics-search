from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
EXCEL_FILE = 'TX-ICO-HOUSTON汇总表.xls'
SHEET_NAME = '汇总表'

@app.route('/', methods=['GET'])
def index():
    keyword = request.args.get('q', '').strip()
    df = pd.read_excel(EXCEL_FILE, sheet_name=SHEET_NAME)

    if keyword:
        df = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)]

    table_html = df.to_html(classes='table table-striped table-bordered', index=False, border=0)
    return render_template('index.html', table=table_html, keyword=keyword)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)