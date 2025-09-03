try:
    # Non-existent module
    import baz
except ImportError:
    print('Module not found')