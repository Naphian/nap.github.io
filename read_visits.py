from app import db, Visit, app  # Import `app` as well

with app.app_context():  # Create an application context
    visits = db.session.query(Visit.page_name, db.func.count(Visit.id)).group_by(Visit.page_name).all()
    
    for page_name, count in visits:
        print(f"{page_name}: {count}")
