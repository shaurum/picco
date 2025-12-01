<style>
.zoom-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 95vw;
    max-height: 95vh;
    width: fit-content;
    height: fit-content;
    z-index: 10000;
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25);
    cursor: zoom-out;
    padding: 20px;
    box-sizing: border-box;
    display: none;
    border: 1px solid #e0e0e0;
}

.zoom-modal.active {
    display: flex;
    align-items: center;
    justify-content: center;
}

.zoom-modal img {
    max-width: calc(100vw - 60px);   /* с учётом padding и border */
    max-height: calc(100vh - 60px);
    height: auto;
    width: auto;
    object-fit: contain;
    border-radius: 4px;
}

.zoom-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    z-index: 9999;
    display: none;
}

.zoom-overlay.active {
    display: block;
}

.zoom-trigger {
    cursor: zoom-in;
    transition: transform 0.2s ease;
    display: block;
    margin: 0 auto;
}

.zoom-trigger:hover {
    transform: none;
}

.close-btn {
    position: absolute;
    top: 15px;
    right: 20px;
    background: none;
    border: none;
    font-size: 28px;
    color: #666;
    cursor: pointer;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    z-index: 10001;
}

.close-btn:hover {
    background: #f5f5f5;
    color: #333;
}
</style>

<script>
function openZoomModal(src, alt) {
    // Создаем элементы, если они еще не существуют
    let overlay = document.querySelector('.zoom-overlay');
    let modal = document.querySelector('.zoom-modal');
    
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.className = 'zoom-overlay';
        document.body.appendChild(overlay);
    }
    
    if (!modal) {
        modal = document.createElement('div');
        modal.className = 'zoom-modal';
        
        const closeBtn = document.createElement('button');
        closeBtn.className = 'close-btn';
        closeBtn.innerHTML = '×';
        closeBtn.onclick = closeZoomModal;
        
        const img = document.createElement('img');
        img.id = 'zoomed-image';
        // ДОБАВЛЕНО: Закрытие по клику на саму картинку
        img.onclick = closeZoomModal;
        
        modal.appendChild(closeBtn);
        modal.appendChild(img);
        document.body.appendChild(modal);
        
        // Закрытие по клику на overlay
        overlay.onclick = closeZoomModal;
        // Предотвращаем закрытие при клике на само изображение
        modal.onclick = function(e) {
            e.stopPropagation();
        };
    }
    
    // Устанавливаем изображение
    const zoomedImg = document.getElementById('zoomed-image');
    zoomedImg.src = src;
    zoomedImg.alt = alt;
    
    // Показываем модальное окно и overlay
    overlay.classList.add('active');
    modal.classList.add('active');
    
    // Закрытие по ESC
    document.addEventListener('keydown', handleEscKey);
}

function closeZoomModal() {
    const overlay = document.querySelector('.zoom-overlay');
    const modal = document.querySelector('.zoom-modal');
    
    if (overlay) overlay.classList.remove('active');
    if (modal) modal.classList.remove('active');
    
    document.removeEventListener('keydown', handleEscKey);
}

function handleEscKey(e) {
    if (e.key === 'Escape') {
        closeZoomModal();
    }
}
</script>

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
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

В открывшемся окне нажмите **Установить**, выберете скаченный таргет файл, в нашем случае **СА ПЛК**

<div style="text-align: center;">
    <img src="setup_preparation/C_1.2.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>


В появившемся окне установите галочку **Не подписанные и самоподписанные пакеты** для
подтверждения установки пакета без цифровой подписи и нажмите **ОК**.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.3.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

После этого начнется установка пакета таргет-файла.

В следующем окне ознакомьтесь с текстом лицензионного соглашения, выберите пункт **I have read, understand, and accept the license agreement displayed above** и нажмите **Next**.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.4.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Далее тип настройки. Выберите пункт **Typical setup** и нажмите **Next**.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.5.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Завершите настройку.

<div style="text-align: center;">
    <img src="setup_preparation/C_1.7.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Для создания нового проекта необходимо выбрать пункт **Новый проект..**. Если же вы хотите открыть существующий проект – то можно сделать это с помощью команды **Открыть проект**.

После этого откроется окно создания проектов. Выберите **Стандартный проект**.

В нижней части окна выберите имя файла проекта и директорию, в которой он будет сохранен, после чего нажмите **ОK**.


<div style="text-align: center;">
    <img src="setup_preparation/C_1.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

В следующем окне отобразится список артефактов, которые будут созданы для нового проекта.

Проверьте и, при необходимости, измените настройки "Устройство" и "Язык программирования".

Если предложенные по умолчанию параметры верны, нажмите кнопку **OK**.

<div style="text-align: center;">
    <img src="setup_preparation/C_2.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Интерфейс CODESYS выглядит следующим образом:

<div style="text-align: center;">
    <img src="setup_preparation/C_3.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

В дереве проекта левой кнопкой мыши дважды кликните на узел **Device**.

 Затем нажмите **Scan network**. В появившемся списке следует выбрать нужный контроллер (sa[002A]) и установить связь, нажав **ОК**.
 
 В случае успешной установки связи индикаторы шлюза и контроллера загорятся зеленым.

<div style="text-align: center;">
    <img src="setup_preparation/C_4.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Для загрузки проекта нажмите **Логин**, после чего появится окно с предложением создать пользователя контроллера и задать ему логин и пароль. Эти логин и
пароль потребуется вводить при каждом подключении к виртуальному контроллеру.

<div style="text-align: center;">
    <img src="setup_preparation/C_5.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Выполните вход в систему.

<div style="text-align: center;">
    <img src="setup_preparation/C_7.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Для продолжения загрузки создайте приложение "Application", ответив **Да** в появившемся окне.

<div style="text-align: center;">
    <img src="setup_preparation/C_8.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

После выполнения команды **Логин** и  входа в систему, проект загружается в контроллер. Для запуска проекта следует выполните команду **Старт**.

Текущее состояние программы отображается в строке состояния CODESYS, расположенной внизу экрана.

<div style="text-align: center;">
    <img src="setup_preparation/C_9.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Нажмите на кнопку **Отключение**, которая находится справа от кнопки **Логин**, чтобы добавить устройство.

В дереве проекта правой кнопкой мыши кликните на узел **Device**. В появившемся используйте команду **Добавить устройство**.

<div style="text-align: center;">
    <img src="setup_preparation/C_10.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

Выберите **EtherCAT Master** и добавьте устройство. 

<div style="text-align: center;">
    <img src="setup_preparation/C_11.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

В дереве устройств два раза кликните на **EtherCAT Master**. Нжмите **Select...** и выберете **ecat**. Нажмите **ОК**.

<div style="text-align: center;">
    <img src="setup_preparation/C_12.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

В дереве устройств правой кнопкой мыши щелкните на **EtherCAT Master**. Используйте команду **Поиск устройств...**, чтобы автоматически обнаружить подключенные устройства, и добавьте их в проект командой **Копировать все устройства в проект**.

<div style="text-align: center;">
    <img src="setup_preparation/C_13.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>


Для того чтобы проверить корректность настройки, в дереве устройств 2 раза кликните на **PLC_PRG**. В открывшейся вкладке пропишите код.

!!! note ""
    Приведенный код предназначен для управления [Модулем дискретных выходов DO](DO.md) в рамках рассматриваемого примера

Нажмите **Логин**, а затем **Старт**.

<div style="text-align: center;">
    <img src="setup_preparation/C_15.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

В случае успешной настройки и запуска программы, индикация запущенного приложения в древе проекта должна гореть зеленым.

<div style="text-align: center;">
    <img src="setup_preparation/C_16.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>