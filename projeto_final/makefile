up:
	docker compose up --build -d

down:
	docker compose down

clean:
	docker compose down
	docker system prune -f

test-get:
	curl -k https://localhost/items

test-post:
	curl -k -X POST https://localhost/items -H 'Content-Type: application/json' -d '{"name": "NovoItem"}'

test-put:
	curl -k -X PUT https://localhost/items/0 -H 'Content-Type: application/json' -d '{"name": "ItemAlterado"}'

test-delete:
	curl -k -X DELETE https://localhost/items/0