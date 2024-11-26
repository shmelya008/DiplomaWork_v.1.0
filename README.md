# DiplomaWork_v.1.0
<a id="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/shmelya008/DiplomaWork_v.1.0/blob/master/ReadmeImages/IMG_6837.PNG">
    <img src="ReadmeImages/IMG_6837.PNG" alt="Logo" width="300" height="200">
  </a>

<h3 align="center">Hair Aprel Studio</h3>

  <p align="center">
    Сайт салона красоты Hair Aprel
    <br />
    <a href="https://github.com/shmelya008/DiplomaWork_v.1.0.git"><strong>Explore the docs »</strong></a>
    <br />
<!--     <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p> -->
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Оглавление</summary>
  <ol>
    <li>
      <a href="#about-the-project">О проекте</a>
      <ul>
        <li><a href="#built-with">Создано с поддержкой</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Начало работы</a>
      <ul>
        <li><a href="#installation">Установка</a></li>
      </ul>
    </li>
    <li><a href="#usage">Использование</a></li>
    <li><a href="#roadmap">Дорожная карта</a></li>
<!--     <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Контакты</a></li>
<!--     <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## О проекте

[![Product Name Screen Shot][product-screenshot]](ScreenSite.PNG)

Проект создан для моей подруги Кати Апрельской, блогера и владелицы студии красоты "Hair Aprel"
Этот мини сайт должен помочь ей расширить аудиторию клиентов студии, и помочь в администрировании бизнеса.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Создано с поддержкой

* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Начало работы

Переходим в директорию HAProject

Создаем виртуальное окружение через командную строку python -m venv venv

Активируем виртуальное окружение:

Для Linux/Mac: source venv/bin/activate
Для Windows: venv/Scripts/activate
Выполняем команду pip install -r requirements.txt

Выполняем миграции python manage.py migrate

Запускаем приложение python manage.py runserver


### Установка доплнительных ресурсов

Для полноценной работы приложения необходимо установить и настроить дополнительные ресурсы: 
1. Чат бот Телеграм
2. Публичный канал Телеграм.
   
#### Создание бота в телеграм
Нам нужно создать бота в телеграм. Для этого мы ищем по имени BotFather бота @BotFather в телеграм

<img src="ReadmeImages/BotFather.png" width="600" height="200">

Заходим в этот бот и создаем нашего бота. Для этого вы должны ввести команду /newbot . Дальше вам предложать выбрать имя для вашего бота , после того как вы введете имя будет предложено выбрать username для вашего бота , который должен быть уникальным и окончиваться на _bot.

<img src="ReadmeImages/BotFather2.png" width="600" height="500">

### Создание нового канала в телеграм
Создать канал очень легко. В телеграме кликаем по ссылке "Создать канал" и вводим название канала и описание

<img src="ReadmeImages/tgchannel1.png" width="600" height="400">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Использование

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Контакты

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Благодарности

Благодарю всех преподавателей, кураторов университета Urban и всех, кто помогал мне в моей работе.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: ReadmeImages/ScreenSite.PNG

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

