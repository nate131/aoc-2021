This days code is a joke [posed on reddit](https://www.reddit.com/r/adventofcode/comments/r77mkv/these_problems_are_harder_than_i_remembered/) to solve the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).

docker-compose run --rm aoc-app && docker rmi $(docker images --filter=reference="*aoc-app*" -q)
