from decouple import config

db = {
	'dbname': config('dbname'),
	'user': config('dbuser'),
	'password': config('dbpasswd'),
	'host': config('dbhost'),
	'port': ''
}
