# Модуль основной SA-P5-GMB 

## Общие сведения
 
<!-- Модуль GMB - адаптивный блок -->
<div class="gmb-block" style="display: flex; gap: 2rem; align-items: flex-start; margin: 1rem 0;">
    <!-- Изображение -->
    <img src="img/modules/GMB.png" alt="Модуль основной GMB" 
         width="150" 
         style="flex-shrink: 0; max-width: 30%; height: auto; width: auto;"
         loading="lazy">

    <!-- Текст -->
    <div style="flex: 1; text-align: left; padding: 0 1rem; box-sizing: border-box;">
        <p style="text-align: left; margin: 0 0 1rem 0; line-height: 1.4;">
            <strong>Наименование:</strong><br>
            Модуль основной GMB
        </p>
        
        <p style="text-align: left; margin: 0 0 1rem 0; line-height: 1.4;">
            <strong>Исполнения:</strong><br>
            • SA-P5-GMB (без покрытия)<br>
            • SA-P5-GMB-V (с лаковым покрытием)
        </p>
        
        <p style="text-align: left; margin: 0 0 1rem 0; line-height: 1.4;">
            <strong>Назначение:</strong><br>
            Модуль основной GMB (далее-модуль) является центральным компонентом системы управления.
        </p>
        
        <p style="text-align: left; margin: 0 0 0 0; line-height: 1.4;">
            <strong>Функции:</strong><br>
            • выполнение пользовательской прикладной программы управления;<br>
            • обмен информацией со сторонними устройствами по встроенным интерфейсам;<br>
            • звуковое оповещение при загрузке данных и при сбросе настроек;<br>
            • опрос модулей расширения.
        </p>
    </div>
</div>

<!-- Описание + Интерактивная схема -->
<div class="description-scheme" style="display: flex; gap: 2rem; align-items: flex-start; margin: 1rem 0;">
    <!-- Описание -->
    <div style="flex: 1; text-align: justify;">
        <p style="text-align: justify; margin: 0 0 8px 0;"><strong>Описание:</strong></p>
        <p style="text-align: justify; margin: 0 0 8px 0;">На передней панели модуля расположен переключатель режима работы RUN/STOP, предназначенный для запуска и остановки выполнения цикла основной программы.</p>
        <p style="text-align: justify; margin: 0 0 0 0;">Для сброса до заводских настроек на верхней грани модуля предусмотрена скрытая кнопка «Сброс». Необходимо нажать на кнопку тонким заостренным предметом и удерживать до появления трех звуковых сигналов, подтверждающих выполнение сброса.</p>
    </div>
    
    <!-- Интерактивная схема -->
    <div class="interactive-image">
        <img src="img/connection/GMB.svg" alt="Панель управления устройством" class="main-image">
        
        <!-- Точка на батарейке -->
        <div class="point" style="top: 25%; left: 53%;" data-video="video-battery">
            <span class="dot"></span>
            <div class="tooltip">Батарейка</div>
        </div>
        
        <!-- Точка на кнопке СРОС -->
        <div class="point" style="top: 14%; left: 33%;" data-video="video-emergency">
            <span class="dot"></span>
            <div class="tooltip">Кнопка Сброс</div>
        </div>
        
        <!-- Точка на переключателе РАН/СТОП -->
        <div class="point" style="top: 43%; left: 22%;" data-video="video-switch">
            <span class="dot"></span>
            <div class="tooltip">Переключатель RUN/STOP</div>
        </div>
    </div>
</div>

<!-- Дополнительный текст — теперь он идёт ПОСЛЕ схемы, в потоке документа -->
<p style="text-align: justify; margin: 0 0 0 0;">Также для обеспечения автономной работы часов реального времени при отключении основного питания на верхней грани корпуса модуля предусмотрен разъём под батарейку типа CR1620.</p>

<div style="clear: both;"></div>

<div id="video-battery" class="video-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <video controls loop muted playsinline>
      <source src="img/animation/battery.mp4" type="video/mp4">
      Ваш браузер не поддерживает видео тег.
    </video>
    <div class="video-title">Батарейка</div>
  </div>
</div>

<div id="video-emergency" class="video-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <video controls loop muted playsinline>
      <source src="img/animation/reset.mp4" type="video/mp4">
      Ваш браузер не поддерживает видео тег.
    </video>
    <div class="video-title">Кнопка Сброс</div>
  </div>
</div>

