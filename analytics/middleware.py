from typing import Any
from .models import OSAnalytics
import re


class Analytics:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request, *args: Any, **kwds: Any) -> Any:
        if not request.user.is_superuser:
            self.stats(request.META['HTTP_USER_AGENT'])
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Logic executed before a call to view.
        # Gives access to view itself and arguments.
        ...

    def process_exception(self, request, exception):
        # print(f'Exception count: {self.num_exceptions}')
        ...
    
    def process_template_response(self, request, response):
        # response.context_data['new_data'] = self.context_response
        return response
        ...


    def stats(self, os_info):
        os_info = re.sub(r'[^a-zA-Z]', ' ', os_info).split()[1]
        OSAnalytics.objects.create(os=os_info)