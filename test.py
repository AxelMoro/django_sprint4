 app_list = resolver.app_dict[ns]
                    # Yes! Path part matches an app in the current Resolver.
                    if current_ns and current_ns in app_list:
                        # If we are reversing for a particular app, use that
                        # namespace.
                        ns = current_ns
                    elif ns not in app_list:
                        # The name isn't shared by one of the instances (i.e.,
                        # the default) so pick the first instance as the default.
                        ns = app_list[0]
                except KeyError:
                    pass

                if ns != current_ns:
                    current_path = None

                try:
>                   extra, resolver = resolver.namespace_dict[ns]
E                   KeyError: 'registration'

venv\lib\site-packages\django\urls\base.py:71: KeyError

During handling of the above exception, another exception occurred:

self = <form.comment.create_form_tester.CreateCommentFormTester object at 0x000001E8B6153E50>, form = <CommentForm bound=True, valid=True, fields=(text)>, qs = <QuerySet []>
submitter = <form.base_form_tester.AnonymousSubmitTester object at 0x000001E8B6166180>, assert_created = False

    def try_create_item(
            self, form: BaseForm, qs: QuerySet,
            submitter: SubmitTester,
            assert_created: bool = True
    ) -> Tuple[HttpResponse, Model]:
    
        if not form.is_valid():
            raise FormValidationException(form.errors)
        elif form.errors:
            raise FormValidationException(form.errors)

        items_before = set(qs.all())

        restored_data = restore_cleaned_data(form.cleaned_data)
        try:
>           response = submitter.test_submit(
                url=self._action, data=restored_data)

tests\form\base_form_tester.py:120:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <form.base_form_tester.AnonymousSubmitTester object at 0x000001E8B6166180>, url = '/posts/2/comment/', data = {'text': 'Test create comment 1847432 text'}

    def test_submit(self, url: str, data: dict) -> HttpResponse:
        assert isinstance(self.client, django.test.Client)
>       response = self.client.post(url, data=data, follow=True)

tests\form\base_form_tester.py:388:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B6061AC0>, path = '/posts/2/comment/', data = {'text': 'Test create comment 1847432 text'}, content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg', follow = True
secure = False, extra = {}

    def post(self, path, data=None, content_type=MULTIPART_CONTENT,
             follow=False, secure=False, **extra):
        """Request a response from the server using POST."""
        self.extra = extra
>       response = super().post(path, data=data, content_type=content_type, secure=secure, **extra)

venv\lib\site-packages\django\test\client.py:751:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B6061AC0>, path = '/posts/2/comment/', data = {'text': 'Test create comment 1847432 text'}, content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg', secure = False
extra = {}, post_data = b'--BoUnDaRyStRiNg\r\nContent-Disposition: form-data; name="text"\r\n\r\nTest create comment 1847432 text\r\n--BoUnDaRyStRiNg--\r\n'

    def post(self, path, data=None, content_type=MULTIPART_CONTENT,
             secure=False, **extra):
        """Construct a POST request."""
        data = self._encode_json({} if data is None else data, content_type)
        post_data = self._encode_data(data, content_type)

>       return self.generic('POST', path, post_data, content_type,
                            secure=secure, **extra)

venv\lib\site-packages\django\test\client.py:407:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B6061AC0>, method = 'POST', path = '/posts/2/comment/'
data = b'--BoUnDaRyStRiNg\r\nContent-Disposition: form-data; name="text"\r\n\r\nTest create comment 1847432 text\r\n--BoUnDaRyStRiNg--\r\n', content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg', secure = False, extra = {}   
parsed = ParseResult(scheme='', netloc='', path='/posts/2/comment/', params='', query='', fragment='')
r = {'CONTENT_LENGTH': '119', 'CONTENT_TYPE': 'multipart/form-data; boundary=BoUnDaRyStRiNg', 'PATH_INFO': '/posts/2/comment/', 'QUERY_STRING': '', ...}, query_string = ''

    def generic(self, method, path, data='',
                content_type='application/octet-stream', secure=False,
                **extra):
        """Construct an arbitrary HTTP request."""
        parsed = urlparse(str(path))  # path can be lazy
        data = force_bytes(data, settings.DEFAULT_CHARSET)
        r = {
            'PATH_INFO': self._get_path(parsed),
            'REQUEST_METHOD': method,
            'SERVER_PORT': '443' if secure else '80',
            'wsgi.url_scheme': 'https' if secure else 'http',
        }
        if data:
            r.update({
                'CONTENT_LENGTH': str(len(data)),
                'CONTENT_TYPE': content_type,
                'wsgi.input': FakePayload(data),
            })
        r.update(extra)
        # If QUERY_STRING is absent or empty, we want to extract it from the URL.
        if not r.get('QUERY_STRING'):
            # WSGI requires latin-1 encoded strings. See get_path_info().
            query_string = parsed[4].encode().decode('iso-8859-1')
            r['QUERY_STRING'] = query_string
