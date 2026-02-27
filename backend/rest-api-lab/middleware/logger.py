from flask import request, jsonify
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_middlewares(app):
    """Register middleware functions with the Flask app"""
    
    @app.before_request
    def log_request_info():
        """Log incoming request information"""
        logger.info(f"[{datetime.now()}] {request.method} {request.path} - {request.remote_addr}")
    
    @app.after_request
    def log_response_info(response):
        """Log response information"""
        logger.info(f"[{datetime.now()}] Response: {response.status_code}")
        return response
    
    @app.errorhandler(404)
    def not_found(error):
        """Custom 404 error handler"""
        return jsonify({"error": "Endpoint not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Custom 500 error handler"""
        return jsonify({"error": "Internal server error"}), 500
