"""
Blueprints in Flask are a way to organize an application into smaller, modular parts.
They allow developers to define application components (e.g., routes, templates, static files)
in separate modules, which can then be registered with the main application. Blueprints
make large Flask applications more manageable by promoting a modular structure,
improving readability, and making it easier to reuse code across different parts of the
application.

Using Blueprints, developers can create modules for specific features or areas of the
application, such as user authentication or an admin panel, and integrate them into the main
app.
"""

from flask import Flask, Blueprint

app = Flask(__name)

# Create a blueprint for the admin section of the app
admin_bp = Blueprint('admin', __name__)

# Register routes for the admin section
@admin_bp.route('/dashboard')
def admin_dashboard():
    return 'Admin Dashboard'

@admin_bp.route('/settings')
def admin_settings():
    return 'Admin Settings'

# Register the blueprint with the main app
app.register_blueprint(admin_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)