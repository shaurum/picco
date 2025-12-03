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
    <img src="setup_preparation\IP.webp" 
         alt="Image title" 
         width="300" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>


    **Способ 2: Подключение через сетевую инфраструктуру**

    Подключите сетевой кабель к порту Eth1 или Eth2 контроллера, а другой конец - к коммутатору или роутеру в сети с настроенным DHCP-сервером.

4. Для входа в веб-интерфейс управления:

    - Откройте браузер и в адресной строке введите: `http://sa.local`
    - В открывшемся окне авторизации введите: **Логин** - `sa` и **Пароль** - `sa`

5. После первой авторизации смените пароль:

    - Нажмите на иконку профиля в правом верхнем углу.
    - В выпадающем меню выберите пункт «Профиль».

    <div style="text-align: center;">
    <img src="setup_preparation/web.webp" 
         alt="Image title" 
         width="600" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>

   <ul style="margin-left: 45px;">
<li>В открывшемся окне введите текущий пароль, задайте и подтвердите новый пароль, затем нажмите кнопку «Сохранить изменения».</li>
</ul>

<div style="text-align: center;">
    <img src="setup_preparation/password.webp" 
         alt="Image title" 
         width="400" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>


