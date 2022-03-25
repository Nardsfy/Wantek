from flask import render_template
from wantek import app

@app.errorhandler(403)
def forbidden_403(e):
	# note that we set the 404 status explicitly
	return render_template('error/403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
	# note that we set the 404 status explicitly
	return render_template('error/404.html'), 404

@app.context_processor
def global_var():
	''' Function buat Global Variable '''
	return dict(namaAplikasi=app.config['NAMA_APLIKASI'])