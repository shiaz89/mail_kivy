# mail_kivy
Создание мобильного приложания для отсылки почты.

Для работы приложения на windows необходимо установить приложение tesseract в папку 'src'. При установке необходимо выбрать языкрврй пакет, в данном случае additioanal language/Russian.

Приложение может отсылать сообщения с адреса shiaz@yandex.ru.
Может разобрать картинку, по умолчанию ищет кирилицу, язык русский.
Сообщение можно исправлять.

#Создание .exe файла
Для создания исполняемого файла используется библиотека `pyinstaller`. После установки пакета, моэно выполнить следующую команду в терминале:
`pyinstaller -F --onefile src/to_exe/main.spec` либо `pyinstaller src/main.py --onefile`, терминал должен вызываться из папки проекта.