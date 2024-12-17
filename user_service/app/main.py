from flask import Flask
from core.database import Base, engine
from api.v1.routes.auth import user_router

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

app.register_blueprint(user_router, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(debug=True, port=8001)