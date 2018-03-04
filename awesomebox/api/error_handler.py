"""Handle errors."""
import flask
import awesomebox


class InvalidUsage(Exception):
    """Handle errors."""

    def __init__(self, message, status_code=None, payload=None):
        """Construct for error class."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Convert the error to dictionary for printing."""
        error_message = dict(self.payload or ())
        error_message['message'] = self.message
        error_message['status_code'] = self.status_code
        return error_message


@awesomebox.app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """Handle errors."""
    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