<div id="video-switch" class="video-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <video controls loop muted playsinline>
      <source src="img/animation/run_stop.mp4" type="video/mp4">
      Ваш браузер не поддерживает видео тег.
    </video>
    <div class="video-title">Переключатель RUN/STOP</div>
  </div>
</div>

<style>
/* --- СТИЛИ ДЛЯ ВСЕХ УСТРОЙСТВ --- */
.interactive-image {
  position: relative;
  display: inline-block;
  max-width: 100%;
  margin: 20px 0;
}

.main-image {
  width: 100%;
  height: auto;
  border: 1px;
  border-radius: 4px;
}

.point {
  position: absolute;
  display: block;
  width: 24px;
  height: 24px;
  cursor: pointer;
  transform: translate(-50%, -50%);
  z-index: 100;
}

.dot {
  display: block;
  width: 16px;
  height: 16px;
  background: #f39200;
  border: 3px solid white;
  border-radius: 50%;
  box-shadow: 0 0 6px rgba(0,0,0,0.7);
  transition: all 0.3s ease;
  animation: pulse 2s infinite;
}

.point:hover .dot {
  transform: scale(1.4);
  background: #ffaa33;
  animation: none;
}

.tooltip {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0,0,0,0.85);
  color: white;
  padding: 8px 12px;
  border-radius: 6px;
  white-space: nowrap;
  font-size: 14px;
  font-weight: bold;
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
  z-index: 10;
}

.point:hover .tooltip {
  opacity: 1;
}

.video-modal {
  display: none;
  position: fixed;
  z-index: 10000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.95);
  backdrop-filter: blur(10px);
}

.modal-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: transparent;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,0.5);
  max-width: 90vw;
  max-height: 90vh;
}

.modal-content video {
  display: block;
  width: auto;
  height: auto;
  max-width: 80vw;
  max-height: 80vh;
  border-radius: 8px;
}

.video-title {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0,0,0,0.8));
  color: white;
  padding: 30px 20px 15px 20px;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
}

.close {
  position: absolute;
  top: 15px;
  right: 15px;
  font-size: 28px;
  font-weight: bold;
  color: white;
  cursor: pointer;
  z-index: 10001;
  transition: color 0.3s;
  line-height: 1;
  background: rgba(0,0,0,0.5);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255,255,255,0.3);
}

.close:hover {
  color: #f39200;
  background: rgba(0,0,0,0.7);
  border-color: rgba(255,255,255,0.5);
}

@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(243, 146, 0, 0.7); }
  70% { box-shadow: 0 0 0 10px rgba(243, 146, 0, 0); }
  100% { box-shadow: 0 0 0 0 rgba(243, 146, 0, 0); }
}

/* --- АДАПТАЦИЯ ПОД МОБИЛЬНЫЕ УСТРОЙСТВА (≤ 768px) --- */
@media (max-width: 768px) {
  .gmb-block {
    flex-direction: column;
    gap: 1rem;
  }

  .gmb-block img {
    width: 100%;
    max-width: 180px;
    margin: 0 auto;
  }

  .gmb-block div {
    padding: 0.5rem 0.75rem;
    width: 100%;
  }

  .description-scheme {
    flex-direction: column;
    gap: 1rem;
  }

  .description-scheme .interactive-image {
    width: 100%;
    max-width: 400px;
    margin: 0 auto;
  }

  .point {
    width: 30px;
    height: 30px;
  }

  .dot {
    width: 20px;
    height: 20px;
  }

  .tooltip {
    font-size: 12px;
    padding: 6px 10px;
  }

  .modal-content {
    max-width: 95vw;
    max-height: 95vh;
  }

  .modal-content video {
    max-width: 95vw;
    max-height: 85vh;
  }

  .video-title {
    font-size: 16px;
    padding: 25px 15px 10px 15px;
  }

  .close {
    top: 15px;
    right: 15px;
    width: 45px;
    height: 45px;
    font-size: 32px;
  }
}

@media (max-width: 480px) {
  .video-title {
    font-size: 14px;
    padding: 20px 10px 8px 10px;
  }

  .modal-content video {
    max-height: 80vh;
  }

  p[style*="Также для обеспечения"] {
    margin: 1.2rem 0 0 0 !important;
    font-size: clamp(14px, 4vw, 16px) !important;
    line-height: 1.5 !important;
  }
}
</style>

<script>
let scrollPosition = 0;

