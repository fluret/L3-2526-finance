from tempfile import TemporaryFile

fp = TemporaryFile('w+t')
fp.write('Hello universe!')

fp.seek(0)
data = fp.read()

fp.close()