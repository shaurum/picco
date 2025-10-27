# Работа прибора с CODESYS V3.5

## Установка CODESYS V3.5

Для начала работы с прибором в среде программирования CODESYS V3.5 необходимо:

1. [Скачать архив](setup_preparation/CODESYS%2064%203.5.21.30.zip) для установки CODESYS.
2. Распакуйте архив в отдельную папку и запустите установщика с названием CODESYS Sandbox Prerequisites 3.5.21.30.

    В появившемся окне нажмите кнопку **Next**, чтобы начать установку.

    ![Image title](setup_preparation/install1.jpg){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне ознакомьтесь с текстом лицензионного соглашения, выберите пункт **I accept the terms in the license agreement** и нажмите кнопку **Next**.

    ![Image title](setup_preparation/install2.jpg){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне нажмите кнопку **Install** для запуска процесса установки.

    ![Image title](setup_preparation/install3.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Процесс установки занимает от нескольких минут до часа (в зависимости от характеристик ПК). В случае успешного завершения появится следующее окно:  

    ![Image title](setup_preparation/install4.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Нажмите кнопку **Finish** для закрытия этого окна.

3. Для удаленного подключения к контроллеру установите [CODESYS Gateway](setup_preparation/CODESYS Gateway 3.5.21.30.exe).

    После запуска появиться стартовое окно установщика. Нажмите кнопку **Next**.

    ![Image title](setup_preparation/get_1.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне ознакомьтесь с текстом лицензионного соглашения, выберите пункт I **accept the terms in the license agreement** и нажмите кнопку **Next**:

    ![Image title](setup_preparation/get_2.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Далее ознакомтесь с информацией о выпуске, после чего выберите пункт **I have read the information** и нажмите кнопку **Next**

    ![Image title](setup_preparation/get_3.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне выберите директорию, в которую будет установлен CODESYS, и нажмите кнопку **Next**

    ![Image title](setup_preparation/get_4.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    Следующим шагом необходимо выбрать режим установки CODESYS. Укажите режим полной установки (Complete), чтобы установить все доступные плагины, и нажмите **Next**.

    ![Image title](setup_preparation/get_5.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    В следующем окне нажмите кнопку **Install** для запуска процесса установки.

    ![Image title](setup_preparation/get_6.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

    После завершения установки в появившемся окне нажмите кнопку **Finish**, чтобы завершить процесс.

    ![Image title](setup_preparation/get_7.png){ width="400" style="display: block; margin-left: auto; margin-right: auto;" }

4. Установка завершена. Для запуска программы откройте файл CODESYS 3.5 SP21 (64 Bit) Контроллер СА.

!!! note "Примечание"
    Файл программы рекомендуется открывать от имени администратора

## Настройка и работа CODESYS V3.5

Для создания нового проекта необходимо выбрать пункт **Новый проект..**. Если же вы хотите открыть существующий проект – то можно сделать это с помощью команды **Открыть проект**.

После этого откроется окно создания проектов. Выберите **Стандартный проект**.

В нижней части окна выберите имя файла проекта и директорию, в которой он будет сохранен, после чего нажмите **Ок**.


<div style="text-align: center;">
    <img src="setup_preparation/С_1.png" 
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

В следующем окне вы увидите список объектов, которые будут сосзданы для нового проекта. Нажмите **Ок**.

<div style="text-align: center;">
    <img src="setup_preparation/C_2.png" 
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

Интерфейс CODESYS выглядит следующим образом

<div style="text-align: center;">
    <img src="setup_preparation/C_3.png" 
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
    <img src="setup_preparation/C_4.png" 
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
    <img src="setup_preparation/C_5.png" 
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
    <img src="setup_preparation/C_7.png" 
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
    <img src="setup_preparation/C_8.png" 
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
    <img src="setup_preparation/C_9.png" 
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
    <img src="setup_preparation/C_10.png" 
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
    <img src="setup_preparation/C_11.png" 
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
    <img src="setup_preparation/C_12.png" 
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

В дереве устройств правой кнопкой мыши щелкните на **EtherCAT Master**. Используйте команду **Поиск устройств...**, чтобы автоматически обнаружить подключенные устройства и добавить их в проект командой **Копировать все устройства в проект**.

<div style="text-align: center;">
    <img src="setup_preparation/C_13.png" 
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


Для того чтобы проверить корректность настройки, в дереве устройств 2 раза кликните на **PLC_PRG**. В открывшейся вкладке, для примера, пропишите краткий код.

Нажмите **Логин**, а затем **Старт**.

<div style="text-align: center;">
    <img src="setup_preparation/C_15.png" 
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
    <img src="setup_preparation/C_16.png" 
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