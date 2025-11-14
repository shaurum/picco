# Монтаж и демонтаж

## Монтаж модулей на DIN-рейку

!!! Info "Подготовка к монтажу"
    Перед монтажом для контроллера предварительно организуется рабочее место, обеспечивающее защиту от попадания влаги, грязи и посторонних предметов. 
!!! Info ""
    Монтаж модулей осуществляется в вертикальном положении посредством присоединения к стандартной DIN-рейке шириной 35 мм.


Монтаж первого модуля группы осуществляется следующим образом: приставить модуль к DIN-рейке пазом, расположенном на тыльной стороне модуля, после чего зафиксировать, установив верхнюю и нижнюю защелки в положение «закрыто».

<div style="display: flex; gap: 20px; flex-wrap: wrap; margin: 30px 0;">
    <img src="img/inistallation/inistallation_1_1.svg" 
         alt="Installation 1" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery(0)">
    <img src="img/inistallation/inistallation_1_2.svg" 
         alt="Installation 2" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery(1)">
    <img src="img/inistallation/inistallation_1_3.svg" 
         alt="Installation 3" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery(2)">
</div>

<!-- Модальное окно галереи -->
<div id="galleryModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; cursor: zoom-out;">
    
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
    <div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">
        <img id="galleryImage" src="" alt="" style="max-width: 90%; max-height: 90%; background: white; padding: 20px; border-radius: 8px; object-fit: contain;">
    </div>
    
    <!-- Счетчик изображений -->
    <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 18px; background: rgba(0,0,0,0.5); padding: 10px 20px; border-radius: 20px;">
        <span id="imageCounter">1 / 3</span>
    </div>
</div>

<script>
const images = [
    'img/inistallation/inistallation_1_1.svg',
    'img/inistallation/inistallation_1_2.svg', 
    'img/inistallation/inistallation_1_3.svg'
];

let currentIndex = 0;

