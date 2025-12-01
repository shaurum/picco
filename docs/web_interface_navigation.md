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

# Web-интерфейс
## Настройка интерфейсов

<div style="text-align: center;">
    <img src="setup_preparation/web_2.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>


При переходе в веб-интерфейс на экране отображается раздел "Нстройка сети", где представлены текущие параметры всех сетевых интерфейсов. Каждый интерфейс сопоставлен с физическим портом на основном модуле и имеет кнопку "Настроить" для изменения параметров.  

<div style="text-align: center;">
    <img src="setup_preparation/settings.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>


Для настройки сетевого интерфейса можно выбрать как автоматический режим присвоения сетевых параметров с помощью DHCP, так и вводить их вручную. 

## Системное время

<div style="text-align: center;">
    <img src="setup_preparation/time.webp" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
    </div>


В данном разделе Вы можете настроить системное время устройства: выбрать часовой пояс и включать автоматическую синхронизацию времени через NTP-сервер.

В поле "NTP-серверы" можно указать один или несколько адресов NTP-серверов.

!!! note "Примечание"
      Рекомендуется настроить синхронизацию времени при помощи NTP.
     
После завершения настройки времени сохраните изменения.

## Сброс до заводских настроек

??? example "Разработка"

    На текущий момент данный раздел находится в разработке.

Сброс до заводских настроек осуществляется при помощи скрытой кнопки на [Модуле основном GMB](GMB.md).