>       return self.request(**r)

venv\lib\site-packages\django\test\client.py:473:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B6061AC0>, request = {'CONTENT_LENGTH': '119', 'CONTENT_TYPE': 'multipart/form-data; boundary=BoUnDaRyStRiNg', 'PATH_INFO': '/posts/2/comment/', 'QUERY_STRING': '', ...}
environ = {'CONTENT_LENGTH': '119', 'CONTENT_TYPE': 'multipart/form-data; boundary=BoUnDaRyStRiNg', 'HTTP_COOKIE': '', 'PATH_INFO': '/posts/2/comment/', ...}
data = {'context': [[{'True': True, 'False': False, 'None': None}, {'is_email': False, 'unicode_hint': '', 'frames': [{'exc_c...)', '', ''], 'pre_context_lineno': 75}}]], 'templates': [<django.template.base.Template object at 0x000001E8B61801F0>]}
on_template_render = functools.partial(<function store_rendered_templates at 0x000001E8B4236550>, {'templates': [<django.template.base.Temp... '', '    return resolver._reverse_with_prefix(view, prefix, *args, **kwargs)', '', ''], 'pre_context_lineno': 75}}]]})
signal_uid = 'template-render-2098981220480', exception_uid = 'request-exception-2098981220480', response = <HttpResponse status_code=500, "text/html">

    def request(self, **request):
        """
        The master request method. Compose the environment dictionary and pass
        to the handler, return the result of the handler. Assume defaults for
        the query environment, which can be overridden using the arguments to
        the request.
        """
        environ = self._base_environ(**request)

        # Curry a data dictionary into an instance of the template renderer
        # callback function.
        data = {}
        on_template_render = partial(store_rendered_templates, data)
        signal_uid = "template-render-%s" % id(request)
        signals.template_rendered.connect(on_template_render, dispatch_uid=signal_uid)
        # Capture exceptions created by the handler.
        exception_uid = "request-exception-%s" % id(request)
        got_request_exception.connect(self.store_exc_info, dispatch_uid=exception_uid)
        try:
            response = self.handler(environ)
        finally:
            signals.template_rendered.disconnect(dispatch_uid=signal_uid)
            got_request_exception.disconnect(dispatch_uid=exception_uid)
        # Check for signaled exceptions.
>       self.check_exception(response)

venv\lib\site-packages\django\test\client.py:719:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B6061AC0>, response = <HttpResponse status_code=500, "text/html">

    def check_exception(self, response):
        """
        Look for a signaled exception, clear the current context exception
        data, re-raise the signaled exception, and clear the signaled exception
        from the local cache.
        """
        response.exc_info = self.exc_info
        if self.exc_info:
            _, exc_value, _ = self.exc_info
            self.exc_info = None
            if self.raise_request_exception:
>               raise exc_value

venv\lib\site-packages\django\test\client.py:580:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

request = <WSGIRequest: POST '/posts/2/comment/'>

    @wraps(get_response)
    def inner(request):
        try:
>           response = get_response(request)

venv\lib\site-packages\django\core\handlers\exception.py:47:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.ClientHandler object at 0x000001E8B6061A60>, request = <WSGIRequest: POST '/posts/2/comment/'>

    def _get_response(self, request):
        """
        Resolve and call the view, then apply view, exception, and
        template_response middleware. This method is everything that happens
        inside the request/response middleware.
        """
        response = None
        callback, callback_args, callback_kwargs = self.resolve_request(request)

        # Apply view middleware
        for middleware_method in self._view_middleware:
            response = middleware_method(request, callback, callback_args, callback_kwargs)
            if response:
                break

        if response is None:
            wrapped_callback = self.make_view_atomic(callback)
            # If it is an asynchronous view, run it in a subthread.
            if asyncio.iscoroutinefunction(wrapped_callback):
                wrapped_callback = async_to_sync(wrapped_callback)
            try:
>               response = wrapped_callback(request, *callback_args, **callback_kwargs)

venv\lib\site-packages\django\core\handlers\base.py:181:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

request = <WSGIRequest: POST '/posts/2/comment/'>, args = (), kwargs = {'post_id': '2'}, path = 'http://testserver/posts/2/comment/'

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if test_func(request.user):
            return view_func(request, *args, **kwargs)
        path = request.build_absolute_uri()
>       resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)

venv\lib\site-packages\django\contrib\auth\decorators.py:23:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

to = 'registration:login', args = (), kwargs = {}

    def resolve_url(to, *args, **kwargs):
        """
        Return a URL appropriate for the arguments passed.

        The arguments could be:

            * A model: the model's `get_absolute_url()` function will be called.

            * A view name, possibly with arguments: `urls.reverse()` will be used
              to reverse-resolve the name.

            * A URL, which will be returned as-is.
        """
        # If it's a model, use get_absolute_url()
        if hasattr(to, 'get_absolute_url'):
            return to.get_absolute_url()

        if isinstance(to, Promise):
            # Expand the lazy instance, as it can cause issues when it is passed
            # further to some Python functions like urlparse.
            to = str(to)

        # Handle relative URLs
        if isinstance(to, str) and to.startswith(('./', '../')):
            return to

        # Next try a reverse URL resolution.
        try:
>           return reverse(to, args=args, kwargs=kwargs)

venv\lib\site-packages\django\shortcuts.py:130:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

viewname = 'registration:login', urlconf = 'blogicum.urls', args = [], kwargs = {}, current_app = None

    def reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None):
        if urlconf is None:
            urlconf = get_urlconf()
        resolver = get_resolver(urlconf)
        args = args or []
        kwargs = kwargs or {}

        prefix = get_script_prefix()

        if not isinstance(viewname, str):
            view = viewname
        else:
            *path, view = viewname.split(':')

            if current_app:
                current_path = current_app.split(':')
                current_path.reverse()
            else:
                current_path = None

            resolved_path = []
            ns_pattern = ''
            ns_converters = {}
            for ns in path:
                current_ns = current_path.pop() if current_path else None
                # Lookup the name to see if it could be an app identifier.
                try:
                    app_list = resolver.app_dict[ns]
                    # Yes! Path part matches an app in the current Resolver.
                    if current_ns and current_ns in app_list:
                        # If we are reversing for a particular app, use that
                        # namespace.
                        ns = current_ns
                    elif ns not in app_list:
                        # The name isn't shared by one of the instances (i.e.,
                        # the default) so pick the first instance as the default.
                        ns = app_list[0]
                except KeyError:
                    pass

                if ns != current_ns:
                    current_path = None

                try:
                    extra, resolver = resolver.namespace_dict[ns]
                    resolved_path.append(ns)
                    ns_pattern = ns_pattern + extra
                    ns_converters.update(resolver.pattern.converters)
                except KeyError as key:
                    if resolved_path:
                        raise NoReverseMatch(
                            "%s is not a registered namespace inside '%s'" %
                            (key, ':'.join(resolved_path))
                        )
                    else:
>                       raise NoReverseMatch("%s is not a registered namespace" % key)
E                       django.urls.exceptions.NoReverseMatch: 'registration' is not a registered namespace

venv\lib\site-packages\django\urls\base.py:82: NoReverseMatch

During handling of the above exception, another exception occurred:

user_client = <django.test.client.Client object at 0x000001E8B6116A30>, another_user_client = <django.test.client.Client object at 0x000001E8B6061940>, unlogged_client = <django.test.client.Client object at 0x000001E8B6061AC0>       
post_with_published_location = <Post: Down Nice Miss Bank A Reason>, another_user = <User: tara20>, post_comment_context_form_item = KeyVal(key='form', val=<CommentForm bound=False, valid=False, fields=(text)>)
CommentModel = <class 'blog.models.Comment'>, CommentModelAdapter = <class 'adapters.comment.CommentModelAdapter.<locals>._CommentModelAdapter'>

    @pytest.mark.django_db(transaction=True)
    def test_comment(
            user_client: django.test.Client,
            another_user_client: django.test.Client,
            unlogged_client: django.test.Client,
            post_with_published_location: Any,
            another_user: Model,
            post_comment_context_form_item: Tuple[str, BaseForm],
            CommentModel: Type[Model],
            CommentModelAdapter: CommentModelAdapterT):
        post_with_published_location.author = another_user
        post_with_published_location.save()
        _, ctx_form = post_comment_context_form_item
        a_post_get_response = get_a_post_get_response_safely(
            user_client, post_with_published_location.id)

        # create comments
        creation_tester = CreateCommentFormTester(
            a_post_get_response, CommentModel, user_client,
            another_user_client, unlogged_client, item_adapter=None,
            ModelAdapter=CommentModelAdapter)

        Form: Type[BaseForm] = type(ctx_form)

        item_ix_start: int = random.randint(1000000, 2000000)
        item_ix_cnt: int = 5
        rand_range = list(range(item_ix_start, item_ix_start + item_ix_cnt))
        forms_data = []
        for i in rand_range:
            forms_data.append({'text': f'Test create comment {i} text'})

        forms_to_create = creation_tester.init_create_item_forms(
            Form, Model=CommentModel, ModelAdapter=CommentModelAdapter,
            forms_unadapted_data=forms_data
        )
        try:
>           creation_tester.test_unlogged_cannot_create(
                form=forms_to_create[0], qs=CommentModel.objects.all())

