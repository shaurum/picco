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
        <p style="text-align: justify; margin: 0 0 8px 0;">Для сброса до заводских настроек на верхней грани модуля предусмотрена скрытая кнопка «Сброс». Необходимо нажать на кнопку тонким заостренным предметом и удерживать до появления трех звуковых сигналов, подтверждающих выполнение сброса.</p>
    </div>
    
    <img src="img/connection/GMB.svg" alt="Image title" width="340" style="flex-shrink: 0; margin: 0;">
</div>

<p style="text-align: justify; margin: 0 0 0 0;">Также для обеспечения автономной работы часов реального времени при отключении основного питания на верхней грани корпуса модуля предусмотрен разъём под батарейку типа CR1620.</p>

<div style="clear: both;"></div>

## Технические характеристики 

| Характеристика | Значение |
| :--- | :--- |
| Ядро | 4 x Cortex-A72 |
| Оперативная память, Гб | 4, DDR4 |
| Объем памяти, Гб | 8 |
| Поддерживаемые интерфейсы | Ethernet 1000 Мбит/с – 1 (на лицевой части)<br>Ethernet 100 Мбит/с – 2 |
| Операционная система | Linux с RT патчем |
| Диапазон входного напряжения, В | от 19 до 29 |
| Номинальное напряжение питания, В | 24 |
| Наличие индикации питания, канала информационного обмена | да |
| Наличие индикации интерфейсов | да |
| Максимальная потребляемая мощность, Вт | 7,5 |
| Время выполнения цикла | Менее 1 мс |
| Масса, кг | 0,34 |
| Размеры (Ш х В х Г), мм | 57,1х130,9x98,0 |

## Эксплуатационные характеристики
<div style="width: 100%; overflow-x: auto;">
<table border="1" style="border-collapse: collapse; width: 100%;">
<thead>
<tr>
<th rowspan="2" style="text-align: center; vertical-align: middle; padding: 4px;">Параметр</th>
<th colspan="2" style="border: 1px; text-align: center; vertical-align: middle; padding: 4px;">Значение фактора</th>
</tr>
<tr>
<th style="text-align: center; padding: 4px;">Без лака</th>
<th style="text-align: center; padding: 4px;">С лаком</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px; padding: 8px;"><strong>Температура среды, °С</strong></td>
<td colspan="2" style="border: ; text-align: center; vertical-align: middle; padding: 8px;">от минус 40 до 60</td>
</tr>
<tr>
<td style=" padding: 8px;"><strong>Относительная влажность воздуха, %</strong></td>
<td style=" text-align: center; vertical-align: middle; padding: 8px;">от 5 до 70</td>
<td style="text-align: center; vertical-align: middle; padding: 8px;">от 5 до 95</td>
</tr>
<tr>
<td style=" padding: 8px;"><strong>Атмосферное давление, кПа</strong></td>
<td colspan="2" " text-align: center; vertical-align: middle; padding: 8px;">от 84,0 до 106,7</td>
</tr>
<tr>
<td style=" padding: 8px;"><strong>Вибрация</strong><br><em>амплитуда, не более</em></td>
<td colspan="2" style=" text-align: center; vertical-align: middle; padding: 8px;">0,35 мм с частотой 55 Гц</td>
</tr>
</tbody>
</table>
</div>

## Индикация

| Обозначение | Индикация | Показатель |
|---|---|---|
| P | <span class="status-dot green"></span> | Наличие напряжения питания |
| P | <span class="status-dot off"></span> | Отсутствие напряжения питания |
| L | <span class="status-dot green"></span> | Наличие соединения по Ethernet |
| L | <span class="status-dot ethernet-pulse"></span> | Обмен данными по Ethernet |
| L | <span class="status-dot off"></span> | Отсутствие соединения по Ethernet |
| L | <span class="status-dot orange"></span> | Модуль в рабочем состоянии |
| L | <span class="status-dot orange-pulse"></span> | Выполнение загрузки |
|1 - 3| <span class="status-dot green"></span> | Пользовательский светодтод 1 - 3 включен|
|1 - 3| <span class="status-dot off"></span> | Пользовательский светодтод 1 - 3 выключен|
| BL | <span class="status-dot red"></span> | Низкое напряжение питания |
| BL | <span class="status-dot off"></span> | Рабочее напряжение питания |

<style>
.status-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    margin-right: 2px;
}

.status-dot.green {
    background-color: #0ec20eff;
}

.status-dot.red {
    background-color: #d82e2eff;
}

.status-dot.orange {
    background-color: #ffa500;
}

.status-dot.off {
    background-color: #cccccc;
}

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
    0% {
        opacity: 0.4;
        transform: scale(0.9);
        box-shadow: 0 0 5px rgba(0, 255, 0, 0.3);
    }
    50% {
        opacity: 1;
        transform: scale(1.1);
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.7);
    }
    100% {
        opacity: 0.4;
        transform: scale(0.9);
        box-shadow: 0 0 5px rgba(0, 255, 0, 0.3);
    }
}

@keyframes soft-pulse-orange {
    0% {
        opacity: 0.4;
        transform: scale(0.9);
        box-shadow: 0 0 5px rgba(255, 165, 0, 0.3);
    }
    50% {
        opacity: 1;
        transform: scale(1.1);
        box-shadow: 0 0 15px rgba(255, 165, 0, 0.7);
    }
    100% {
        opacity: 0.4;
        transform: scale(0.9);
        box-shadow: 0 0 5px rgba(255, 165, 0, 0.3);
    }
}
</style>

## Размеры

=== "Габаритные размеры" 
    ![Image title](img/dimensions/overall_dimensions_GMB.svg){ width="100"}
=== "Установочные размеры"
    ![Image title](img/dimensions/installation_dimensions_GMB.svg){ width="100"}


## Файлы для скачивания
<a href="/downloads/proplc.package" download>Пакет таргет файлов для CODESYS v3</a>  