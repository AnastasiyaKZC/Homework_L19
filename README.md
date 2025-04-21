# Homework_L19 Мобильная автоматизация #1. Разрабатываем автотесты с Browserstack. Станислав Васенков и Яков Крамаренко

- [Ссылка на занятие](https://school.qa.guru/pl/teach/control/lesson/view?id=334954981&editMode=0) 
- [Ссылка на лекцию](https://github.com/qa-guru/knowledge-base/wiki/19.-%D0%9C%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%231.-%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%B0%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC-%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D1%8B-%D1%81-Browserstack)


1. Практика
– Учимся пользоваться инспектором в Browserstack, разрабатываем первые автотесты на Android / iOS с Selene
– Browserstack-API. Забираем логи, видео

2. Теория
– Основы тестирования мобильных приложений


browserstack - сервис удаленного запуска автотестов на всех платформах

Исходники:

- начальный код из урока https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-1-initial

- финальный код из основной части урока (без хелперов для этача видео & Co в Allure отчет) https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-1-pre-final

- финальный код из дополнительной частью урока  (с настройкой отчета Allure и этача видео & Co) https://github.com/yashaka/selene-in-action/tree/py06-lesson-mobile-1-final-with-more-allure-steps-n-attachments

- финальный код из предыдущей версии этого урока для первых потоков на курсе: https://github.com/qa-guru/mobile-tests-13-py/tree/demo-selene-appium-with-browserstack-android


Основные ссылки:

- Страничка «Get Started» на браузерстек (выбирать язык Python): https://app-automate.browserstack.com/dashboard/v2/quick-start/get-started

  - пример использовать не из нее, а с гитхаба по ссылке: https://github.com/browserstack/python-appium-app-browserstack/blob/master/android/browserstack_sample.py

- Дешбоард на браузерстек: https://app-automate.browserstack.com/dashboard/v2

- Инспектор на браузерстек: https://app-live.browserstack.com

- Как загрузить свою версию апки в браузерстек:
https://github.com/qa-guru/mobile-tests-13-py/tree/demo-selene-appium-with-browserstack-android#how-...

- Откуда скачать последнюю версию апки Wikipedia под android? - https://github.com/wikimedia/apps-android-wikipedia/releases

  - чтобы работал тот же тест с этой версией апки, вероятно, придется дописать дополнительную опцию (капабилити): 'appWaitActivity': 'org.wikipedia.*'

- Официальные примеры Selene для запуска на разных платформах: https://github.com/yashaka/selene/tree/master/examples

browserstack - сервис удаленного запуска автотестов на всех платформах