tests\test_comment.py:89:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
tests\form\base_form_tester.py:170: in test_unlogged_cannot_create
    self.test_create_item(
tests\form\base_form_tester.py:195: in test_create_item
    response, created = self.try_create_item(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <form.comment.create_form_tester.CreateCommentFormTester object at 0x000001E8B6153E50>, form = <CommentForm bound=True, valid=True, fields=(text)>, qs = <QuerySet []>
submitter = <form.base_form_tester.AnonymousSubmitTester object at 0x000001E8B6166180>, assert_created = False

    def try_create_item(
            self, form: BaseForm, qs: QuerySet,
            submitter: SubmitTester,
            assert_created: bool = True
    ) -> Tuple[HttpResponse, Model]:

        if not form.is_valid():
            raise FormValidationException(form.errors)
        elif form.errors:
            raise FormValidationException(form.errors)

        items_before = set(qs.all())

        restored_data = restore_cleaned_data(form.cleaned_data)
        try:
            response = submitter.test_submit(
                url=self._action, data=restored_data)
        except Exception as e:
>           raise AssertionError(
                f'При создании {self.of_which_obj} {self.on_which_page} '
                f'возникает ошибка:\n'
                f'{type(e).__name__}: {e}'
            )
E           AssertionError: При создании комментария на странице создания комментария возникает ошибка:
E           NoReverseMatch: 'registration' is not a registered namespace

tests\form\base_form_tester.py:123: AssertionError
--------------------------------------------------------------------------------------------------------- Captured stderr call --------------------------------------------------------------------------------------------------------- 
Internal Server Error: /posts/2/comment/
Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 71, in reverse
    extra, resolver = resolver.namespace_dict[ns]
KeyError: 'registration'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\exception.py", line 47, in inner
    response = get_response(request)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\contrib\auth\decorators.py", line 23, in _wrapped_view
    resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\shortcuts.py", line 130, in resolve_url
    return reverse(to, args=args, kwargs=kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 82, in reverse
    raise NoReverseMatch("%s is not a registered namespace" % key)
django.urls.exceptions.NoReverseMatch: 'registration' is not a registered namespace
---------------------------------------------------------------------------------------------------------- Captured log call ----------------------------------------------------------------------------------------------------------- 
ERROR    django.request:log.py:224 Internal Server Error: /posts/2/comment/
Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 71, in reverse
    extra, resolver = resolver.namespace_dict[ns]
KeyError: 'registration'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\exception.py", line 47, in inner
    response = get_response(request)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\contrib\auth\decorators.py", line 23, in _wrapped_view
    resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\shortcuts.py", line 130, in resolve_url
    return reverse(to, args=args, kwargs=kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 82, in reverse
    raise NoReverseMatch("%s is not a registered namespace" % key)
django.urls.exceptions.NoReverseMatch: 'registration' is not a registered namespace
______________________________________________________________________________________________________________ test_post _______________________________________________________________________________________________________________ 

viewname = 'registration:login', urlconf = 'blogicum.urls', args = [], kwargs = {}, current_app = None

    def reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None):
        if urlconf is None:
            urlconf = get_urlconf()
        resolver = get_resolver(urlconf)
        args = args or []
        kwargs = kwargs or {}

        prefix = get_script_prefix()

        if not isinstance(viewname, str):
            view = viewname
        else:
            *path, view = viewname.split(':')

            if current_app:
                current_path = current_app.split(':')
                current_path.reverse()
            else:
                current_path = None

            resolved_path = []
            ns_pattern = ''
            ns_converters = {}
            for ns in path:
                current_ns = current_path.pop() if current_path else None
                # Lookup the name to see if it could be an app identifier.
                try:
                    app_list = resolver.app_dict[ns]
                    # Yes! Path part matches an app in the current Resolver.
                    if current_ns and current_ns in app_list:
                        # If we are reversing for a particular app, use that
                        # namespace.
                        ns = current_ns
                    elif ns not in app_list:
                        # The name isn't shared by one of the instances (i.e.,
                        # the default) so pick the first instance as the default.
                        ns = app_list[0]
                except KeyError:
                    pass

                if ns != current_ns:
                    current_path = None

                try:
>                   extra, resolver = resolver.namespace_dict[ns]
E                   KeyError: 'registration'

venv\lib\site-packages\django\urls\base.py:71: KeyError

During handling of the above exception, another exception occurred:

self = <form.post.create_form_tester.CreatePostFormTester object at 0x000001E8B605BC40>, form = <PostForm bound=True, valid=True, fields=(title;text;pub_date;image;location;category)>
qs = <QuerySet [<Post: Kitchen Full Whatever Station Already Of>]>, submitter = <form.base_form_tester.AnonymousSubmitTester object at 0x000001E8B60A8BD0>, assert_created = False

    def try_create_item(
            self, form: BaseForm, qs: QuerySet,
            submitter: SubmitTester,
            assert_created: bool = True
    ) -> Tuple[HttpResponse, Model]:

        if not form.is_valid():
            raise FormValidationException(form.errors)
        elif form.errors:
            raise FormValidationException(form.errors)

        items_before = set(qs.all())

        restored_data = restore_cleaned_data(form.cleaned_data)
        try:
>           response = submitter.test_submit(
                url=self._action, data=restored_data)

tests\form\base_form_tester.py:120:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <form.base_form_tester.AnonymousSubmitTester object at 0x000001E8B60A8BD0>, url = '/posts/create/'
data = {'category': 4, 'image': <SimpleUploadedFile: test_image.jpg (image/jpeg)>, 'location': 3, 'pub_date': datetime.datetime(2023, 5, 26, 19, 40, 54, 649239, tzinfo=<UTC>), ...}

    def test_submit(self, url: str, data: dict) -> HttpResponse:
        assert isinstance(self.client, django.test.Client)
>       response = self.client.post(url, data=data, follow=True)

tests\form\base_form_tester.py:388:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B60F5250>, path = '/posts/create/'
data = {'category': 4, 'image': <SimpleUploadedFile: test_image.jpg (image/jpeg)>, 'location': 3, 'pub_date': datetime.datetime(2023, 5, 26, 19, 40, 54, 649239, tzinfo=<UTC>), ...}
content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg', follow = True, secure = False, extra = {}

    def post(self, path, data=None, content_type=MULTIPART_CONTENT,
             follow=False, secure=False, **extra):
        """Request a response from the server using POST."""
        self.extra = extra
>       response = super().post(path, data=data, content_type=content_type, secure=secure, **extra)

venv\lib\site-packages\django\test\client.py:751:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B60F5250>, path = '/posts/create/'
data = {'category': 4, 'image': <SimpleUploadedFile: test_image.jpg (image/jpeg)>, 'location': 3, 'pub_date': datetime.datetime(2023, 5, 26, 19, 40, 54, 649239, tzinfo=<UTC>), ...}
content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg', secure = False, extra = {}
post_data = b'--BoUnDaRyStRiNg\r\nContent-Disposition: form-data; name="title"\r\n\r\nTest create post 1980247 title\r\n--BoUnDaRy...on"\r\n\r\n3\r\n--BoUnDaRyStRiNg\r\nContent-Disposition: form-data; name="category"\r\n\r\n4\r\n--BoUnDaRyStRiNg--\r\n'

    def post(self, path, data=None, content_type=MULTIPART_CONTENT,
             secure=False, **extra):
        """Construct a POST request."""
        data = self._encode_json({} if data is None else data, content_type)
        post_data = self._encode_data(data, content_type)

>       return self.generic('POST', path, post_data, content_type,
                            secure=secure, **extra)

venv\lib\site-packages\django\test\client.py:407:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B60F5250>, method = 'POST', path = '/posts/create/'
data = b'--BoUnDaRyStRiNg\r\nContent-Disposition: form-data; name="title"\r\n\r\nTest create post 1980247 title\r\n--BoUnDaRy...on"\r\n\r\n3\r\n--BoUnDaRyStRiNg\r\nContent-Disposition: form-data; name="category"\r\n\r\n4\r\n--BoUnDaRyStRiNg--\r\n'
content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg', secure = False, extra = {}, parsed = ParseResult(scheme='', netloc='', path='/posts/create/', params='', query='', fragment='')
r = {'CONTENT_LENGTH': '1405', 'CONTENT_TYPE': 'multipart/form-data; boundary=BoUnDaRyStRiNg', 'PATH_INFO': '/posts/create/', 'QUERY_STRING': '', ...}, query_string = ''

    def generic(self, method, path, data='',
                content_type='application/octet-stream', secure=False,
                **extra):
        """Construct an arbitrary HTTP request."""
        parsed = urlparse(str(path))  # path can be lazy
        data = force_bytes(data, settings.DEFAULT_CHARSET)
        r = {
            'PATH_INFO': self._get_path(parsed),
            'REQUEST_METHOD': method,
            'SERVER_PORT': '443' if secure else '80',
            'wsgi.url_scheme': 'https' if secure else 'http',
        }
        if data:
            r.update({
                'CONTENT_LENGTH': str(len(data)),
                'CONTENT_TYPE': content_type,
                'wsgi.input': FakePayload(data),
            })
        r.update(extra)
        # If QUERY_STRING is absent or empty, we want to extract it from the URL.
        if not r.get('QUERY_STRING'):
            # WSGI requires latin-1 encoded strings. See get_path_info().
            query_string = parsed[4].encode().decode('iso-8859-1')
            r['QUERY_STRING'] = query_string
>       return self.request(**r)

venv\lib\site-packages\django\test\client.py:473:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B60F5250>, request = {'CONTENT_LENGTH': '1405', 'CONTENT_TYPE': 'multipart/form-data; boundary=BoUnDaRyStRiNg', 'PATH_INFO': '/posts/create/', 'QUERY_STRING': '', ...}
environ = {'CONTENT_LENGTH': '1405', 'CONTENT_TYPE': 'multipart/form-data; boundary=BoUnDaRyStRiNg', 'HTTP_COOKIE': '', 'PATH_INFO': '/posts/create/', ...}
data = {'context': [[{'True': True, 'False': False, 'None': None}, {'is_email': False, 'unicode_hint': '', 'frames': [{'exc_c...)', '', ''], 'pre_context_lineno': 75}}]], 'templates': [<django.template.base.Template object at 0x000001E8B61F6880>]}
on_template_render = functools.partial(<function store_rendered_templates at 0x000001E8B4236550>, {'templates': [<django.template.base.Temp... '', '    return resolver._reverse_with_prefix(view, prefix, *args, **kwargs)', '', ''], 'pre_context_lineno': 75}}]]})
signal_uid = 'template-render-2098999464896', exception_uid = 'request-exception-2098999464896', response = <HttpResponse status_code=500, "text/html">

    def request(self, **request):
        """
        The master request method. Compose the environment dictionary and pass
        to the handler, return the result of the handler. Assume defaults for
        the query environment, which can be overridden using the arguments to
        the request.
        """
        environ = self._base_environ(**request)

        # Curry a data dictionary into an instance of the template renderer
        # callback function.
        data = {}
        on_template_render = partial(store_rendered_templates, data)
        signal_uid = "template-render-%s" % id(request)
        signals.template_rendered.connect(on_template_render, dispatch_uid=signal_uid)
        # Capture exceptions created by the handler.
        exception_uid = "request-exception-%s" % id(request)
        got_request_exception.connect(self.store_exc_info, dispatch_uid=exception_uid)
        try:
            response = self.handler(environ)
        finally:
            signals.template_rendered.disconnect(dispatch_uid=signal_uid)
            got_request_exception.disconnect(dispatch_uid=exception_uid)
        # Check for signaled exceptions.
