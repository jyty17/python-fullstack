import hashlib

def HandleFileUpload(file, filename, user_id):
	new_filename = f'{user_id}_{filename}'
	hashed_filename=hashlib.sha224(new_filename.encode()).hexdigest()
	with open(f'uploads/{hashed_filename}.py', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
