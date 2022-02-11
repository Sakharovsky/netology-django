## Процесс установки

## Требования

- OS Ubuntu
- установленный docker

## Команды для запуска

1. С помощью команды git clone устанавливаем репозиторий в отдельную директорию.

2. Создаём образ следующей командой:

```bash
sudo docker build -t dj-stocks .
```

3. Запускаем контейнер следующщей командойЖ

```bash
sudo docker run --name dj-stocks -d -p 8000:8000 dj-stocks
```
Приложение будет запущено в фоновом режиме. Обратиться к нему можно по адресу http://server-ip:8000/, где server-ip является адресом хоста.

## Основные команды управления

Остановка работы контейнера

```bash
sudo docker container stop dj-stocks
```

Возобновление работы контейнера

```bash
sudo docker container start dj-stocks
```

Удаление контейнера и образа

```bash
sudo docker container rm dj-stocks
sudo docker image rm dj-stocks
```