>       self.check_exception(response)

venv\lib\site-packages\django\test\client.py:719:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.Client object at 0x000001E8B60F5250>, response = <HttpResponse status_code=500, "text/html">

    def check_exception(self, response):
        """
        Look for a signaled exception, clear the current context exception
        data, re-raise the signaled exception, and clear the signaled exception
        from the local cache.
        """
        response.exc_info = self.exc_info
        if self.exc_info:
            _, exc_value, _ = self.exc_info
            self.exc_info = None
            if self.raise_request_exception:
>               raise exc_value

venv\lib\site-packages\django\test\client.py:580:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

request = <WSGIRequest: POST '/posts/create/'>

    @wraps(get_response)
    def inner(request):
        try:
>           response = get_response(request)

venv\lib\site-packages\django\core\handlers\exception.py:47:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <django.test.client.ClientHandler object at 0x000001E8B60F5DF0>, request = <WSGIRequest: POST '/posts/create/'>

    def _get_response(self, request):
        """
        Resolve and call the view, then apply view, exception, and
        template_response middleware. This method is everything that happens
        inside the request/response middleware.
        """
        response = None
        callback, callback_args, callback_kwargs = self.resolve_request(request)

        # Apply view middleware
        for middleware_method in self._view_middleware:
            response = middleware_method(request, callback, callback_args, callback_kwargs)
            if response:
                break

        if response is None:
            wrapped_callback = self.make_view_atomic(callback)
            # If it is an asynchronous view, run it in a subthread.
            if asyncio.iscoroutinefunction(wrapped_callback):
                wrapped_callback = async_to_sync(wrapped_callback)
            try:
