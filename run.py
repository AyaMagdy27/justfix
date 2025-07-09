#!/usr/bin/env python3
"""
Just Fix Application Runner
Simple script to start the Just Fix home service application.
"""

import os
import sys

def main():
    print("=" * 50)
    print("🔧 Starting Just Fix Application")
    print("=" * 50)
    print()

    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found!")
        print("Please make sure you're in the just_fix_app directory.")
        return 1

    # Check if requirements are installed
    try:
        import flask
        print("✅ Flask is installed")
    except ImportError:
        print("❌ Flask not found!")
        print("Please install requirements first:")
        print("   pip install -r requirements.txt")
        return 1

    print("🚀 Starting the application...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print()
    print("-" * 50)

    # Import and run the app
    try:
        from app import app, init_db
        init_db()  # Make sure database is initialized
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(main())
