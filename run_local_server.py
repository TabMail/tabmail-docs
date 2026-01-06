import http.server
import os
import socketserver

# Config (env override friendly)
DEFAULT_PORT = 8001
PORT = int(os.environ.get("PORT", DEFAULT_PORT))
DIRECTORY = "web"

class ReusableTCPServer(socketserver.TCPServer):
    # Avoid "Address already in use" during quick restarts (TIME_WAIT, etc.)
    allow_reuse_address = True


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Cloudflare Pages-style convention:
        # - directory pages are canonical with trailing slash (e.g. /faq/)
        # - "clean" URLs can map to .html when a file exists (for parity with tabmail-site)
        #
        # This keeps local testing behavior close to production.

        # If the path is a directory request, let the default handler serve index.html.
        if self.path.endswith("/"):
            return super().do_GET()

        local_path = self.translate_path(self.path)

        # If shared scripts request /assets/*, redirect to canonical tabmail.ai assets.
        # This keeps docs independent of shipping asset copies.
        if self.path.startswith("/assets/"):
            target = "https://tabmail.ai" + self.path
            print(f"[DocsLocalServer] Redirecting assets request: {self.path} -> {target}")
            self.send_response(302)
            self.send_header("Location", target)
            self.end_headers()
            return

        # If this maps to a directory on disk, redirect to trailing slash.
        # Example: /faq -> /faq/
        if os.path.isdir(local_path):
            self.send_response(301)
            self.send_header("Location", self.path + "/")
            self.end_headers()
            return

        # If the path doesn't exist but path.html does, serve that instead.
        # Example: /auth/callback -> /auth/callback.html
        if (not os.path.exists(local_path)) and os.path.exists(local_path + ".html"):
            self.path = self.path + ".html"

        return super().do_GET()


os.chdir(os.path.join(os.path.dirname(__file__), DIRECTORY))

with ReusableTCPServer(("", PORT), CleanUrlHandler) as httpd:
    print(f"Serving TabMail Docs at http://localhost:{PORT}")
    print("Clean URLs enabled:")
    print(f"  - http://localhost:{PORT}/getting-started -> redirects to /getting-started/")
    print(f"  - http://localhost:{PORT}/faq -> redirects to /faq/")
    print(f"  - http://localhost:{PORT}/some/page -> serves /some/page.html if present")
    httpd.serve_forever()


