# Модуль основной SA-P5-GMB 

## Общие сведения

??? example "Тестирование"

    На текущий момент модуль на стадии тестирования. Серийный выпуск запланирован на декабрь 2025 года 
<div style="display: flex; gap: 2rem; align-items: flex-start; margin: 1rem 0;">
    <img src="img/modules/GMB.png" alt="Модуль основной GMB" width="270" style="flex-shrink: 0;">

    <div style="flex: 1; text-align: justify;">
        <p style="text-align: justify; margin: 0 0 1rem 0;"><strong>Наименование:</strong> Модуль основной GMB</p>
        
        <p style="text-align: justify; margin: 0 0 1rem 0;"><strong>Исполнения:</strong><br>
        - SA-P5-GMB (без покрытия)<br>
        - SA-P5-GMB-V (с лаковым покрытием)</p>
        
        <p style="text-align: justify; margin: 0 0 1rem 0;"><strong>Назначение:</strong><br>
        Модуль основной GMB (далее-модуль) является центральным компонентом системы управления.</p>
        
        <p style="text-align: justify; margin: 0 0 0 0;"><strong>Функции:</strong><br>
        - выполнение пользовательской прикладной программы управления;<br>
        - обмен информацией со сторонним устройствами по встроенным интерфейсам;<br>
        - звуковое оповещение, при загрузке данных и при сбросе настроек;<br>
        - опрос модулей расширения.</p>
    </div>
</div>

<div style="display: flex; gap: 2rem; align-items: flex-start; margin: 1rem 0;">
    <div style="flex: 1; text-align: justify;">
        <p style="text-align: justify; margin: 0 0 8px 0;"><strong>Описание:</strong></p>
        <p style="text-align: justify; margin: 0 0 8px 0;">На передней панели модуля расположен переключатель режима работы RUN/STOP, предназначенный для запуска и остановки выполнения цикла основной программы.</p>
        <p style="text-align: justify; margin: 0 0 0 0;">Для сброса до заводских настроек на верхней грани модуля предусмотрена скрытая кнопка «Сброс». Необходимо нажать на кнопку тонким заостренным предметом и удерживать до появления трех звуковых сигналов, подтверждающих выполнение сброса.</p>
    </div>
    
    <img src="img/connection/GMB.svg" alt="Image title" width="340" style="flex-shrink: 0; margin: 0;">
</div>

<p style="text-align: justify; margin: 0 0 0 0;">Также для обеспечения автономной работы часов реального времени при отключении основного питания на верхней грани корпуса модуля предусмотрен разъём под батарейку типа CR1620.</p>

<div style="clear: both;"></div>

## Технические характеристики  

<table style="border-collapse: collapse; width: 100%; min-width: 100%; table-layout: fixed;">
  <colgroup>
    <col style="width: 600px;">   <!-- Фиксированная ширина -->
    <col style="width: 400px;">   <!-- Фиксированная ширина -->
  </colgroup>
  </thead>
    <tr>
      <th style="text-align: center; padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Характеристика</th>
      <th style="text-align: center; padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Значение</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Ядро</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">4 x Cortex-A72</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Оперативная память, Гб</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">4, DDR4</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Объем памяти, Гб</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">8</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; vertical-align: middle; word-wrap: break-word;">Поддерживаемые интерфейсы</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Ethernet 1000 Мбит/с – 1, Ethernet 100 Мбит/с – 2</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Операционная система</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Linux с RT патчем</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Диапазон входного напряжения, В</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">от 19 до 29</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Номинальное напряжение питания, В</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">24</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Наличие индикации питания, канала информационного обмена</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">да</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Наличие индикации интерфейсов</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">да</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Максимальная потребляемая мощность, Вт</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">7,5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Время выполнения цикла</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Менее 1 мс</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Масса, кг</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">0,34</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Размеры (Ш х В х Г), мм</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">57,1х130,9x98,0</td>
    </tr>
  </tbody>
</table>

## Эксплуатационные характеристики 

<div style="width: 100%; display: grid; grid-template-columns: 1fr;">
  <table style="border-collapse: collapse; width: 100%; min-width: 100%; table-layout: fixed; grid-column: 1 / -1;">
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
        <td style="padding: 8px; border: 1px solid #ccc;"><strong>Температура среды, °С</strong></td>
        <td colspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от минус 40 до 60</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ccc;"><strong>Относительная влажность воздуха, %</strong></td>
        <td style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от 5 до 70</td>
        <td style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от 5 до 95</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ccc;"><strong>Атмосферное давление, кПа</strong></td>
        <td colspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">от 84,0 до 106,7</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ccc;"><strong>Вибрация</strong><br><em>амплитуда, не более</em></td>
        <td colspan="2" style="text-align: center; vertical-align: middle; padding: 8px; border: 1px solid #ccc;">0,35 мм с частотой 55 Гц</td>
      </tr>
    </tbody>
  </table>
</div>

## Индикация 

<div style="width: 100%; display: grid; grid-template-columns: 1fr;">
  <table style="border-collapse: collapse; width: 100%; min-width: 100%; table-layout: fixed; grid-column: 1 / -1;">
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
    ![Image title](img/dimensions/overall_dimensions_GMB.svg){ width="100"}
=== "Установочные размеры"
    ![Image title](img/dimensions/installation_dimensions_GMB.svg){ width="100"}


## Файлы для скачивания
<a href="/downloads/proplc.package" download>Пакет таргет файлов для CODESYS v3</a>  