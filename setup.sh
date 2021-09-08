docker-compose exec backend python3 manage.py migrate \
&& docker-compose exec backend python3 manage.py new_user \
&& docker exec -ti poke-api-backend python3 manage.py collectstatic --noinput