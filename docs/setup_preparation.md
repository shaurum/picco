# Подготовка к настройке

Для настройки прибора следуйте следующим пунктам:

1. Соберите модульную группу в соответствии с разделом [Правила сборки](assembly_rules.md).
2. Подайте питание на Модуль ввода питания SPPM по [схеме подключения](SPPM.md#_4) и убедитесь, что индикаторы питания на всех модулях горят зеленым светом.
3. Подключите контроллер к сети Ethernet одним из следующих способов:

    **Способ 1: Прямое подключение к ПК**

    Соедините сетевой кабель портом Eth0 на основном модуле и сетевым портом вашего компьютера.

    Настройте сетевой адрес ПК:

    - Перейдите в настройки компьютера, в раздел «Сеть и Интернет».
    - Откройте «Свойства» сетевого подключения.
    - В пункте «Назначение IP» выберите ручной метод настройки и активируйте переключатель IPv4.
    - В открывшейся форме задайте следующие параметры:

    !!! note "Примечание"
        IP-адрес задается следующим образом: `192.168.1.Х`, где `Х` — любое число от 2 до 254, кроме 42.

    <div style="text-align: center;">
        <img src="setup_preparation/IP.webp" 
            alt="Image title" 
            width="280" 
            style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;"
            class="zoom-trigger"
            onclick="openZoomModal(this.src, this.alt)">
    </div>

    <style>
    .zoom-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.7);
        z-index: 9998;
    }

    .zoom-modal {
        display: none;
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 9999;
        max-width: 90%;
        max-height: 90%;
    }

    .zoom-modal img {
        max-width: 100%;
        max-height: 90vh;
        background: white;
        padding: 20px;
        border-radius: 8px;
        object-fit: contain;
        cursor: pointer;
    }

    .close-btn {
        position: absolute;
        top: -40px;
        right: -40px;
        background: rgba(0, 0, 0, 0.5);
        color: white;
        border: 2px solid white;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 24px;
        cursor: pointer;
        z-index: 10000;
    }

    .zoom-overlay.active,
    .zoom-modal.active {
        display: block;
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
            // Закрытие по клику на саму картинку
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


    **Способ 2: Подключение через сетевую инфраструктуру**

    Подключите сетевой кабель к порту Eth1 или Eth2 контроллера, а другой конец - к коммутатору или роутеру в сети с настроенным DHCP-сервером.

4. Для входа в веб-интерфейс управления:

    - Откройте браузер и в адресной строке введите: `http://sa.local`
    - В открывшемся окне авторизации введите: **Логин** - `sa` и **Пароль** - `sa`

5. После первой авторизации смените пароль:

    - Нажмите на иконку профиля в правом верхнем углу.
    - В выпадающем меню выберите пункт «Профиль».

![Image title](setup_preparation/web.webp){ .fullscreen-image width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

   <ul style="margin-left: 45px;">
<li>В открывшемся окне введите текущий пароль, задайте и подтвердите новый пароль, затем нажмите кнопку «Сохранить изменения».</li>
</ul>

![Image title](setup_preparation/password.webp){ .fullscreen-image width="300" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

<style>
.fullscreen-image {
    cursor: zoom-in;
    margin: 20px auto;
}

.fullscreen-image.fullscreen-active {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    z-index: 9999 !important;
    background: rgba(0, 0, 0, 0.7) !important;
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