// Единый обработчик кликов на весь документ (делегирование)
document.addEventListener('click', function(e) {
  // Клик по точке для открытия видео
  if (e.target.closest('.point')) {
    e.preventDefault();
    e.stopPropagation();
    
    const point = e.target.closest('.point');
    const videoId = point.getAttribute('data-video');
    const modal = document.getElementById(videoId);
    
    if (!modal) return;
    
    // Сохраняем позицию скролла
    scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
    
    // Показываем модалку
    modal.style.display = 'block';
    
    // Блокируем скролл
    document.body.style.overflow = 'hidden';
    document.body.style.position = 'fixed';
    document.body.style.top = `-${scrollPosition}px`;
    document.body.style.width = '100%';
    
    // === КЛЮЧЕВОЕ: play() вызывается СРАЗУ в контексте клика ===
    const video = modal.querySelector('video');
    if (video) {
      video.currentTime = 0;
      // Пробуем воспроизвести СРАЗУ — в контексте прямого клика
      const playPromise = video.play();
      if (playPromise !== undefined) {
        playPromise.catch(err => {
          // Если не сработало — не страшно, controls включены
          console.warn('Авто-воспроизведение заблокировано:', err);
        });
      }
    }
  }
  
  // Клик по кнопке закрытия
  if (e.target.closest('.close')) {
    const modal = e.target.closest('.video-modal');
    if (modal) closeVideoModal(modal);
  }
  
  // Клик по фону модалки
  if (e.target.classList.contains('video-modal')) {
    closeVideoModal(e.target);
  }
});

// Обработчик клавиш
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    const openModal = document.querySelector('.video-modal[style*="block"]');
    if (openModal) closeVideoModal(openModal);
  }
});

function closeVideoModal(modal) {
  if (!modal) return;
  
  const video = modal.querySelector('video');
  if (video) {
    video.pause();
    video.currentTime = 0;
  }
  
  modal.style.display = 'none';
  
  // Восстанавливаем скролл
  document.body.style.overflow = '';
  document.body.style.position = '';
  document.body.style.top = '';
  document.body.style.width = '';
  
  window.scrollTo(0, scrollPosition);
}

// Остановка видео при уходе со страницы
window.addEventListener('beforeunload', function() {
  document.querySelectorAll('.video-modal video').forEach(v => {
    v.pause();
    v.currentTime = 0;
  });
});
</script>

## Технические характеристики  
<div style="width: 100%; display: grid; grid-template-columns: 1fr;">
  <table class="responsive-table">
    <colgroup>
      <col class="col-parameter">
      <col class="col-value">
    </colgroup>
    <thead>
      <tr>
        <th class="header-cell">Характеристика</th>
        <th class="header-cell">Значение</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="data-cell">Ядро</td>
        <td class="data-cell">4 x Cortex-A72</td>
      </tr>
      <tr>
        <td class="data-cell">Оперативная память, Гб</td>
        <td class="data-cell">4, DDR4</td>
      </tr>
      <tr>
        <td class="data-cell">Объем памяти, Гб</td>
        <td class="data-cell">8</td>
      </tr>
      <tr>
        <td class="data-cell vertical-middle">Поддерживаемые интерфейсы</td>
        <td class="data-cell">Ethernet 1000 Мбит/с – 1,<br>Ethernet 100 Мбит/с – 2</td>
      </tr>
      <tr>
        <td class="data-cell">Операционная система</td>
        <td class="data-cell">Linux с RT патчем</td>
      </tr>
      <tr>
        <td class="data-cell">Диапазон входного напряжения, В</td>
        <td class="data-cell">от 19 до 29</td>
      </tr>
      <tr>
        <td class="data-cell">Номинальное напряжение питания, В</td>
        <td class="data-cell">24</td>
      </tr>
      <tr>
        <td class="data-cell">Наличие индикации питания, канала информационного обмена</td>
        <td class="data-cell">да</td>
      </tr>
      <tr>
        <td class="data-cell">Наличие индикации интерфейсов</td>
        <td class="data-cell">да</td>
      </tr>
      <tr>
        <td class="data-cell">Максимальная потребляемая мощность, Вт</td>
        <td class="data-cell">7,5</td>
      </tr>
      <tr>
        <td class="data-cell">Время выполнения цикла</td>
        <td class="data-cell">Менее 1 мс</td>
      </tr>
      <tr>
        <td class="data-cell">Масса, кг</td>
        <td class="data-cell">0,34</td>
      </tr>
      <tr>
        <td class="data-cell">Размеры (Ш х В х Г), мм</td>
        <td class="data-cell">57,1х130,9x98,0</td>
      </tr>
    </tbody>
  </table>
</div>

## Эксплуатационные характеристики 