function openGallery(index) {
    currentIndex = index;
    const modal = document.getElementById('galleryModal');
    const galleryImage = document.getElementById('galleryImage');
    const imageCounter = document.getElementById('imageCounter');
    
    galleryImage.src = images[currentIndex];
    imageCounter.textContent = `${currentIndex + 1} / ${images.length}`;
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeGallery() {
    const modal = document.getElementById('galleryModal');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateGallery();
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    updateGallery();
}

function updateGallery() {
    const galleryImage = document.getElementById('galleryImage');
    const imageCounter = document.getElementById('imageCounter');
    
    galleryImage.src = images[currentIndex];
    imageCounter.textContent = `${currentIndex + 1} / ${images.length}`;
}

// Закрытие по ESC
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

// Закрытие по клику на фон
document.getElementById('galleryModal').addEventListener('click', function(e) {
    if (e.target === this) {
        closeGallery();
    }
});
</script>

Монтаж каждого последующего модуля осуществляется путем присоединения его к уже установленному модулю методом шип-паз. Устанавливаемый модуль задвигается вдоль шип-паза до упора к DIN-рейке и фиксируется верхней и нижней защелками в положение «закрыто».

<div style="display: flex; gap: 20px; justify-content: center; margin: 20px 0;">
    <img src="img/inistallation/inistallation_2_1.svg" 
         alt="Installation 2-1" 
         width="250" 
         style="cursor: zoom-in;"
         onclick="openGallery2(0)">
    
    <img src="img/inistallation/inistallation_2_2.svg" 
         alt="Installation 2-2" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery2(1)">
    
    <img src="img/inistallation/inistallation_2_3.svg" 
         alt="Installation 2-3" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery2(2)">
</div>

<!-- Модальное окно галереи для второй группы -->
<div id="galleryModal2" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; cursor: zoom-out;">
    
    <!-- Кнопка закрытия -->
    <div style="position: absolute; top: 20px; right: 20px; z-index: 10000;">
        <button onclick="closeGallery2()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">×</button>
    </div>
    
    <!-- Кнопка назад -->
    <div style="position: absolute; top: 50%; left: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="prevImage2()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">‹</button>
    </div>
    
    <!-- Кнопка вперед -->
    <div style="position: absolute; top: 50%; right: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="nextImage2()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">›</button>
    </div>
    
    <!-- Область изображения -->
    <div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">
        <img id="galleryImage2" src="" alt="" style="max-width: 90%; max-height: 90%; background: white; padding: 20px; border-radius: 8px; object-fit: contain;">
    </div>
    
    <!-- Счетчик изображений -->
    <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 18px; background: rgba(0,0,0,0.5); padding: 10px 20px; border-radius: 20px;">
        <span id="imageCounter2">1 / 3</span>
    </div>
</div>

<script>
// Данные для второй галереи
const images2 = [
    'img/inistallation/inistallation_2_1.svg',
    'img/inistallation/inistallation_2_2.svg', 
    'img/inistallation/inistallation_2_3.svg'
];

let currentIndex2 = 0;

function openGallery2(index) {
    currentIndex2 = index;
    const modal = document.getElementById('galleryModal2');
    const galleryImage = document.getElementById('galleryImage2');
    const imageCounter = document.getElementById('imageCounter2');
    
    galleryImage.src = images2[currentIndex2];
    imageCounter.textContent = `${currentIndex2 + 1} / ${images2.length}`;
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeGallery2() {
    const modal = document.getElementById('galleryModal2');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function prevImage2() {
    currentIndex2 = (currentIndex2 - 1 + images2.length) % images2.length;
    updateGallery2();
}

function nextImage2() {
    currentIndex2 = (currentIndex2 + 1) % images2.length;
    updateGallery2();
}

function updateGallery2() {
    const galleryImage = document.getElementById('galleryImage2');
    const imageCounter = document.getElementById('imageCounter2');
    
    galleryImage.src = images2[currentIndex2];
    imageCounter.textContent = `${currentIndex2 + 1} / ${images2.length}`;
}

// Управление клавиатурой для второй галереи
document.addEventListener('keydown', function(e) {
    const modal = document.getElementById('galleryModal2');
    if (modal.style.display === 'block') {
        if (e.key === 'Escape') {
            closeGallery2();
        } else if (e.key === 'ArrowLeft') {
            prevImage2();
        } else if (e.key === 'ArrowRight') {
            nextImage2();
        }
    }
});

// Закрытие по клику на фон для второй галереи
document.getElementById('galleryModal2').addEventListener('click', function(e) {
    if (e.target === this) {
        closeGallery2();
    }
});
</script>

## Монтаж подводящих кабелей
!!! Info "Подготовка к монтажу"
    Перед началом работ по подключению необходимо убедиться, что кабели обесточены. 

1. При подключении одножильного провода или многожильного провода с НШВИ подключить провод к клеммной колодке путем надавливания до упора.
2. При подключении многожильного провода без НШВИ надавить на защелку, находящуюся на клеммной колодке напротив нужного разъема, и одновременно подключить провод к клеммной колодке путем ввода до упора.
3. Подключить все необходимые подводящие кабели на каждый модуль.
    <!-- Первая строка из 3 изображений -->
    <div style="display: flex; gap: 20px; justify-content: center; margin: 20px 0;">
        <img src="img/inistallation/inistallation_3_1.svg" 
            alt="Installation 3-1" 
            width="245" 
            style="cursor: zoom-in;"
            onclick="openGallery3A(0)">
        <img src="img/inistallation/inistallation_3_2.svg" 
            alt="Installation 3-2" 
            width="245" 
            style="cursor: zoom-in;"
            onclick="openGallery3A(1)">
        <img src="img/inistallation/inistallation_3_3.svg" 
            alt="Installation 3-3" 
            width="245" 
            style="cursor: zoom-in;"
            onclick="openGallery3A(2)">
    </div>

    <!-- Модальное окно галереи для первой группы -->
    <div id="galleryModal3A" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; cursor: zoom-out;">
        
        <!-- Кнопка закрытия -->
        <div style="position: absolute; top: 20px; right: 20px; z-index: 10000;">
            <button onclick="closeGallery3A()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">×</button>
        </div>
        
        <!-- Кнопка назад -->
        <div style="position: absolute; top: 50%; left: 20px; transform: translateY(-50%); z-index: 10000;">
            <button onclick="prevImage3A()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">‹</button>
        </div>
        
        <!-- Кнопка вперед -->
        <div style="position: absolute; top: 50%; right: 20px; transform: translateY(-50%); z-index: 10000;">
            <button onclick="nextImage3A()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">›</button>
        </div>
        
        <!-- Область изображения -->
        <div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">
            <img id="galleryImage3A" src="" alt="" style="max-width: 90%; max-height: 90%; background: white; padding: 20px; border-radius: 8px; object-fit: contain;">
        </div>
        
        <!-- Счетчик изображений -->
        <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 18px; background: rgba(0,0,0,0.5); padding: 10px 20px; border-radius: 20px;">
            <span id="imageCounter3A">1 / 3</span>
        </div>
    </div>

    <script>
    // Данные для галереи 3A
    const images3A = [
        'img/inistallation/inistallation_3_1.svg',
        'img/inistallation/inistallation_3_2.svg', 
        'img/inistallation/inistallation_3_3.svg'
    ];

    let currentIndex3A = 0;

    function openGallery3A(index) {
        currentIndex3A = index;
        const modal = document.getElementById('galleryModal3A');
        const galleryImage = document.getElementById('galleryImage3A');
        const imageCounter = document.getElementById('imageCounter3A');
        
        galleryImage.src = images3A[currentIndex3A];
        imageCounter.textContent = `${currentIndex3A + 1} / ${images3A.length}`;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }

    function closeGallery3A() {
        const modal = document.getElementById('galleryModal3A');
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }

    function prevImage3A() {
        currentIndex3A = (currentIndex3A - 1 + images3A.length) % images3A.length;
        updateGallery3A();
    }

    function nextImage3A() {
        currentIndex3A = (currentIndex3A + 1) % images3A.length;
        updateGallery3A();
    }

    function updateGallery3A() {
        const galleryImage = document.getElementById('galleryImage3A');
        const imageCounter = document.getElementById('imageCounter3A');
        
        galleryImage.src = images3A[currentIndex3A];
        imageCounter.textContent = `${currentIndex3A + 1} / ${images3A.length}`;
    }

    // Управление клавиатурой для галереи 3A
    document.addEventListener('keydown', function(e) {
        const modal = document.getElementById('galleryModal3A');
        if (modal.style.display === 'block') {
            if (e.key === 'Escape') {
                closeGallery3A();
            } else if (e.key === 'ArrowLeft') {
                prevImage3A();
            } else if (e.key === 'ArrowRight') {
                nextImage3A();
            }
        }
    });

    // Закрытие по клику на фон для галереи 3A
    document.getElementById('galleryModal3A').addEventListener('click', function(e) {
        if (e.target === this) {
            closeGallery3A();
        }
    });
    </script>

4. Вставить клеммную колодку в специальный разъем на модуле.
5. Затянуть винты клеммной колодки с усилием 0,2 Нм.
6. Для удобства следует зафиксировать провода вместе относительно модуля путем закрепления хомута через ушко корпуса модуля.
<!-- Вторая строка из 3 изображений -->
<div style="display: flex; gap: 20px; justify-content: center; margin: 20px 0;">
    <img src="img/inistallation/inistallation_3_4.svg" 
         alt="Installation 3-4" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery3B(0)">
        <img src="img/inistallation/inistallation_3_5.svg" 
         alt="Installation 3-5" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery3B(1)">
        <img src="img/inistallation/inistallation_3_6.svg" 
         alt="Installation 3-6" 
         width="240" 
         style="cursor: zoom-in;"
         onclick="openGallery3B(2)">
</div>

<!-- Модальное окно галереи для второй группы -->
<div id="galleryModal3B" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; cursor: zoom-out;">
    
    <!-- Кнопка закрытия -->
    <div style="position: absolute; top: 20px; right: 20px; z-index: 10000;">
        <button onclick="closeGallery3B()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">×</button>
    </div>
    
    <!-- Кнопка назад -->
    <div style="position: absolute; top: 50%; left: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="prevImage3B()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">‹</button>
    </div>
    
    <!-- Кнопка вперед -->
    <div style="position: absolute; top: 50%; right: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="nextImage3B()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">›</button>
    </div>
    
    <!-- Область изображения -->
    <div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">
        <img id="galleryImage3B" src="" alt="" style="max-width: 90%; max-height: 90%; background: white; padding: 20px; border-radius: 8px; object-fit: contain;">
    </div>
    
    <!-- Счетчик изображений -->
    <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 18px; background: rgba(0,0,0,0.5); padding: 10px 20px; border-radius: 20px;">
        <span id="imageCounter3B">1 / 3</span>
    </div>
</div>

<script>
// Данные для галереи 3B
const images3B = [
    'img/inistallation/inistallation_3_4.svg',
    'img/inistallation/inistallation_3_5.svg',
    'img/inistallation/inistallation_3_6.svg'
];

let currentIndex3B = 0;

function openGallery3B(index) {
    currentIndex3B = index;
    const modal = document.getElementById('galleryModal3B');
    const galleryImage = document.getElementById('galleryImage3B');
    const imageCounter = document.getElementById('imageCounter3B');
    
    galleryImage.src = images3B[currentIndex3B];
    imageCounter.textContent = `${currentIndex3B + 1} / ${images3B.length}`;
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeGallery3B() {
    const modal = document.getElementById('galleryModal3B');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function prevImage3B() {
    currentIndex3B = (currentIndex3B - 1 + images3B.length) % images3B.length;
    updateGallery3B();
}

function nextImage3B() {
    currentIndex3B = (currentIndex3B + 1) % images3B.length;
    updateGallery3B();
}

function updateGallery3B() {
    const galleryImage = document.getElementById('galleryImage3B');
    const imageCounter = document.getElementById('imageCounter3B');
    
    galleryImage.src = images3B[currentIndex3B];
    imageCounter.textContent = `${currentIndex3B + 1} / ${images3B.length}`;
}

// Управление клавиатурой для галереи 3B
document.addEventListener('keydown', function(e) {
    const modal = document.getElementById('galleryModal3B');
    if (modal.style.display === 'block') {
        if (e.key === 'Escape') {
            closeGallery3B();
        } else if (e.key === 'ArrowLeft') {
            prevImage3B();
        } else if (e.key === 'ArrowRight') {
            nextImage3B();
        }
    }
});

// Закрытие по клику на фон для галереи 3B
document.getElementById('galleryModal3B').addEventListener('click', function(e) {
    if (e.target === this) {
        closeGallery3B();
    }
});
</script>


Для монтажа кабелей должны выполняться следующие требования:

- Для обеспечения надёжности электрических соединений рекомендуется использовать только медные провода. 
- При использовании одножильного провода перед соединением необходимо зачистить на длину 12 мм, с таким расчетом, чтобы срез изоляции плотно прилегал к клеммной колодке, т.е. чтобы оголенные участки провода не выступали за ее пределы.
!!! warning "Предупреждение"
    Использование наконечников типа НШВИ длинной менее 12 мм может привести к ненадежной фиксации контактов.
- Для гибкого (многожильного) провода следует использовать наконечники штыревые втулочные изолированные типа НШВИ длиной 12 мм соответствующего сечения кабеля. Допускается монтаж многожильного провода без использования НШВИ, предварительно скрутив жилы провода.
- Максимальное сечение проводов, подключаемых к клеммной колодке при монтаже – 1,5 мм2.
!!! success "Рекомендация"
    Рекомендуемое сечение проводов для подключения к клеммной колодке – 0,5 мм².

## Демонтаж подводящих кабелей 
!!! Info "Подготовка к демонтажу"
    Перед началом работ необходимо убедиться, что кабели обесточены. 
2. Открутить винты на клеммной колодке.
3. Отсоединить клеммную колодку от модуля потянув на себя.
4. Надавить отверткой на защелку оранжевого цвета, расположенной на клеммной колодке напротив демонтируемого кабеля, и одновременно потянуть демонтируемый кабель на себя.

<div style="display: flex; gap: 20px; justify-content: center; margin: 20px 0;">
    <img src="img/inistallation/inistallation_4_1.svg" 
         alt="Installation 4-1" 
         width="250" 
         style="cursor: zoom-in;"
         onclick="openGallery4(0)">
    <img src="img/inistallation/inistallation_4_2.svg" 
         alt="Installation 4-1" 
         width="250" 
         style="cursor: zoom-in;"
         onclick="openGallery4(1)">
    <img src="img/inistallation/inistallation_4_3.svg" 
         alt="Installation 4-1" 
         width="250" 
         style="cursor: zoom-in;"
         onclick="openGallery4(1)">
</div>

<!-- Модальное окно галереи для четвертой группы -->
<div id="galleryModal4" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; cursor: zoom-out;">
    
    <!-- Кнопка закрытия -->
    <div style="position: absolute; top: 20px; right: 20px; z-index: 10000;">
        <button onclick="closeGallery4()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">×</button>
    </div>
    
    <!-- Кнопка назад -->
    <div style="position: absolute; top: 50%; left: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="prevImage4()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">‹</button>
    </div>
    
    <!-- Кнопка вперед -->
    <div style="position: absolute; top: 50%; right: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="nextImage4()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">›</button>
    </div>
    
    <!-- Область изображения -->
    <div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">
        <img id="galleryImage4" src="" alt="" style="max-width: 90%; max-height: 90%; background: white; padding: 20px; border-radius: 8px; object-fit: contain;">
    </div>
    
    <!-- Счетчик изображений -->
    <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 18px; background: rgba(0,0,0,0.5); padding: 10px 20px; border-radius: 20px;">
        <span id="imageCounter4">1 / 2</span>
    </div>
</div>

<script>
// Данные для четвертой галереи
const images4 = [
    'img/inistallation/inistallation_4_1.svg',
    'img/inistallation/inistallation_4_2.svg',
    'img/inistallation/inistallation_4_3.svg'
];

let currentIndex4 = 0;

function openGallery4(index) {
    currentIndex4 = index;
    const modal = document.getElementById('galleryModal4');
    const galleryImage = document.getElementById('galleryImage4');
    const imageCounter = document.getElementById('imageCounter4');
    
    galleryImage.src = images4[currentIndex4];
    imageCounter.textContent = `${currentIndex4 + 1} / ${images4.length}`;
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeGallery4() {
    const modal = document.getElementById('galleryModal4');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function prevImage4() {
    currentIndex4 = (currentIndex4 - 1 + images4.length) % images4.length;
    updateGallery4();
}

function nextImage4() {
    currentIndex4 = (currentIndex4 + 1) % images4.length;
    updateGallery4();
}

function updateGallery4() {
    const galleryImage = document.getElementById('galleryImage4');
    const imageCounter = document.getElementById('imageCounter4');
    
    galleryImage.src = images4[currentIndex4];
    imageCounter.textContent = `${currentIndex4 + 1} / ${images4.length}`;
}

// Управление клавиатурой для четвертой галереи
document.addEventListener('keydown', function(e) {
    const modal = document.getElementById('galleryModal4');
    if (modal.style.display === 'block') {
        if (e.key === 'Escape') {
            closeGallery4();
        } else if (e.key === 'ArrowLeft') {
            prevImage4();
        } else if (e.key === 'ArrowRight') {
            nextImage4();
        }
    }
});

// Закрытие по клику на фон для четвертой галереи
document.getElementById('galleryModal4').addEventListener('click', function(e) {
    if (e.target === this) {
        closeGallery4();
    }
});
</script>

## Демонтаж модулей
Перед демонтажем модуля необходимо убедится, что все подводящие к нему кабели отсоединены, затем с помощью плоской отвертки аккуратно перевести защелки, расположенные снизу и сверху, в положение «открыто». После чего потянуть модуль на себя вдоль шип-пазов до полного отсоединения.
 
<div style="display: flex; gap: 20px; justify-content: center; margin: 20px 0;">
    <img src="img/inistallation/inistallation_5_1.svg" 
         alt="Installation 5-1" 
         width="300" 
         style="cursor: zoom-in;"
         onclick="openGallery5(0)">
    
    <img src="img/inistallation/inistallation_5_2.svg" 
         alt="Installation 5-2" 
         width="300" 
         style="cursor: zoom-in;"
         onclick="openGallery5(1)">
</div>

<!-- Модальное окно галереи для пятой группы -->
<div id="galleryModal5" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); z-index: 9999; cursor: zoom-out;">
    
    <!-- Кнопка закрытия -->
    <div style="position: absolute; top: 20px; right: 20px; z-index: 10000;">
        <button onclick="closeGallery5()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">×</button>
    </div>
    
    <!-- Кнопка назад -->
    <div style="position: absolute; top: 50%; left: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="prevImage5()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">‹</button>
    </div>
    
    <!-- Кнопка вперед -->
    <div style="position: absolute; top: 50%; right: 20px; transform: translateY(-50%); z-index: 10000;">
        <button onclick="nextImage5()" style="background: rgba(0,0,0,0.5); color: white; border: 2px solid white; border-radius: 50%; width: 50px; height: 50px; font-size: 24px; cursor: pointer;">›</button>
    </div>
    
    <!-- Область изображения -->
    <div style="display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">
        <img id="galleryImage5" src="" alt="" style="max-width: 90%; max-height: 90%; background: white; padding: 20px; border-radius: 8px; object-fit: contain;">
    </div>
    
    <!-- Счетчик изображений -->
    <div style="position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: white; font-size: 18px; background: rgba(0,0,0,0.5); padding: 10px 20px; border-radius: 20px;">
        <span id="imageCounter5">1 / 2</span>
    </div>
</div>

<script>
// Данные для пятой галереи
const images5 = [
    'img/inistallation/inistallation_5_1.svg',
    'img/inistallation/inistallation_5_2.svg'
];

let currentIndex5 = 0;

function openGallery5(index) {
    currentIndex5 = index;
    const modal = document.getElementById('galleryModal5');
    const galleryImage = document.getElementById('galleryImage5');
    const imageCounter = document.getElementById('imageCounter5');
    
    galleryImage.src = images5[currentIndex5];
    imageCounter.textContent = `${currentIndex5 + 1} / ${images5.length}`;
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeGallery5() {
    const modal = document.getElementById('galleryModal5');
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function prevImage5() {
    currentIndex5 = (currentIndex5 - 1 + images5.length) % images5.length;
    updateGallery5();
}

function nextImage5() {
    currentIndex5 = (currentIndex5 + 1) % images5.length;
    updateGallery5();
}

function updateGallery5() {
    const galleryImage = document.getElementById('galleryImage5');
    const imageCounter = document.getElementById('imageCounter5');
    
    galleryImage.src = images5[currentIndex5];
    imageCounter.textContent = `${currentIndex5 + 1} / ${images5.length}`;
}

// Управление клавиатурой для пятой галереи
document.addEventListener('keydown', function(e) {
    const modal = document.getElementById('galleryModal5');
    if (modal.style.display === 'block') {
        if (e.key === 'Escape') {
            closeGallery5();
        } else if (e.key === 'ArrowLeft') {
            prevImage5();
        } else if (e.key === 'ArrowRight') {
            nextImage5();
        }
    }
});

// Закрытие по клику на фон для пятой галереи
document.getElementById('galleryModal5').addEventListener('click', function(e) {
    if (e.target === this) {
        closeGallery5();
    }
});
</script>

