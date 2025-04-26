from app import app
from models import db, Incident

with app.app_context():
    db.drop_all()
    db.create_all()

    # Sample incidents
    incident1 = Incident(title="AI model hallucination", description="Generated harmful misinformation", severity="High")
    incident2 = Incident(title="Bias in hiring algorithm", description="Discriminated against certain groups", severity="Medium")

    db.session.add(incident1)
    db.session.add(incident2)
    db.session.commit()
