from memes.models import Meme
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import AnonymousUser, User
import PIL
from PIL import Image
from memes.views import meme_add

from memes.forms import AddMeme

# Success Codes:
# 200 - OK
# 201 - CREATED
# 202 - ACCEPTED
# 203 - NON_AUTHORITATIVE_INFORMATION
# 204 - NO_CONTENT
# 205 - RESET_CONTENT
# 206 - PARTIAL_CONTENT
# 207 - MULTI_STATUS

# Redirect Codes:
# 300 - MULTIPLE_CHOICES
# 301 - MOVED_PERMANENTLY
# 302 - FOUND
# 303 - SEE_OTHER
# 304 - NOT_MODIFIED
# 305 - USE_PROXY
# 306 - RESERVED
# 307 - TEMPORARY_REDIRECT

# Failure Codes:
# 400 - BAD_REQUEST
# 401 - UNAUTHORIZED
# 402 - PAYMENT_REQUIRED
# 403 - FORBIDDEN
# 404 - NOT_FOUND
# 405 - METHOD_NOT_ALLOWED
# 406 - NOT_ACCEPTABLE
# 407 - PROXY_AUTHENTICATION_REQUIRED
# 408 - REQUEST_TIMEOUT
# 409 - CONFLICT
# 410 - GONE
# 411 - LENGTH_REQUIRED
# 412 - PRECONDITION_FAILED
# 413 - REQUEST_ENTITY_TOO_LARGE
# 414 - REQUEST_URI_TOO_LONG
# 415 - UNSUPPORTED_MEDIA_TYPE
# 416 - REQUESTED_RANGE_NOT_SATISFIABLE
# 417 - EXPECTATION_FAILED
# 422 - UNPROCESSABLE_ENTITY
# 423 - LOCKED
# 424 - FAILED_DEPENDENCY
# 428 - PRECONDITION_REQUIRED
# 429 - TOO_MANY_REQUESTS
# 431 - REQUEST_HEADER_FIELDS_TOO_LARGE
# 451 - UNAVAILABLE_FOR_LEGAL_REASONS

# Server Error:
# 500 - INTERNAL_SERVER_ERROR
# 501 - NOT_IMPLEMENTED
# 502 - BAD_GATEWAY
# 503 - SERVICE_UNAVAILABLE
# 504 - GATEWAY_TIMEOUT
# 505 - HTTP_VERSION_NOT_SUPPORTED
# 507 - INSUFFICIENT_STORAGE
# 511 - NETWORK_AUTHENTICATION_REQUIRED

class TestForms(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='karton', email='karton@box.pl', password='top_secret')
        # self.meme = Meme.objects.create(
        #     description='Paweł najlepszy!',
        #     image=Image.open("paweljumper.jpg"),
        #     author='karton'
        # )

    def tearDown(self):
        self.client = None
        self.factory = None
        self.user = None
        self.meme = None

    def test_add_meme_user(self):
        # Create an instance of a GET request.
        request = self.factory.post('add/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user
        request.POST = {"description": "Pan Pawel Skacze",
                        "author": "jumper"}
        request.FILES = {"paweljumper": Image.open("paweljumper.jpg")}

        # Test my_view() as if it were deployed at /customer/details
        response = meme_add(request)
        self.assertEqual(response.status_code, 201)

    # def test_add_meme_anonymous(self):
    #     # Create an instance of a GET request.
    #     request = self.factory.post('add/')
    #
    #     # Or you can simulate an anonymous user by setting request.user to
    #     # an AnonymousUser instance.
    #     request.user = AnonymousUser()
    #
    #     # Test my_view() as if it were deployed at /customer/details
    #     response = meme_add(request)
    #
    #     self.assertEqual(response.status_code, 403)
