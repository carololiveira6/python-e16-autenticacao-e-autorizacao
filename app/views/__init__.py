from flask import Flask


def init_app(app: Flask):

    from app.views.admin_view import bp as bp_admin
    app.register_blueprint(bp_admin)

    from app.views.api_view import bp as bp_api
    app.register_blueprint(bp_api)