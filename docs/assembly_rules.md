# Сборка контроллера
Контроллер представляет собой модульную систему, состоящую из **модулей расширения**, работающих с сигналами, и **специальных модулей расширения**, обеспечивающих работу контроллера в самых гибких конфигурациях.
Для правильной и бесперебойной работы контроллера необходимо выполнение ряда требований при его сборке. К этим требованиям относятся:

- правильная последовательность модулей в группе
- организация питания в группе
- оранизация подключения групп

!!! success "Рекомендация"
    Правильная сборка позволяет обеспечить работу таких функций как [горячая замена модулей]() и [резервирование питания контроллера]()

## Последовательность модулей в группе

<script>
// Улучшенный парсер с правильными отступами для вложенных списков
const mdParser = new (function() {
    this.parse = function(text) {
        let lines = text.split('\n');
        let result = [];
        let inList = false;
        
        for (let i = 0; i < lines.length; i++) {
            let line = lines[i];
            let trimmed = line.trim();
            
            if (trimmed.startsWith('- ')) {
                // Определяем уровень вложенности по количеству пробелов в начале
                let indent = line.match(/^\s*/)[0].length;
                let content = trimmed.substring(2);
                
                if (!inList) {
                    result.push('<ul>');
                    inList = true;
                }
                
                // Добавляем отступ в зависимости от уровня
                let margin = indent * 8; // 8px на каждый уровень отступа
                result.push(`<li style="margin-left: ${margin}px;">${this.parseInline(content)}</li>`);
            }
            else if (trimmed) {
                if (inList) {
                    result.push('</ul>');
                    inList = false;
                }
                
                // Если строка начинается с ** и заканчивается ** - это заголовок
                if (trimmed.startsWith('**') && trimmed.endsWith('**')) {
                    let title = trimmed.slice(2, -2); // Убираем **
                    result.push(`<div class="popup-title">${title}</div>`);
                } else {
                    result.push(this.parseInline(trimmed) + '<br>');
                }
            }
            else {
                if (inList) {
                    result.push('</ul>');
                    inList = false;
                }
                result.push('<br>');
            }
        }
        
        if (inList) result.push('</ul>');
        
        return result.join('');
    };
    
    this.parseInline = function(text) {
        return text
            .replace(/\[([^\]]+)\]\(([^)]+)\.md\)/g, '<a href="$2.html">$1</a>')
            .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
            .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
            .replace(/\*([^*]+)\*/g, '<em>$1</em>')
            .replace(/`([^`]+)`/g, '<code>$1</code>');
    };
})();

document.addEventListener('DOMContentLoaded', function() {
    // Сначала преобразуем Markdown в попапах
    document.querySelectorAll('.hover-popup[data-markdown]').forEach(popup => {
        const markdown = popup.getAttribute('data-markdown');
        popup.innerHTML = '<div class="popup-arrow"></div>' + mdParser.parse(markdown);
    });

    // Затем инициализируем попапы
    const hoverElements = document.querySelectorAll('[data-hover]');
    
    hoverElements.forEach(function(hoverElement) {
        const popupId = hoverElement.getAttribute('data-hover');
        const popup = document.getElementById(popupId);
        
        if (!popup) return;
        
        let isOverPopup = false;
        
        function updatePopupPosition() {
            const rect = hoverElement.getBoundingClientRect();
            const popupHeight = popup.offsetHeight;
            const viewportHeight = window.innerHeight;
            
            const spaceAbove = rect.top;
            const spaceBelow = viewportHeight - rect.bottom;
            
            const mainContent = document.querySelector('.md-main__inner') || document.querySelector('.md-content');
            let contentRect;
            let leftBoundary = 20;
            let rightBoundary = window.innerWidth - 20;
            
            if (mainContent) {
                contentRect = mainContent.getBoundingClientRect();
                leftBoundary = contentRect.left + 10;
                rightBoundary = contentRect.right - 10;
            }
            
            const contentWidth = rightBoundary - leftBoundary;
            const maxWidth = Math.min(contentWidth * 0.9, 600);
            
            popup.style.width = 'auto';
            popup.style.maxWidth = maxWidth + 'px';
            
            const popupWidth = popup.offsetWidth;
            let leftPosition = rect.left + window.pageXOffset + (rect.width / 2) - (popupWidth / 2);
            
            leftPosition = Math.max(leftBoundary + window.pageXOffset, 
                                   Math.min(leftPosition, 
                                           rightBoundary + window.pageXOffset - popupWidth));
            
            let topPosition, arrowPosition;
            
            if (spaceBelow >= popupHeight + 30 || spaceBelow >= spaceAbove) {
                topPosition = rect.bottom + window.pageYOffset + 15;
                arrowPosition = 'top';
            } else {
                topPosition = rect.top + window.pageYOffset - popupHeight - 15;
                arrowPosition = 'bottom';
            }
            
            popup.style.left = leftPosition + 'px';
            popup.style.top = topPosition + 'px';
            popup.setAttribute('data-arrow', arrowPosition);
            
            const arrow = popup.querySelector('.popup-arrow');
            if (arrow) {
                const arrowOffset = (rect.left + window.pageXOffset + rect.width / 2) - leftPosition;
                const limitedOffset = Math.max(20, Math.min(popupWidth - 20, arrowOffset));
                arrow.style.left = limitedOffset + 'px';
            }
        }
        
        hoverElement.addEventListener('mouseenter', function() {
            document.querySelectorAll('.hover-popup').forEach(p => p.style.display = 'none');
            popup.style.display = 'block';
            updatePopupPosition();
        });
        
        hoverElement.addEventListener('mouseleave', function() {
            setTimeout(() => {
                if (!isOverPopup) {
                    popup.style.display = 'none';
                }
            }, 100);
        });
        
        popup.addEventListener('mouseenter', function() {
            isOverPopup = true;
        });
        
        popup.addEventListener('mouseleave', function() {
            isOverPopup = false;
            setTimeout(() => {
                popup.style.display = 'none';
            }, 100);
        });
        
        window.addEventListener('scroll', function() {
            if (popup.style.display === 'block') {
                updatePopupPosition();
            }
        });
        
        window.addEventListener('resize', function() {
            if (popup.style.display === 'block') {
                updatePopupPosition();
            }
        });
    });
});
</script>

<style>
/* Стили для заголовков и текста */
.hover-popup .popup-title {
    font-size: 1.1em; /* Чуть больше */
    font-weight: 600;
    color: #555; /* Чуть темнее серый */
    margin: 0 0 12px 0;
    line-height: 1.3;
}

.hover-popup strong {
    color: #000; /* Черный для жирного текста */
    font-weight: 700;
}

/* Стили для правильных отступов вложенных списков */
.hover-popup ul {
    margin: 8px 0;
    padding-left: 0; /* Убираем стандартный отступ */
    list-style: none; /* Убираем стандартные маркеры */
}

.hover-popup li {
    margin: 4px 0;
    position: relative;
    padding-left: 16px; /* Отступ для маркера */
}

.hover-popup li:before {
    content: "•";
    position: absolute;
    left: 0;
    color: #666;
}

/* Остальные стили */
.hover-trigger {
    color: #0066cc;
    border-bottom: 1px dashed #0066cc;
    cursor: pointer;
    padding: 0 2px;
}

.hover-trigger:hover {
    background-color: #f0f8ff;
}

.hover-popup {
    display: none;
    position: absolute;
    background: white;
    border: 1px solid #adadad;
    border-radius: 4px;
    padding: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    z-index: 10000;
    box-sizing: border-box;
    white-space: normal;
    font-size: 0.9em;
    line-height: 1.5;
    color: #333; /* Стандартный цвет текста */
}

.hover-popup a {
    color: var(--md-typeset-a-color, #0066cc);
    text-decoration: none;
}

.hover-popup a:hover {
    text-decoration: underline;
}

.hover-popup em {
    font-style: italic;
    color: #333;
}

.hover-popup code {
    background: #f5f5f5;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
    font-size: 0.9em;
    color: #333;
}

.popup-arrow {
    position: absolute;
    width: 16px;
    height: 8px;
    left: 50%;
    transform: translateX(-50%);
}

.hover-popup[data-arrow="top"] .popup-arrow {
    top: -8px;
}

.hover-popup[data-arrow="top"] .popup-arrow::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 8px solid white;
}

.hover-popup[data-arrow="top"] .popup-arrow::after {
    content: '';
    position: absolute;
    top: -1px;
    left: 0;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 8px solid #adadad;
    z-index: -1;
}

.hover-popup[data-arrow="bottom"] .popup-arrow {
    bottom: -8px;
}

.hover-popup[data-arrow="bottom"] .popup-arrow::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 8px solid white;
}

.hover-popup[data-arrow="bottom"] .popup-arrow::after {
    content: '';
    position: absolute;
    top: 1px;
    left: 0;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 8px solid #adadad;
    z-index: -1;
}

[data-md-color-scheme="slate"] .hover-popup {
    background: var(--md-default-bg-color);
    border-color: #5d5d5d;
    color: var(--md-default-fg-color);
}

[data-md-color-scheme="slate"] .popup-arrow::before {
    border-bottom-color: var(--md-default-bg-color);
    border-top-color: var(--md-default-bg-color);
}

[data-md-color-scheme="slate"] .popup-arrow::after {
    border-bottom-color: #5d5d5d;
    border-top-color: #5d5d5d;
}
</style>

Сборка группы, включающей в себя <span class="hover-trigger" data-hover="popup1">основной модуль</span>, должна начинаться с установки [Модуля ввода питания SPPM](SPPM.md). Вторым модулем всегда устанавливается <span class="hover-trigger" data-hover="popup1">основной модуль</span>, после чего устанавливаются модули расширения.

<div id="popup1" class="hover-popup" data-markdown="**Основные модули**
*Основные модули -  это центральные устройства, которые содержат процессор, память и интерфейсы для управления подключенными устройствами по заданной программе*

На настоящий момент представлено 2 модуля **основных**
- [Модуль основной GMB](GMB.md), обладающий следующими ключевыми характеристиками:
  - Процессор RiP
  - 256MB памяти
- [Модуль основной GMR](GMR.md)
  - **находится в разработке**
  - планируемый релиз: Q4 2024">
</div>

<style>
.zoom-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 90vw;
    height: 90vh;
    max-width: 1200px;
    max-height: 800px;
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
    max-width: 100%;
    max-height: 100%;
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

/* Убираем transform: scale при наведении */
.zoom-trigger:hover {
    transform: none; /* Убираем масштабирование */
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
}

.close-btn:hover {
    background: #f5f5f5;
    color: #333;
}
</style>

<div style="text-align: center;">
    <img src="img\assembly_rules\assembly_rules_1.svg" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
</div>

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


Сборка группы, **не включающей** в себя основной модуль, должна начинаться с <span class="hover-trigger" data-hover="popup2">оконечного модуля</span>. Вторым в такой группе устанавливается [Модуль ввода питания SPPM](SPPM.md), после чего устанавливаются модули расширения в соответсвии с [организацией питания в группах]().

<div style="text-align: center;">
    <img src="img\assembly_rules\assembly_rules_2.svg" 
         alt="Image title" 
         width="500" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
</div>

<div id="popup2" class="hover-popup" data-markdown="**Оконечные модули**
*Оконечные модули - это специальные модули расширения, которые обеспечивают связь двух групп между собой и горячую замену модулей*

На настоящий момент представлено 2 **оконечных** модуля
- [Модуль оконечный SPTM](SPTM.md)
  - Обеспечивает связь между группами при помощи Ethernet-кабеля с патч-кордами **RJ-45**
- [Модуль оконечный SPSFP](SPSFP.md)
  - Обеспечивает связь между группами при помощи **оптоволоконного кабеля**">
</div>
    
Для расширения контроллера последующими группами или подключения по схеме [«Кольцо»](assembly.md#_2), в конце группы ставится <span class="hover-trigger" data-hover="popup2">модуль оконечный</span>.

!!! success "Рекомендация"
    Рекомендуем в любом случае ставить модуль оконечный в конце группы для дальнейшего подключения по схеме [«Кольцо»](assembly.md#_2). Это повышает надежность контроллера.
!!! danger "Обратите внимание"
    На первый и последний модули в группе в обязательном порядке ставится заглушка


<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin: 30px 0; gap: 20px;">
    <!-- Первые изображения - видны на сайте -->
    <div style="flex: 1; min-width: 200px; display: flex; justify-content: center;">
        <img src="img\assembly_rules\assembly_rules_3_1m.svg" 
             alt="Installation 1" 
             width="235" 
             style="cursor: zoom-in; max-width: 100%; height: auto;"
             onclick="openGallery(0, 'gallery1')">
    </div>
    <div style="flex: 1; min-width: 200px; display: flex; justify-content: center;">
        <img src="img\assembly_rules\assembly_rules_3_2m.svg" 
             alt="Installation 2" 
             width="220" 
             style="cursor: zoom-in; max-width: 100%; height: auto;"
             onclick="openGallery(1, 'gallery1')">
    </div>
    <div style="flex: 1; min-width: 200px; display: flex; justify-content: center;">
        <img src="img\assembly_rules\assembly_rules_3_3m.svg" 
             alt="Installation 3" 
             width="220" 
             style="cursor: zoom-in; max-width: 100%; height: auto;"
             onclick="openGallery(2, 'gallery1')">
    </div>
     <div style="flex: 1; min-width: 200px; display: flex; justify-content: center;">
        <img src="img\assembly_rules\assembly_rules_3_4m.svg" 
             alt="Installation 4" 
             width="220" 
             style="cursor: zoom-in; max-width: 100%; height: auto;"
             onclick="openGallery(3, 'gallery1')">
    </div>
</div>

<!-- Модальное окно галереи -->
<div id="galleryModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; cursor: pointer;">
    
    <!-- Кнопка закрытия -->
 <div style="position: absolute; top: 20px; right: 20px; z-index: 10000;">
        <button onclick="closeGallery()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">×</button>
    </div>
    
    <!-- Кнопка назад -->
 <div style="position: absolute; top: 50%; left: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="prevImage()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">‹</button>
    </div>
    
    <!-- Кнопка вперед -->
 <div style="position: absolute; top: 50%; right: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="nextImage()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">›</button>
    </div>
    
    <!-- Область изображения -->
 <div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; padding: 20px; box-sizing: border-box;">
        <img id="galleryImage" src="" alt="" style="max-width: 100%; max-height: 100%; background: white; padding: 20px; border-radius: 8px; object-fit: contain; cursor: pointer;">
    </div>
    
    <!-- Счетчик изображений -->
 <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 18px; background: rgba(0,0,0,0.5); padding: 10px 20px; border-radius: 20px;">
        <span id="imageCounter">1 / 4</span>
    </div>
</div>

<script>
// Разные наборы изображений для разных галерей
const gallerySets = {
    'gallery1': [
        'img/assembly_rules/assembly_rules_3_1.svg',
        'img/assembly_rules/assembly_rules_3_2.svg',
        'img/assembly_rules/assembly_rules_3_3.svg',
        'img/assembly_rules/assembly_rules_3_4.svg',
    ],
};

let currentImages = [];
let currentIndex = 0;
let currentGallery = '';

function openGallery(index, galleryId) {
    currentIndex = index;
    currentGallery = galleryId;
    currentImages = gallerySets[galleryId]  [];
    
    const modal = document.getElementById('galleryModal');
    const galleryImage = document.getElementById('galleryImage');
    const imageCounter = document.getElementById('imageCounter');
    
    if (currentImages.length > 0) {
        galleryImage.src = currentImages[currentIndex];
        imageCounter.textContent = `${currentIndex + 1} / ${currentImages.length}`;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
}

function closeGallery() {
    const modal = document.getElementById('galleryModal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
    currentImages = [];
    currentGallery = '';
}

function prevImage() {
    if (currentImages.length > 0) {
        currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
        updateGallery();
    }
}

function nextImage() {
    if (currentImages.length > 0) {
        currentIndex = (currentIndex + 1) % currentImages.length;
        updateGallery();
    }
}

function updateGallery() {
    const galleryImage = document.getElementById('galleryImage');
    const imageCounter = document.getElementById('imageCounter');
    
    if (currentImages.length > 0) {
        galleryImage.src = currentImages[currentIndex];
        imageCounter.textContent = `${currentIndex + 1} / ${currentImages.length}`;
    }
}

// Управление клавиатурой
document.addEventListener('keydown', function(e) {
    const modal = document.getElementById('galleryModal');
    if (modal.style.display === 'block') {
        if (e.key === 'Escape') {
            closeGallery();
        } else if (e.key === 'ArrowLeft') {
            prevImage();
        } else if (e.key === 'ArrowRight') {
            nextImage();
        }
    }
});

// Закрытие по клику на фон или на изображение
document.getElementById('galleryModal').addEventListener('click', function(e) {
    // Закрываем при клике на фон ИЛИ на само изображение
    if (e.target === this  e.target.id === 'galleryImage') {
        closeGallery();
    }
});
</script>

## Организация питания в группе

Правильная организация питания в группе позволяет реализовать функции [горяцей замены модулей]() и [резервирование питания]() контроллера и обенспечивает бесперебойную работу контроллера.

[Модуль ввода питания SPPM]() обеспечивает питание всех остальных модулей контроллера. Он позволяет запитать до **48 Вт** нагрузки. Базово [Модуль ввода питания SPPM]() питает правостоящие от него модули, однако если установлена перемычка он питает как правостоящие, так и левостоящие от него модули, но максимальная мощность питания остается неизменной - 48 Вт.

Потребляемая мощность всех модулей приведена ниже:

<div class="compact-center">

<table class="compact-center">
  <thead>
    <tr>
      <th>Наименование модуля</th>
      <th>Максимальная потребляемая мощность, Вт</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>GMB</td><td>7,5</td></tr>
    <tr><td>DI</td><td>5</td></tr>
    <tr><td>DO</td><td>3</td></tr>
    <tr><td>AIC</td><td>4</td></tr>
    <tr><td>AIV</td><td>2,5</td></tr>
    <tr><td>AITC</td><td>5,5</td></tr>
    <tr><td>AITR</td><td>2,5</td></tr>
    <tr><td>AO</td><td>7,5</td></tr>
    <tr><td>SPPC</td><td>3</td></tr>
    <tr><td>SPPM</td><td>0,5</td></tr>
    <tr><td>SPTM</td><td>0</td></tr>
    <tr><td>IF485/422</td><td>2,5</td></tr>
  </tbody>
</table>

</div>


### Организация питания **без** функции горячей замены модуля

При организации питания без поддержки горячей замены модулей должно выполняться следующие правило:

Сумма потребляемой мощности всех модулей расширения, стоящих справа **от текущего до следующего** [Модуля ввода питания SPPM](), **включая модуль ввода питания** не должна превышать 48 Вт. 

<div style="text-align: center;">
    <img src="img\assembly_rules\assembly_rules_4.svg" 
         alt="Image title" 
         width="700" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
</div>

!!! Example "Пример"
    Например песле первого Модуля SPPM мы поставили:

    _- 1 GMB (7,5 Вт)_

    _- 2 АО (2*7,5 Вт)_

    _- 2 DI (2*5 Вт)_

    _- 4 DO (4*3 Вт)_

    _- и не забыли про то что Модуль ввода питания потребляет 0,5 Вт_

    Таким образом суммарная потребляемая мощность модулей будет равна:

    _P = 7,5 + 2*7,5 + 2*5 + 4*3 + 0,5 = 45 Вт_

    Что меньше 48, значит правило соблюдается :)

### Организация питания с функцией горячей замены модуля

При организации питания с поддержкой **горячей замены модуля** каждый [Модуль ввода питания]() отвечает за питание двух зон модулей в группе:

1. Модули расширения, расположенные справа от текущего до следующего [Модуля ввода питания SPPM]()
2. Модули расширения, расположенные слева от текущего до следующего [Модуля ввода питания SPPM]()

Каждый [Модуль ввода питания]() ставится из расчета, что он питает обе зоны, то есть потребляемая мощность модулей расширения в этих двух зонах, включая [Модуль ввода питания]()  не должна превышать 48 Вт.
В расчет потребляемой мощность не включается самый левый модуль в левой зоне.

!!! info "Информация"
    В нормальном режиме функционирования [Модуль ввода питания]() питает только правую зону, однако в момент [горячей замены]() модуля, он также начинает питать и зону слева от него


<div style="text-align: center;">
    <img src="img\assembly_rules\assembly_rules_5_1.svg" 
         alt="Image title" 
         width="700" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
</div>

## Резервирование питания контроллера
Резервирование питания контроллера необходимо для повышения его устойчивости к помехам питания от внешних источников питания.

На вход каждого из [Модулей ввода питания]() подается питание **24 В** от двух независимых источничников питания. [Модуль ввода питания]() анализирует питание от каждого из источников и, как бы, выбирает лучшее для дальнейшей выдачи его в шину питания модулей.

Организация питания контроллера с резервированием питания позволяет обеспечить непрерывную работу контроллера в случаях, когда один из источников питания неисправен.

!!! success "Рекомендация"
    Контроллер может работать от одного источника питания **без** резервирования питания, однако рекомендуем всегда организовывать питание с применением данной функции.

Для бесперебойной работы [горячей замены модулей]() необходимо придерживаться следующего правила: на каждый [Модуль ввода питания SPPM](), расположенных в одной группе, подается питание с одних и тех же источников питания. 

!!! info "Информация"
    Питание других групп может осужествляться как от других источников питания, так и от этих же.

<div style="text-align: center;">
    <img src="img\assembly_rules\assembly_rules_6.svg" 
         alt="Image title" 
         width="700" 
         class="zoom-trigger"
         onclick="openZoomModal(this.src, this.alt)">
</div>