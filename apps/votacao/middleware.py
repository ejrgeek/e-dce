class SecurityHeaderMiddleware:
    """
    Write by Erlon Jr.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['headers'] = {
            "/**": {
                "Content-Security-Policy": "default-src 'self'; script-src https://code.jquery.com 'sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo' https://cdnjs.cloudflare.com 'sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1' https://stackpath.bootstrapcdn.com 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM'; img-src 'self' https://s3.amazonaws.com; font-src 'self' https://fonts.googleapis.com; style-src 'self' https://fonts.googleapis.com https://stackpath.bootstrapcdn.com 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T'; frame-ancestors 'none';",
                "Referrer-Policy": "no-referrer, strict-origin-when-cross-origin",
                "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
                "X-Content-Type-Options": "nosniff",
                "X-Frame-Options": "DENY",
                "X-XSS-Protection": "1; mode=block"
            }
        }
        return response