>               response = wrapped_callback(request, *callback_args, **callback_kwargs)

venv\lib\site-packages\django\core\handlers\base.py:181:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

request = <WSGIRequest: POST '/posts/create/'>, args = (), kwargs = {}, self = <blog.views.PostCreateView object at 0x000001E8B61F66D0>

    def view(request, *args, **kwargs):
        self = cls(**initkwargs)
        self.setup(request, *args, **kwargs)
        if not hasattr(self, 'request'):
            raise AttributeError(
                "%s instance has no 'request' attribute. Did you override "
                "setup() and forget to call super()?" % cls.__name__
            )
>       return self.dispatch(request, *args, **kwargs)

venv\lib\site-packages\django\views\generic\base.py:70:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <blog.views.PostCreateView object at 0x000001E8B61F66D0>, request = <WSGIRequest: POST '/posts/create/'>, args = (), kwargs = {}

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
>           return self.handle_no_permission()

venv\lib\site-packages\django\contrib\auth\mixins.py:70:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <blog.views.PostCreateView object at 0x000001E8B61F66D0>

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())

        path = self.request.build_absolute_uri()
>       resolved_login_url = resolve_url(self.get_login_url())

venv\lib\site-packages\django\contrib\auth\mixins.py:49:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

to = 'registration:login', args = (), kwargs = {}

    def resolve_url(to, *args, **kwargs):
        """
        Return a URL appropriate for the arguments passed.

        The arguments could be:

            * A model: the model's `get_absolute_url()` function will be called.

            * A view name, possibly with arguments: `urls.reverse()` will be used
              to reverse-resolve the name.

            * A URL, which will be returned as-is.
        """
        # If it's a model, use get_absolute_url()
        if hasattr(to, 'get_absolute_url'):
            return to.get_absolute_url()

        if isinstance(to, Promise):
            # Expand the lazy instance, as it can cause issues when it is passed
            # further to some Python functions like urlparse.
            to = str(to)

        # Handle relative URLs
        if isinstance(to, str) and to.startswith(('./', '../')):
            return to

        # Next try a reverse URL resolution.
        try:
