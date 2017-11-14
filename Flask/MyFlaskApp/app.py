from flask import Flask,render_template,flash,redirect,url_for,session, logging, request
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app=Flask(__name__)    #__name__ is placeholder for current module( app.py)

app.secret_key='secret123'

#Config MySQL
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='ashish'
app.config['MYSQL_PASSWORD']='ashish'
app.config['MYSQL_DB']='flaskapp'
app.config['MYSQL_CURSORCLASS']='DictCursor'

#init MySQL
mysql=MySQL(app)


Articles=Articles()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles=Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html',id=id)


class RegisterForm(Form):
	name 		 = StringField('Name',[validators.Length(min=1,max=20)])
	username     = StringField('Username', [validators.Length(min=4, max=25)])
	email        = StringField('Email Address', [validators.Length(min=6, max=35),validators.Required()])
	password     = PasswordField('Password',[validators.DataRequired(),validators.EqualTo('confirm',message='Password don not match')])
	confirm		 = PasswordField('Confirm Password')

@app.route('/register',methods=['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name=form.name.data
		email=form.email.data
		username=form.username.data
		password=sha256_crypt.encrypt(str(form.password.data))

		#Create cursor
		cur=mysql.connection.cursor()

		cur.execute("insert into users(name,email,username,password) values(%s,%s,%s,%s)",(name,email,username,password))		
		
		#Commit to DB
		mysql.connection.commit()

		#Close connection
		cur.close()
		flash("You are now registered and can log in",'success')
		#redirect_url()
		redirect('/index')
	return render_template('register.html',form=form)


if __name__=='__main__':
	app.run(debug=True)
