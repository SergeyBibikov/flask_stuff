import os
SECRET_KEY=os.getenv('SK')
SQLALCHEMY_DATABASE_URI="postgresql://postgres:@localhost:5432/postgres"
SQLALCHEMY_TRACK_MODIFICATIONS=False
DEBUG_TB_TEMPLATE_EDITOR_ENABLED=False
DEBUG_TB_INTERCEPT_REDIRECTS=False
