try:
    # Existing module, but non-existent object
    from mod import baz
except ImportError:
    print('Object not found in module')