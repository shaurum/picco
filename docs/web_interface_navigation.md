# Web-интерфейс
## Настройка интерфейсов

![Image title](setup_preparation/web_2.png){ .fullscreen-image width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

<style>
.fullscreen-image {
    cursor: zoom-in;
    transition: transform 0.2s;
}

.fullscreen-image:active {
    position: fixed;
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
    transform: none !important;
}
</style>


При переходе в веб-интерфейс на экране отображается раздел "Нстройка сети", где представлены текущие параметры всех сетевых интерфейсов. Каждый интерфейс сопоставлен с физическим портом на основном модуле и имеет кнопку "Настроить" для изменения параметров.  

![Image title](setup_preparation/settings.png){ .fullscreen-image width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

<style>
.fullscreen-image {
    cursor: zoom-in;
    transition: transform 0.2s;
}

.fullscreen-image:active {
    position: fixed;
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
    transform: none !important;
}
</style>

Для настройки сетевого интерфейса можно выбрать как автоматический режим присвоения сетевых параметров с помощью DHCP, так и вводить их вручную. 

## Системное время

![Image title](setup_preparation/time.png){ .fullscreen-image width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

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
            // Выход из полноэкранного режима
            this.classList.remove('fullscreen-active');
            document.body.style.overflow = '';
        } else {
            // Вход в полноэкранный режим
            this.classList.add('fullscreen-active');
            document.body.style.overflow = 'hidden';
        }
    });
});

// Закрытие по ESC
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

В данном разделе Вы можете настроить системное время устройства: выбрать часовой пояс и включать автоматическую синхронизацию времени через NTP-сервер.

В поле "NTP-серверы" можно указать один или несколько адресов NTP-серверов.

!!! note "Примечание"
      Рекомендуется включить NTP-синхронизацию, чтобы обеспечить точность времени.
     
После завершения настройки времени сохраните изменения.

## Сброс до заводских настроек

??? example "Разработка"

    На текущий момент данный раздел находится в разработке.

Сброс до заводских настроек осуществляется при помощи скрытой кнопки на [Модуле основном GMB](GMB.md).