<div style="width: 100%; display: grid; grid-template-columns: 1fr;">
  <table style="border-collapse: collapse; width: 100%; min-width: 100%; table-layout: fixed; margin-bottom: 0;">
    <colgroup>
      <col style="width: 500px;">   <!-- Параметр -->
      <col style="width: 250px;">   <!-- Без лака -->
      <col style="width: 250px;">   <!-- С лаком -->
    </colgroup>
    <thead>
      <tr>
        <th rowspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">Параметр</th>
        <th colspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">Значение фактора</th>
      </tr>
      <tr>
        <th style="text-align: center; padding: 8px; border: 1px solid #ccc;">Без лака</th>
        <th style="text-align: center; padding: 8px; border: 1px solid #ccc;">С лаком</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px; border: 1px solid #ccc;">Температура среды, °С</td>
        <td colspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от минус 40 до 60</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ccc;">Относительная влажность воздуха, %</td>
        <td style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от 5 до 70</td>
        <td style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от 5 до 95</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ccc;">Атмосферное давление, кПа</td>
        <td colspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от 84,0 до 106,7</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ccc;">Вибрация<br><em>амплитуда, не более</em></td>
        <td colspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">0,35 мм с частотой 55 Гц</td>
      </tr>
    </tbody>
  </table>
</div>

## Индикация 

<div style="width: 100%; display: grid; grid-template-columns: 1fr;">
  <table style="border-collapse: collapse; width: 100%; min-width: 100%; table-layout: fixed;">
    <colgroup>
      <col style="width: 200px;">   <!-- Параметр -->
      <col style="width: 200px;">   <!-- Без лака -->
      <col style="width: 600px;">   <!-- С лаком -->
    </colgroup>
      <thead>
        <tr>
          <th style="text-align: center; padding: 8px; border: 1px solid #ccc;">Обозначение</th>
          <th style="text-align: center; padding: 8px; border: 1px solid #ccc;">Индикация</th>
          <th style="text-align: center; padding: 8px; border: 1px solid #ccc;">Показатель</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">P</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot green"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Наличие напряжения питания</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">P</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot off"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Отсутствие напряжения питания</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">L</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot green"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Наличие соединения по Ethernet</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">L</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot ethernet-pulse"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Обмен данными по Ethernet</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">L</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot off"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Отсутствие соединения по Ethernet</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">L</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot orange"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Модуль в рабочем состоянии</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">L</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot orange-pulse"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Выполнение загрузки</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">1 - 3</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot green"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Пользовательский светодиод 1 - 3 включен</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">1 - 3</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot off"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Пользовательский светодиод 1 - 3 выключен</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">BL</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot red"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Низкое напряжение питания</td>
        </tr>
        <tr>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;">BL</td>
          <td style="text-align: center; padding: 8px; border: 1px solid #ccc;"><span class="status-dot off"></span></td>
          <td style="padding: 8px; border: 1px solid #ccc;">Рабочее напряжение питания</td>
        </tr>
      </tbody>
  </table>
</div>

<style>
.status-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    margin-right: 2px;
}

.status-dot.green { background-color: #0ec20eff; }
.status-dot.red { background-color: #d82e2eff; }
.status-dot.orange { background-color: #ffa500; }
.status-dot.off { background-color: #cccccc; }

.status-dot.ethernet-pulse {
    background-color: #0ec20eff;
    animation: soft-pulse 1.5s ease-in-out infinite;
    box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
}

.status-dot.orange-pulse {
    background-color: #ffa500;
    animation: soft-pulse-orange 1.5s ease-in-out infinite;
    box-shadow: 0 0 10px rgba(255, 165, 0, 0.5);
}

@keyframes soft-pulse {
    0%, 100% { opacity: 0.4; transform: scale(0.9); box-shadow: 0 0 5px rgba(0, 255, 0, 0.3); }
    50% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 15px rgba(0, 255, 0, 0.7); }
}

@keyframes soft-pulse-orange {
    0%, 100% { opacity: 0.4; transform: scale(0.9); box-shadow: 0 0 5px rgba(255, 165, 0, 0.3); }
    50% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 15px rgba(255, 165, 0, 0.7); }
}
</style>

## Размеры

=== "Габаритные размеры" 
    ![Image title](img/dimensions/dimensions_GMB.svg){ width="580"}
=== "Установочные размеры"
    ![Image title](img/dimensions/installation_dimensions_GMB.svg){ width="580"}


## Файлы для скачивания
<a href="/downloads/proplc.package" download>Пакет таргет файлов для CODESYS v3</a>  