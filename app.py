"""Flask app for adopt app"""

from flask import Flask, request, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'extremelysecret'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

############################################################################

@app.route('/')
def home_page():
    """ Show home page listing all pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets) 


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add a pet"""

    form = AddPetForm()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}

        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added new pet: {pet.name}")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Render form to edit pet and handle form submission"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():    
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"Updated details for {pet.name}")
        return redirect('/')
    else:
        return render_template('show_details.html', form=form, pet=pet)

        

