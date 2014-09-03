from wtforms import Form, TextField, BooleanField, validators
#from flask.ext.wtf import Required

class LoginForm(Form):
	openid = TextField('openid', validators = [validators.Required()])
	remember_me = BooleanField('remember_me', default = False)