>           return reverse(to, args=args, kwargs=kwargs)

venv\lib\site-packages\django\shortcuts.py:130:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

viewname = 'registration:login', urlconf = 'blogicum.urls', args = [], kwargs = {}, current_app = None

    def reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None):
        if urlconf is None:
            urlconf = get_urlconf()
        resolver = get_resolver(urlconf)
        args = args or []
        kwargs = kwargs or {}

        prefix = get_script_prefix()

        if not isinstance(viewname, str):
            view = viewname
        else:
            *path, view = viewname.split(':')

            if current_app:
                current_path = current_app.split(':')
                current_path.reverse()
            else:
                current_path = None

            resolved_path = []
            ns_pattern = ''
            ns_converters = {}
            for ns in path:
                current_ns = current_path.pop() if current_path else None
                # Lookup the name to see if it could be an app identifier.
                try:
                    app_list = resolver.app_dict[ns]
                    # Yes! Path part matches an app in the current Resolver.
                    if current_ns and current_ns in app_list:
                        # If we are reversing for a particular app, use that
                        # namespace.
                        ns = current_ns
                    elif ns not in app_list:
                        # The name isn't shared by one of the instances (i.e.,
                        # the default) so pick the first instance as the default.
                        ns = app_list[0]
                except KeyError:
                    pass
    
                if ns != current_ns:
                    current_path = None

                try:
                    extra, resolver = resolver.namespace_dict[ns]
                    resolved_path.append(ns)
                    ns_pattern = ns_pattern + extra
                    ns_converters.update(resolver.pattern.converters)
                except KeyError as key:
                    if resolved_path:
                        raise NoReverseMatch(
                            "%s is not a registered namespace inside '%s'" %
                            (key, ':'.join(resolved_path))
                        )
                    else:
>                       raise NoReverseMatch("%s is not a registered namespace" % key)
E                       django.urls.exceptions.NoReverseMatch: 'registration' is not a registered namespace

venv\lib\site-packages\django\urls\base.py:82: NoReverseMatch

During handling of the above exception, another exception occurred:

published_category = <Category: Fast Down Step Color Focus Father>, published_location = <Location: Mr. Garrett Allen>, user_client = <django.test.client.Client object at 0x000001E8B6061B80>
another_user_client = <django.test.client.Client object at 0x000001E8B628B160>, unlogged_client = <django.test.client.Client object at 0x000001E8B60F5250>
comment_to_a_post = <Comment: South during second onto beat. Political shake she card lead maybe. Top continue mention traditional somebody.>
create_post_context_form_item = KeyVal(key='form', val=<PostForm bound=False, valid=False, fields=(title;text;pub_date;image;location;category)>), PostModel = <class 'blog.models.Post'>
CommentModelAdapter = <class 'adapters.comment.CommentModelAdapter.<locals>._CommentModelAdapter'>

    @pytest.mark.django_db(transaction=True)
    def test_post(
            published_category: Model,
            published_location: Model,
            user_client: django.test.Client,
            another_user_client: django.test.Client,
            unlogged_client: django.test.Client,
            comment_to_a_post: Model,
            create_post_context_form_item: Tuple[str, BaseForm],
            PostModel: Type[Model],
            CommentModelAdapter: CommentModelAdapterT
    ):
        _, ctx_form = create_post_context_form_item

        create_a_post_get_response = get_create_a_post_get_response_safely(
            user_client)

>       response_on_created, created_items = _test_create_items(
            PostModel, PostModelAdapter,
            another_user_client,
            create_a_post_get_response, ctx_form,
            published_category, published_location,
            unlogged_client, user_client)

