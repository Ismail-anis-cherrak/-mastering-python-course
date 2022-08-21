'''
====================================
-- 136 - Flask – Jinja Template 
-- link : https://www.youtube.com/watch?v=VdANhdo9pTo&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ------------------------------------
# -- Flask =&gt; Jinja Template Engine --
# ------------------------------------

from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage.html", title="Homepage")

@skills_app.route("/about")
def about():
  return render_template("about.html", title="About Us")

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)