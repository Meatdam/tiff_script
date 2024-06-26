# Скрипт по добавлению изображений в один файл .tiff
В данном скрипте имеется:
_____
### Файл config.py
Файл отвечающий за кореектные относительные пути до папок в котором лежат файлы (изображения)
_____
### Файл utils.py
В данном файле находятся две функции:
- find_files: Функция генератор отвечающая за сбор всех файлов (изображений) из вложенных папок
- stich_tile: Функция отвечающая за добавление всех изображений в один файл с расширением .tiff
_____
## Логика работы скрипта:
Первым делом нам необходимо определиться с какой папкой мы хотели бы работать. Прописываем путь до папки в файле 'config.py' в константе 'PATH_IMG', где 'PATH' это константа от корня проекта (Обязательно указывать)<br>
После чего необходимо указать в константу 'FILE' путь до папки куда будут складываться все изображение в одну папку. 
После чего мы заходим в файл 'utils.py' и в функции stich_tile (в конструкции `if __name__ == '__main__'`) мы можем выбрать, сколько колонок мы хотим  видеть в файле и сколько изображений в одной колонки. <br>
_____
# Важно: 
если изображений будет меньше, чем два числа умноженых друг на друга, которые вы вводите то срайзица ошибка `недостаточно изображений в пути_к_файлу !`
_____
В функции 'find_files' можно указать формат изображений которые мы хотим забрать. Лучше указвать `'*/.j'` тогда все файлы имеющие формат начинающий на `j` будут добавлены
_____

Для запуска проекта у себя локально необходимо сделать: 
```
git@github.com:Meatdam/tiff_script.git
```
Установить виртуальное окружение `venv`
```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```
Активировать виртуальное окружение
```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```
И установить файл с зависимостями
```
pip install -r requirements.txt
```

Автор проекта:<br>
[Кузькин Илья](https://github.com/Meatdam)
