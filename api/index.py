from app import app

# This is the serverless function entry point for Vercel
def handler(request):
    return app(request.environ, lambda *args: None)
