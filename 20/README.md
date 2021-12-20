docker-compose run --rm aoc-app && docker rmi $(docker images --filter=reference="*aoc-app*" -q)
