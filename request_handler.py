import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import all, retrieve, get_snakes_by_species, update, create
from urllib.parse import urlparse, parse_qs


method_mapper = {
    'single': retrieve, 'all': all
}


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def get_all_or_single(self, resource, id):
        """Determines whether the client is needing all items or a single item and then calls the correct function.
        """
        if resource in ('species', 'snakes', 'owners'):
            if id is not None:
                response = method_mapper["single"](resource, id)

                if response == []:
                    self._set_headers(405)
                elif response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = ''
            else:
                self._set_headers(200)
                response = method_mapper["all"](resource)
        else:
            self._set_headers(404)

        return response

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/') 
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def do_GET(self):
        """Handles GET requests to the server """

        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            response = None
            (resource, id) = parsed
            response = self.get_all_or_single(resource, id)
        else:  
            response = {}
            (resource, query) = parsed

            if query.get('species') and resource == 'snakes':
                self._set_headers(200)
                response = get_snakes_by_species(query['species'][0])


        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_data = None

        if resource == "snakes":
            if "name" in post_body and "owner_id" in post_body and "species_id" in post_body and "gender" in post_body and "color" in post_body:
                self._set_headers(201)
                new_data = create(resource, post_body)
            else:
                self._set_headers(400)
                new_data = {
                    "message": f'{"name is required" if "name" not in post_body else ""} {"owner_id is required" if "owner_id" not in post_body else ""} {"species_id is required" if "species_id" not in post_body else ""} {"gender is required" if "gender" not in post_body else ""} {"color is required" if "color" not in post_body else ""}'
                }
        else:
            self._set_headers(404)

        self.wfile.write(json.dumps(new_data).encode())

    def do_PUT(self):
       self._set_headers(404)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        self._set_headers(404)

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
