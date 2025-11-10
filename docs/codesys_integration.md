# Работа прибора с CODESYS V3.5

Данный раздел предназначен для изучения работы со средой разработки для программируемых логических контроллеров — CODESYS V3.5.

## Установка CODESYS V3.5

Для начала работы с прибором в среде программирования CODESYS V3.5 необходимо:

1. [Скачать архив](setup_preparation/CODESYS%2064%203.5.21.30.zip) для установки CODESYS.
2. Распакуйте архив в отдельную папку и запустите установщика с названием CODESYS Sandbox Prerequisites 3.5.21.30.

    В появившемся окне нажмите **Next**, чтобы начать установку.

    ![Image title](setup_preparation/install1.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне ознакомьтесь с текстом лицензионного соглашения, выберите пункт **I accept the terms in the license agreement** и нажмите **Next**.

    ![Image title](setup_preparation/install2.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне нажмите **Install** для запуска процесса установки.

    ![Image title](setup_preparation/install3.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Процесс установки занимает от нескольких минут до часа (в зависимости от характеристик ПК). В случае успешного завершения появится следующее окно:  

    ![Image title](setup_preparation/install4.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Нажмите **Finish** для закрытия этого окна.

3. Для удаленного подключения к контроллеру установите [CODESYS Gateway](setup_preparation/CODESYS Gateway 3.5.21.30.exe).

    После запуска появиться стартовое окно установщика. Нажмите **Next**.

    ![Image title](setup_preparation/get_1.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне ознакомьтесь с текстом лицензионного соглашения, выберите пункт I **accept the terms in the license agreement** и нажмите **Next**.

    ![Image title](setup_preparation/get_2.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Далее ознакомтесь с информацией о выпуске, после чего выберите пункт **I have read the information** и нажмите **Next**.

    ![Image title](setup_preparation/get_3.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне выберите директорию, в которую будет установлен CODESYS, и нажмите **Next**.

    ![Image title](setup_preparation/get_4.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Следующим шагом необходимо выбрать режим установки CODESYS. Укажите режим полной установки (Complete), чтобы установить все доступные плагины, и нажмите **Next**.

    ![Image title](setup_preparation/get_5.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне нажмите **Install** для запуска процесса установки.

    ![Image title](setup_preparation/get_6.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    После завершения установки в появившемся окне нажмите **Finish**, чтобы завершить процесс.

    ![Image title](setup_preparation/get_7.webp){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

4. Установка завершена. Для запуска программы откройте файл CODESYS 3.5 SP21 (64 Bit) Контроллер СА.

!!! note "Примечание"
    Файл программы рекомендуется открывать от имени администратора

## Настройка и работа CODESYS V3.5

!!! note ""
    Для лучшего понимания принципов работы в CODESYS в разделе приведен пример создания нового проекта для подключенного контроллера. Пример включает сборку из следующих модулей: [Модуль основной GMB](GMB.md), [Модуль ввода питания SPPM](SPPM.md) и  [Модуль дискретного вывода DO](DO.md).

Перед началом настройки проекта необходимо скачать актуальный [таргет файл](https://saplc.ru/documents/).

Установка пакета производится с помощью утилиты **Менеджер пакетов**.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.1.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

В открывшемся окне нажмите **Установить**, выберете скаченный таргет файл, в нашем случае **СА ПЛК**

<div style="text-align: center;">
    <img src="setup_preparation/C_1.2.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

В появившемся окне установите галочку **Не подписанные и самоподписанные пакеты** для
подтверждения установки пакета без цифровой подписи и нажмите **ОК**.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.3.webp" 
         alt="Image title" 
         width="500" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

После этого начнется установка пакета таргет-файла.

В следующем окне ознакомьтесь с текстом лицензионного соглашения, выберите пункт **I have read, understand, and accept the license agreement displayed above** и нажмите **Next**.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.4.webp" 
         alt="Image title" 
         width="500" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Далее тип настройки. Выберите пункт **Typical setup** и нажмите **Next**.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.5.webp" 
         alt="Image title" 
         width="500" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Завершите настройку.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.7.webp" 
         alt="Image title" 
         width="500" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Для создания нового проекта необходимо выбрать пункт **Новый проект..**. Если же вы хотите открыть существующий проект – то можно сделать это с помощью команды **Открыть проект**.

После этого откроется окно создания проектов. Выберите **Стандартный проект**.

В нижней части окна выберите имя файла проекта и директорию, в которой он будет сохранен, после чего нажмите **ОK**.


<div style="text-align: center;">
    <img src="setup_preparation/С_1.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

В следующем окне отобразится список артефактов, которые будут созданы для нового проекта.

Проверьте и, при необходимости, измените настройки "Устройство" и "Язык программирования".

Если предложенные по умолчанию параметры верны, нажмите кнопку **OK**.

<div style="text-align: center;">
    <img src="setup_preparation/C_2.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Интерфейс CODESYS выглядит следующим образом:

<div style="text-align: center;">
    <img src="setup_preparation/C_3.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

В дереве проекта левой кнопкой мыши дважды кликните на узел **Device**.

 Затем нажмите **Scan network**. В появившемся списке следует выбрать нужный контроллер (sa[002A]) и установить связь, нажав **ОК**.
 
 В случае успешной установки связи индикаторы шлюза и контроллера загорятся зеленым.

<div style="text-align: center;">
    <img src="setup_preparation/C_4.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Для загрузки проекта нажмите **Логин**, после чего появится окно с предложением создать пользователя контроллера и задать ему логин и пароль. Эти логин и
пароль потребуется вводить при каждом подключении к виртуальному контроллеру.

<div style="text-align: center;">
    <img src="setup_preparation/C_5.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Выполните вход в систему.

<div style="text-align: center;">
    <img src="setup_preparation/C_7.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Для продолжения загрузки создайте приложение "Application", ответив **Да** в появившемся окне.

<div style="text-align: center;">
    <img src="setup_preparation/C_8.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

После выполнения команды **Логин** и  входа в систему, проект загружается в контроллер. Для запуска проекта следует выполните команду **Старт**.

Текущее состояние программы отображается в строке состояния CODESYS, расположенной внизу экрана.

<div style="text-align: center;">
    <img src="setup_preparation/C_9.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Нажмите на кнопку **Отключение**, которая находится справа от кнопки **Логин**, чтобы добавить устройство.

В дереве проекта правой кнопкой мыши кликните на узел **Device**. В появившемся используйте команду **Добавить устройство**.

<div style="text-align: center;">
    <img src="setup_preparation/C_10.webp" 
         alt="Image title" 
         width="500" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

Выберите **EtherCAT Master** и добавьте устройство. 

<div style="text-align: center;">
    <img src="setup_preparation/C_11.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

В дереве устройств два раза кликните на **EtherCAT Master**. Нжмите **Select...** и выберете **ecat**. Нажмите **ОК**.

<div style="text-align: center;">
    <img src="setup_preparation/C_12.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

В дереве устройств правой кнопкой мыши щелкните на **EtherCAT Master**. Используйте команду **Поиск устройств...**, чтобы автоматически обнаружить подключенные устройства, и добавьте их в проект командой **Копировать все устройства в проект**.

<div style="text-align: center;">
    <img src="setup_preparation/C_13.webp" 
         alt="Image title" 
         width="500" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>


Для того чтобы проверить корректность настройки, в дереве устройств 2 раза кликните на **PLC_PRG**. В открывшейся вкладке пропишите код.

!!! note ""
    Приведенный код предназначен для управления [Модулем дискретных выходов DO](DO.md) в рамках рассматриваемого примера

Нажмите **Логин**, а затем **Старт**.

<div style="text-align: center;">
    <img src="setup_preparation/C_15.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>

В случае успешной настройки и запуска программы, индикация запущенного приложения в древе проекта должна гореть зеленым.

<div style="text-align: center;">
    <img src="setup_preparation/C_16.webp" 
         alt="Image title" 
         width="700" 
         style="cursor: zoom-in; display: block; margin: 0 auto;" 
         onclick="this.classList.toggle('fullscreen')"
         class="fullscreen-image">
</div>

<style>
.fullscreen-image.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.95);
    object-fit: contain;
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
}
</style>