Crie e ative o ambiente virtual

Crie e ative o ambiente virtual

python -m venv venv

Ative o ambiente:


.\venv\Scripts\activate

 Instale as dependências
Instale todas as bibliotecas necessárias:


pip install -r requirements.txt



Crie o arquivo .env na raiz do projeto


DB_NAME=agendamento_db
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY= xxxvavvavsh
DEBUG=True



Crie o banco de dados no MySQL
sql



CREATE DATABASE blog_login CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'sua_senha_segura';
GRANT ALL PRIVILEGES ON blog_login.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;



Aplique as migrações


python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser


python manage.py runserver