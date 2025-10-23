# Работа прибора с CODESYS V3.5

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

4. Установка завершена. Для запуска программы откройте файл CODESYS 3.5 SP21 (64 Bit) → Контроллер → СА.

!!! note "Примечание"
    Файл программы рекомендуется открывать от имени администратора

<ol start="5">
<li>После запуска CODESYS нажмите на кнопку "Новый проект...". После чего появится окно, в котором выберите "Стандартный проект" и место его расположения. Нажмите кнопку "ок".</li>
</ol>

![Image title](setup_preparation/C_2.png){ .fullscreen-image width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

<style>
.fullscreen-image {
    cursor: zoom-in;
}

.fullscreen-image.fullscreen-active {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    z-index: 9999 !important;
    background: rgba(0, 0, 0, 0.95) !important;
    object-fit: contain !important;
    cursor: zoom-out !important;
    padding: 20px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
}
</style>

<script>
document.querySelectorAll('.fullscreen-image').forEach(img => {
    img.addEventListener('click', function() {
        if (this.classList.contains('fullscreen-active')) {
            this.classList.remove('fullscreen-active');
            document.body.style.overflow = '';
        } else {
            this.classList.add('fullscreen-active');
            document.body.style.overflow = 'hidden';
        }
    });
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const fullscreenImages = document.querySelectorAll('.fullscreen-active');
        fullscreenImages.forEach(img => {
            img.classList.remove('fullscreen-active');
            document.body.style.overflow = '';
        });
    }
});
</script>

<ol start="6">
<li>В следующем окне Вы увидите список объектов, которые будут сосзданы для нового проекта. Нажмите кнопку "ок".</li>
</ol>

![Image title](setup_preparation/C_3.png){ .fullscreen-image width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

<style>
.fullscreen-image {
    cursor: zoom-in;
}

.fullscreen-image.fullscreen-active {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    z-index: 9999 !important;
    background: rgba(0, 0, 0, 0.95) !important;
    object-fit: contain !important;
    cursor: zoom-out !important;
    padding: 20px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
}
</style>

<script>
document.querySelectorAll('.fullscreen-image').forEach(img => {
    img.addEventListener('click', function() {
        if (this.classList.contains('fullscreen-active')) {
            this.classList.remove('fullscreen-active');
            document.body.style.overflow = '';
        } else {
            this.classList.add('fullscreen-active');
            document.body.style.overflow = 'hidden';
        }
    });
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const fullscreenImages = document.querySelectorAll('.fullscreen-active');
        fullscreenImages.forEach(img => {
            img.classList.remove('fullscreen-active');
            document.body.style.overflow = '';
        });
    }
});
</script>