from flask import Flask, render_template, request, redirect, jsonify
from models import db, URL
import validators

app = Flask(__name__)
app.config.from_object("config.Config")
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('url')
        custom_alias = request.form.get('custom_alias')

        if not validators.url(original_url):
            return "Invalid URL", 400
            
        if custom_alias:
            existing_url = URL.query.filter_by(short_id=custom_alias).first()
            if existing_url:
                return "This alias is already taken. Try another.", 400
            short_id = custom_alias  # Use the user-provided alias
        else:
            short_id = URL.generate_unique_short_id() 

        new_url = URL(original_url=original_url)
        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + new_url.short_id
        return render_template("index.html", short_url=short_url)

    return render_template("index.html")

@app.route('/<short_id>')
def redirect_url(short_id):
    url_entry = URL.query.filter_by(short_id=short_id).first()
    if url_entry:
        url_entry.visit_count += 1
        db.session.commit()
        return redirect(url_entry.original_url)
    return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)

