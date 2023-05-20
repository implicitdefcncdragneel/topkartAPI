import json
from rest_framework.renderers import JSONRenderer

class CustomeJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context and 'response' in renderer_context:
            response = renderer_context['response']
            status_code = response.status_code
            if status_code >= 400:
                # Error response
                if isinstance(data, dict):
                    errors = data
                else:
                    errors = { "detail" : data } if isinstance(data, list) else { "detail" : str(data) } 
                error_response = {
                    "errors": errors,
                    "status_code": status_code
                }
                return json.dumps(error_response)
        return json.dumps({"message": data})