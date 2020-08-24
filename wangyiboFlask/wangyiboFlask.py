from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import time 
from changeImg import changeImgStyle, img_resize

from datetime import timedelta
import numpy as np
import json
from poetmaster.write_poem import WritePoem,start_model
import tensorflow.compat.v1 as tf
from IPython import embed


app = Flask(__name__, template_folder = '.')


@app.route('/')
def index():
    return render_template('templates/index.html')

#设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 设置静态文件缓存过期时间
#app.send_file_max_age_default = timedelta(seconds = 30)


# @app.route('/upload', methods=['POST', 'GET'])
@app.route('/getAndChangeImg/', methods=['POST', 'GET'])  # 添加路由
def getAndChangeImg():
    if request.method == 'POST':
        f = request.files['img']

        if not (f and allowed_file(f.filename)):
            return render_template('templates/index.html')

        imgStyle = request.form.get("picStyle")
        imgStyle = 'models/' + imgStyle + '.t7'

        user_input = request.form.get("imgName")

        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        upload_path = os.path.join('static/tmpImg', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        # upload_path = os.path.join(basepath, 'static/images','test.jpg')  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)

        img_resize(upload_path)

        upload_path = upload_path.replace('\\', '/')
        # 使用Opencv转换一下图片格式和名称

        finalName = user_input + '.jpg'
        finalName = os.path.join('static', 'tmpImg', finalName)

        changeImgStyle(imgStyle, upload_path, finalName)
        finalName = os.path.join("..", finalName)
        upload_path = os.path.join("..", upload_path)

        return render_template('templates/changeImage.html', originalUrl = upload_path, changeUrl = finalName)

    return render_template('templates/index.html')

@app.route('/tryFlask/')
def tryFlask():
    a = {'testWord': "it is a test"}
    return json.dumps(a)

@app.route('/apple/')
def apple():
    return render_template('templates/test.html')


#style_help = '<br> para style : 1:自由诗<br> 2:带押韵的自由诗<br> 3:藏头诗<br>4:给定若干字，以最大概率生成诗'

@app.route('/poem')
def write_poem():
    writer = start_model()
    params = request.args
    start_with= ''
    poem_style = 0

    # print(params)
    if 'start' in params :
        start_with = params['start']
    if 'style' in  params:
        poem_style = int(params['style'])

    #embed()
    # return 'hello'
    if  start_with:
         if poem_style == 3:
            # returcdn  writer.cangtou(start_with)
            res = {}
            res['status_code']  = 200
            res['data'] = writer.cangtou(start_with)
            return json.dumps(res, default=lambda obj: obj.__dict__, sort_keys=True, ensure_ascii=False,indent=4), 200
         elif poem_style == 4:
            return writer.hide_words(start_with)

    if poem_style == 1:
        return  writer.free_verse()
    elif poem_style == 2:
        return writer.rhyme_verse()

    return 'hello,what do you want? {}'.format(sytle_help)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug=False)
