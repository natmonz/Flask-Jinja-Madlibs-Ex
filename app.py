from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = "MadlibsRFun"
debug = DebugToolbarExtension(app)

@app.route('/')
def main_page():
    return render_template('base.html')

    

@app.route('/select-story')
def story_selection():
    return render_template('select_story.html', stories=stories.values())

@app.route('/form')
def form_page():
    story_id = request.args['story_id']
    story = stories[story_id]
    prompts = story.prompts
    return render_template('form.html', story_id=story_id, title=story.title, prompts=prompts)

@app.route('/story')
def your_story():
    story_id = request.args['story_id']
    story = stories[story_id]
    text = story.generate(request.args)
    return render_template('story.html', title=story.title, text = text)