tests\test_post.py:73:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
tests\test_post.py:133: in _test_create_items
    creation_tester.test_unlogged_cannot_create(
tests\form\base_form_tester.py:170: in test_unlogged_cannot_create
    self.test_create_item(
tests\form\base_form_tester.py:195: in test_create_item
    response, created = self.try_create_item(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

self = <form.post.create_form_tester.CreatePostFormTester object at 0x000001E8B605BC40>, form = <PostForm bound=True, valid=True, fields=(title;text;pub_date;image;location;category)>
qs = <QuerySet [<Post: Kitchen Full Whatever Station Already Of>]>, submitter = <form.base_form_tester.AnonymousSubmitTester object at 0x000001E8B60A8BD0>, assert_created = False

    def try_create_item(
            self, form: BaseForm, qs: QuerySet,
            submitter: SubmitTester,
            assert_created: bool = True
    ) -> Tuple[HttpResponse, Model]:

        if not form.is_valid():
            raise FormValidationException(form.errors)
        elif form.errors:
            raise FormValidationException(form.errors)

        items_before = set(qs.all())

        restored_data = restore_cleaned_data(form.cleaned_data)
        try:
            response = submitter.test_submit(
                url=self._action, data=restored_data)
        except Exception as e:
>           raise AssertionError(
                f'При создании {self.of_which_obj} {self.on_which_page} '
                f'возникает ошибка:\n'
                f'{type(e).__name__}: {e}'
            )
E           AssertionError: При создании публикации на странице создания публикации возникает ошибка:
E           NoReverseMatch: 'registration' is not a registered namespace

tests\form\base_form_tester.py:123: AssertionError
--------------------------------------------------------------------------------------------------------- Captured stderr call --------------------------------------------------------------------------------------------------------- 
Internal Server Error: /posts/create/
Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 71, in reverse
    extra, resolver = resolver.namespace_dict[ns]
KeyError: 'registration'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\exception.py", line 47, in inner
    response = get_response(request)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\views\generic\base.py", line 70, in view
    return self.dispatch(request, *args, **kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\contrib\auth\mixins.py", line 70, in dispatch
    return self.handle_no_permission()
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\contrib\auth\mixins.py", line 49, in handle_no_permission
    resolved_login_url = resolve_url(self.get_login_url())
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\shortcuts.py", line 130, in resolve_url
    return reverse(to, args=args, kwargs=kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 82, in reverse
    raise NoReverseMatch("%s is not a registered namespace" % key)
django.urls.exceptions.NoReverseMatch: 'registration' is not a registered namespace
---------------------------------------------------------------------------------------------------------- Captured log call ----------------------------------------------------------------------------------------------------------- 
ERROR    django.request:log.py:224 Internal Server Error: /posts/create/
Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 71, in reverse
    extra, resolver = resolver.namespace_dict[ns]
KeyError: 'registration'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\exception.py", line 47, in inner
    response = get_response(request)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\core\handlers\base.py", line 181, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\views\generic\base.py", line 70, in view
    return self.dispatch(request, *args, **kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\contrib\auth\mixins.py", line 70, in dispatch
    return self.handle_no_permission()
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\contrib\auth\mixins.py", line 49, in handle_no_permission
    resolved_login_url = resolve_url(self.get_login_url())
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\shortcuts.py", line 130, in resolve_url
    return reverse(to, args=args, kwargs=kwargs)
  File "D:\Dev\django_sprint4\venv\lib\site-packages\django\urls\base.py", line 82, in reverse
    raise NoReverseMatch("%s is not a registered namespace" % key)
django.urls.exceptions.NoReverseMatch: 'registration' is not a registered namespace
_______________________________________________________________________________________________________ test_static_pages_as_cbv _______________________________________________________________________________________________________ 

    def test_static_pages_as_cbv():
        try:
            from pages import urls
        except Exception as e:
            raise AssertionError(
                'Убедитесь, что в файле `pages/urls.py` нет ошибок. '
                'При его импорте возникла ошибка:\n'
                f'{type(e).__name__}: {e}'
            )
        try:
            from pages.urls import urlpatterns
        except Exception as e:
            raise AssertionError(
                'Убедитесь, что в файле `pages/urls.py` задан список urlpatterns.'
            )
        try:
            from pages.urls import app_name
        except Exception as e:
            raise AssertionError(
                'Убедитесь, что в файле `pages/urls.py` определена глобальная переменная `app_name`, '
                'задающая пространство имён url для приложения `pages`.'
            )
        for path in urlpatterns:
            if not hasattr(path.callback, 'view_class'):
>               raise AssertionError(
                    'Убедитесь, что в файле `pages/urls.py` подключаете маршруты '
                    'статических страниц, используя CBV.'
                )
E               AssertionError: Убедитесь, что в файле `pages/urls.py` подключаете маршруты статических страниц, используя CBV.

tests\test_static_pages.py:25: AssertionError
------------------------------------------------------------------------------------------------------- Captured stderr teardown ------------------------------------------------------------------------------------------------------- 
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
======================================================================================================= short test summary info ======================================================================================================== 
FAILED tests/test_users.py::test_profile - django.urls.exceptions.NoReverseMatch: 'registration' is not a registered namespace
FAILED tests/test_comment.py::test_comment - AssertionError: При создании комментария на странице создания комментария возникает ошибка:
FAILED tests/test_post.py::test_post - AssertionError: При создании публикации на странице создания публикации возникает ошибка:
FAILED tests/test_static_pages.py::test_static_pages_as_cbv - AssertionError: Убедитесь, что в файле `pages/urls.py` подключаете маршруты статических страниц, используя CBV.