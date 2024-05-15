# Expense Tracker API

Это простое API приложение на Python с использованием FastAPI для парсинга сообщений о расходах и доходах и записи их в JSON файл.

## Установка и активация нового окружения локально

1. Создайте новое виртуальное окружение с помощью вашего предпочтительного менеджера виртуальных окружений (например, `venv` или `conda`):

    Для `venv`:

    ```bash
    python -m venv myenv
    ```

    Для `conda`:

    ```bash
    conda create --name myenv python=3.9
    ```

    Для `powershell`

    ```powershell
    python -m venv .myenv
    ```

2. Активируйте виртуальное окружение. Например, для `venv` на Linux это может выглядеть так:

    ```bash
    source myenv/bin/activate
    ```

   На Windows:

    ```bash
    myenv\Scripts\activate
    ```

3. Установите зависимости, указанные в файле `requirements.txt`, используя pip:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск приложения локально

Для запуска приложения выполните следующую команду:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```


## Установка и запуск на сервере 

```bash
git clone https://github.com/a0l6g0r8a9l2/Expense-Tracker-API.git
```

```bash
cd Expense-Tracker-API
```

```bash
docker build -t expense-tracker-api-image .
```

```bash
docker run -d --env-file .env --name expense-tracker-api-app -p 80:80 expense-tracker-api-image 
```

```bash
docker ps -a
```

```bash
docker logs {conteiner_id}
```