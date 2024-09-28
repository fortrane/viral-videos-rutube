# Генерация виральных клипов

## О проекте
"Генерация виральных клипов" - Создавайте виральные ролики за минуты! Наш AI-сервис автоматически извлекает ключевые моменты из ваших видео и превращает их в короткие, захватывающие клипы, готовые взорвать соцсети! Попробуйте сейчас и сделайте ваш контент популярным!
- Автоматическое извлечение ключевых моментов из видео.
- Создание коротких вертикальных роликов (20 сек – 3 мин).
- Генерация от 2 до 20 уникальных клипов.
- Добавление названий, описаний и хештегов.
- Редактор для кастомизации клипов.
- Аналитика виральности и эффективности с описанием выбора данного фрагмента.
- Управление и кастомизация из веб-интерфейса.

## Минимальные требования сервера для Web части
- CPU: 2 ядра
- ОЗУ: 2 ГБ
- SSD/HDD: 20 ГБ

## Установка
### Зависимости сервера
Установка производится на любом Linux сервере. В качестве примера рассмотрим установку на Ubuntu 20.04.

#### Обновление системы
```bash
sudo apt update
sudo apt upgrade -y
```

#### Установка Nginx
```bash
sudo apt install nginx -y
```

#### Установка PHP и расширений
```bash
sudo apt install php7.4 php7.4-fpm php7.4-mysql php7.4-xml php7.4-mbstring php7.4-curl -y
```

#### Установка MySQL
```bash
sudo apt install mysql-server -y
sudo mysql_secure_installation
```

#### Дополнительные шаги для настройки PHP
```bash
sudo systemctl start php7.4-fpm
sudo systemctl enable php7.4-fpm
```

#### Настройка Nginx для работы с PHP
Создайте или отредактируйте конфигурационный файл в /etc/nginx/sites-available/your_domain с следующим содержимым:
```nginx
server {
    listen 80;
    server_name your_domain.com www.your_domain.com;

    root /var/www/your_domain;
    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.4-fpm.sock;
    }

    location ~ /\.ht {
        deny all;
    }
}

```

#### Перезапуск Nginx

```bash
sudo nginx -t
sudo systemctl restart nginx
```
### Установка Web части
1. Скачайте контент из папок `web` и `database`.
2. Переместите контент папки `web` в корень вашего сайта.
3. Создайте новую базу данных и импортируйте в неё дамп из папки `database`.
4. Откройте файл `src/Custom/Medoo/connect.php` и укажите параметры подключения к базе данных:
    ```
    $pdo = new PDO('mysql:dbname=DB_NAME;host=localhost', 'DB_USR', 'DB_PWD');
    ```
5. Откройте файл `src/Functions/external.class.php` и укажите URL вашего ML API, а так же секретный ключ для доступа к эндпоинтам:
    ```
    const SERVER_LINK = "http://127.0.0.1:8001/";
    const SECRET_TOKEN = "SECRET_KEY";
    ```

6. Откройте файл `src/Api/v1.external.php` и продублируйте секретный ключ для доступа к эндпоинтам:
    ```
    $secretKey = "SECRET_KEY";
    ```   

## Запуск
После установки и настройки всех компонентов, откройте сайт из корня сервера для доступа к Web части. Вы можете загрузить .mp4 файл весом до 400 МБ. После загрузки требуется подождать какое то время, потому что следом начинается скачивание видео на ML сервер. На странице с видео написана инструкция по эксплуатации интерфейса
