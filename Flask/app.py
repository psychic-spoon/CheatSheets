from flask import Flask,render_template,flash,redirect,url_for,session, logging, request
from werkzeug.utils import secure_filename
import os
from flask import jsonify
import json

app=Flask(__name__)    #__name__ is placeholder for current module( app.py)

UPLOAD_FOLDER = './config'

app.secret_key='secret123'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

global data_in
global data_out
global content
global filename

data_in={}
data_out={}

@app.route('/')
def index():
	return render_template('6kmigtool.html')

@app.route('/uploaded',methods=['GET','POST'])
def upload_file():
    global data_in,data_out,content,filename
    supervisor=request.form['supervisor']
    if request.method == 'POST':
        # check if the post request has the file part
        if '6kmig' not in request.files:
            print("1")
            flash('No file in post request')
            return redirect(request.url)
        
        file = request.files['6kmig']
        # if user does not select file, browser also submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            print("No selected file")
            return redirect(request.url)
        
        if file :
            filename=file.filename
            # print("5")
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save("configs/" + filename)
            # print("6")
            # return redirect(url_for('uploaded_file',
                                    # filename=filename))

            ##PROCESSING
            # cmd = "python _6kmigration.py " + filename + " " + supervisor 
            # os.system(cmd)

            data_in = {}
            data_out = {}

            f = open("log/" + filename + ".json","r+")
            tmp_in = json.load(f)
            f.close()

            content=[]
            for i in tmp_in:
                if i.strip().startswith("interface"):
                    line = i.split('\n')[0]
                    name = line.split()[len(line.split())-1]
                    if 'Vlan' not in name:
                        data_in[name] = i
                        content.append({name:i})
            
            # in_val, out_val

            
            #preprocessing
            for i in data_in:
                data_in[i] = data_in[i].replace("\r\n","<br>").replace('\n',"<br>").replace('\r',"<br>").replace(" ","&nbsp")
            
            return render_template('6kmig_output.html',content=content,cont=json.dumps(data_in))                        
    return "ERROR"
 

@app.route('/map',methods=['GET','POST'])
def map():
    global data_in,data_out
    print(data_out)
    if request.method=="POST":
        print(request.form)
        in_val=request.form['input_int']
        out_val=request.form['target_int']

        tmp_log = []
        tmp_lr = []
        f = open("log/" + filename + ".converted.json","r+")
        tmp_out = f.read()
        f.close()
        f = open("log/" + filename + ".json","r+")
        tmp_in = json.load(f)
        f.close()

        # f = open("log/" + file,"r+")
        # tmp_log = f.read()
        # f.close()
        # f = open("log/" + file + ".lines_removed","r+")
        # tmp_lr = f.read()
        # f.close()
        print(tmp_out)
        print(in_val,out_val)
        for i in tmp_out:
            _str_ = ''
            if in_val in i:
                lines = i.split('\n')
                name = lines[0].split()[len(lines[0].split())-1]
                name1 = name.replace("/","_")
                for j in tmp_lr:
                    if name in j or name1 in j:
                        _str_ = _str_ + '\n' + j
                for j in tmp_log:
                    if name in j or name1 in j:
                        _str_ = _str_ + '\n' + j

                _str_ = _str_ + '\n' + "--------------------------------------" + '\n'
                for j in lines:
                    if "service-policy " in j:
                        pol = j.split()[len(j.split())-1]
                        for k in tmp_out:
                            if pol in k:
                                line1 = k.split('\n')
                                for l in line1:
                                    if "class " in l and "class-default" not in l:
                                        cla = line1.split()[len(line1.split())-1]
                                        for m in tmp_out:
                                            if cla in m and "class-map" in m:
                                                _str_ = _str_ + '\n' + m
                                                break
                                _str_ = _str_ + '\n' + k
                                break
                _str_ = _str_ + '\n' + i
                _str_.replace(in_val,out_val)
                data_out[name] = _str_
                print (_str_)
                break

        for i in data_out:
            data_out[i] = data_out[i].replace("\r\n","<br>").replace('\n',"<br>").replace('\r',"<br>").replace(" ","&nbsp")
    
        print(data_out)

    return render_template('6kmig_output.1.html',inp=data_in[in_val],oup=x,content=content)


if __name__=='__main__':
	app.run(debug=True)