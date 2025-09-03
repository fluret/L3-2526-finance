import tempfile, os

with tempfile.TemporaryDirectory() as tmpdir:
    print('Created temporary directory ', tmpdir)
    print(os.path.exists(tmpdir))

print(tmpdir)
print(os.path.exists(tmpdir))