.PHONY: all
all:
	docker build --no-cache --rm --pull -t lukaszimmermann/luigibio:latest .

