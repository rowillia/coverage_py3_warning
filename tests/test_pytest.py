from foobar import foobar
import warnings

def setup():
    warnings.filterwarnings('error', category=DeprecationWarning, module='foobar')

def teardown():
    warnings.filterwarnings('ignore', category=DeprecationWarning)

def test_pytest():
  assert foobar.say_hello('Roy') == 'Hello Roy1'
