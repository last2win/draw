# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
from datetime import timedelta
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(
    seconds=60)  # 设置图片的缓存时间为1分钟


def get_data():
    data=[]
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        for i in lines:
            i=i.split(',')
            if int(i[0])>=5500:
                break
            data.append((int(i[0]),int(i[1])))
    return data




@app.route('/', methods=['GET'])
def main():
    data = get_data()
    return render_template('index.html', data=data)



if __name__ == '__main__':
    data=[]
    with open('data.csv', 'r') as f:
        lines = f.readlines()
        for i in lines:
            i=i.split(',')
            data.append((int(i[0]),int(i[1])))
    app.run(host='0.0.0.0', port=4000, debug=True)
