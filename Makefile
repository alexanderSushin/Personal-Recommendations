.PHONY: run new-migration help
run: ## Run the project
	docker-compose -f docker-compose.local.yaml up --build

new-migration: ## Create new migration
	migrate create -ext sql -dir migrations -seq migration

help: ## Display this help screen
	grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

 