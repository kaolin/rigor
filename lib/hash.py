""" Common functions for hashing files """

import hashlib

def sha256_hash(path):
	"""
	Returns a SHA-256 hash of either the contents of the path, or the data passed in if file-like.
	"""
	sha256 = hashlib.sha256()
	file_object = path if hasattr(path, 'read') else open(path, 'rb')
	while True:
		buf = file_object.read(0x100000)
		if not buf:
			break
		sha256.update(buf)
	return sha256.hexdigest()
