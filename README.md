# aoc-2021
Answers for [Advent of Code 2021](https://adventofcode.com/2021). Each folder contains a Dockerfile and docker-compose.yml in order to execute the script in a docker container.

The command in each README for day folders will compose the container, run the container once and then delete the container and image. the deletion of the image searches for any images that contain "aoc-app" in them.