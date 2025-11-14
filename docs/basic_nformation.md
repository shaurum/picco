# Основные сведения
## Назначение
Контроллер программируемый логический СА серии P5 (далее - контроллер) предназначен для сбора и обработки информации с датчиков, формирования сигналов управления по заданным алгоритмам, приема и передачи информации по каналам связи.

Условное обозначение контроллера состоит из условных обозначений модулей, входящих в его состав. Условное обозначение модулей контроллера формируется следующим образом:

![Image title](img/article.webp){: style="width:70%; display:block; margin:auto;"}

## Принцип работы
Принцип работы контроллера основан на преобразовании измерительных сигналов в цифровые данные в модулях ввода, передаче данных по внутренней шине в модуль основной или другие внешние системы через коммутационные интерфейсы, обработке кода в соответствии с алгоритмом прикладной программы и выдаче управляющих сигналов посредством модулей вывода.

## Программное обеспечение

Обеспечение связи между устройствами осуществляется с помощью протокола EtherCAT— технологии, основанной на стандарте Ethernet, но оптимизированной для промышленного управления в реальном времени.

В отличие от традиционной Ethernet-сети, где master устройство опрашивает каждое slave устройство отдельными командами, в EtherCAT master отправляет о интерфейсу один запрос, который проходит через каждое slave-устройство. При этом slave «на лету» считывает из запроса предназначенные ему данные и вставляет в него данные, которые нужно передать дальше. Последнее устройство в сети обнаруживает, что ни к чему не подключено, и пересылает датаграмму обратно master-устройству, используя полнодуплексный режим работы Ethernet.

Такой механизм позволяет на высокой скорости управлять до 65535 устройств в одной сети без ограничения в топологии сети. Причем для организации различных топологий не нужны хабы или коммутаторы.

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EtherCAT Data Train</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: white;
            margin: 0;
            padding: 20px;
        }
        
        .ethercat-animation {
            max-width: 900px;
            margin: 0 auto;
            position: relative;
        }
        
        .network-line {
            position: relative;
            height: 100px;
            background: linear-gradient(to bottom, #e0e0e0, #f5f5f5);
            border: 2px solid #333;
            border-radius: 10px;
            margin: 40px 0;
            overflow: hidden;
        }
        
        .devices {
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 100%;
            padding: 0 20px;
        }
        
        .device {
            text-align: center;
            position: relative;
            z-index: 2;
        }
        
        .device.master {
            order: -1;
        }
        
        .device-label {
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        
        .master .device-label {
            background: #4A90E2;
            color: white;
        }
        
        .slave .device-label {
            background: #50E3C2;
            color: black;
        }
        
        .data-slots {
            display: flex;
            gap: 5px;
            justify-content: center;
        }
        
        .data-slot {
            width: 30px;
            height: 30px;
            border: 2px solid #333;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            position: relative;
            transition: all 0.3s ease;
        }
        
        .data-slot.input { 
            background: #FF6B6B; 
            color: white;
        }
        
        .data-slot.output { 
            background: #4ECDC4; 
            color: white;
        }
        
        .data-slot.empty {
            background: #f0f0f0;
            border-style: dashed;
        }
        
        .data-train {
            position: absolute;
            top: 50%;
            left: 0;
            transform: translateY(-50%);
            display: flex;
            align-items: center;
            transition: left 0.1s linear;
        }
        
        .train-engine {
            width: 40px;
            height: 25px;
            background: #FFA500;
            border: 2px solid #FF8C00;
            border-radius: 8px 0 0 8px;
            position: relative;
        }
        
        .train-engine::after {
            content: '🚂';
            position: absolute;
            top: -5px;
            left: 5px;
            font-size: 16px;
        }
        
        .train-wagon {
            width: 35px;
            height: 25px;
            background: #FFD700;
            border: 2px solid #FFB800;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            color: #333;
        }
        
        .train-wagon.has-data {
            background: #32CD32;
            color: white;
        }
        
        .data-transfer {
            position: absolute;
            width: 20px;
            height: 20px;
            background: #FF4444;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 10px;
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 3;
        }
        
        .animation-controls {
            text-align: center;
            margin-top: 30px;
        }
        
        .animation-controls button {
            padding: 10px 20px;
            margin: 0 10px;
            border: none;
            background: #4A90E2;
            color: white;
            cursor: pointer;
            border-radius: 5px;
            font-size: 14px;
        }
        
        .animation-controls button:hover {
            background: #357ABD;
        }
        
        .animation-controls button:disabled {
            background: #cccccc;
            cursor: not-allowed;
        }
        
        .status {
            margin-top: 10px;
            color: #666;
            font-style: italic;
        }
        
        .explanation {
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 5px;
            border-left: 4px solid #4A90E2;
        }
        
        @keyframes transfer {
            0% { transform: scale(0); opacity: 0; }
            50% { transform: scale(1.2); opacity: 1; }
            100% { transform: scale(1); opacity: 0; }
        }
        
        .transfer-animation {
            animation: transfer 0.6s ease-in-out;
        }
    </style>
</head>
<body>
    <div class="ethercat-animation">
        <h2>EtherCAT Data Transfer - "Поезд данных"</h2>
        
        <div class="network-line">
            <div class="devices">
                <!-- Master -->
                <div class="device master">
                    <div class="device-label">Master</div>
                    <div class="data-slots">
                        <div class="data-slot empty" id="master-slot">?</div>
                    </div>
                </div>
                
                <!-- Slaves -->
                <div class="device slave" data-slave="1">
                    <div class="device-label">Slave 1</div>
                    <div class="data-slots">
                        <div class="data-slot input" id="slave1-input">IN</div>
                        <div class="data-slot output" id="slave1-output">OUT</div>
                    </div>
                </div>
                
                <div class="device slave" data-slave="2">
                    <div class="device-label">Slave 2</div>
                    <div class="data-slots">
                        <div class="data-slot input" id="slave2-input">IN</div>
                        <div class="data-slot output" id="slave2-output">OUT</div>
                    </div>
                </div>
                
                <div class="device slave" data-slave="3">
                    <div class="device-label">Slave 3</div>
                    <div class="data-slots">
                        <div class="data-slot output" id="slave3-output">OUT</div>
                    </div>
                </div>
                
                <div class="device slave" data-slave="4">
                    <div class="device-label">Slave 4</div>
                    <div class="data-slots">
                        <div class="data-slot input" id="slave4-input">IN</div>
                        <div class="data-slot output" id="slave4-output">OUT</div>
                    </div>
                </div>
            </div>
            
            <!-- Поезд -->
            <div class="data-train" id="dataTrain">
                <div class="train-engine"></div>
                <div class="train-wagon" id="wagon1"></div>
                <div class="train-wagon" id="wagon2"></div>
                <div class="train-wagon" id="wagon3"></div>
                <div class="train-wagon" id="wagon4"></div>
                <div class="train-wagon" id="wagon5"></div>
                <div class="train-wagon" id="wagon6"></div>
            </div>
        </div>
        
        <div class="animation-controls">
            <button id="startBtn">▶ Запуск поезда</button>
            <button id="stopBtn" disabled>⏹ Остановить</button>
            <button id="resetBtn">↺ Сброс</button>
            <div class="status" id="status">Готов к отправке</div>
        </div>
        
        <div class="explanation">
            <strong>Как работает:</strong> Поезд (EtherCAT фрейм) движется по сети, забирая выходные данные (OUT) у Slave устройств 
            и доставляя им входные данные (IN). В конце маршрута поезд возвращается к Master со всеми собранными данными.
        </div>
    </div>

    <script>
        class EtherCATTrain {
            constructor() {
                this.isPlaying = false;
                this.train = document.getElementById('dataTrain');
                this.wagons = [
                    document.getElementById('wagon1'),
                    document.getElementById('wagon2'),
                    document.getElementById('wagon3'),
                    document.getElementById('wagon4'),
                    document.getElementById('wagon5'),
                    document.getElementById('wagon6')
                ];
                this.status = document.getElementById('status');
                this.animationId = null;
                this.setupEventListeners();
                this.reset();
            }
            
            setupEventListeners() {
                document.getElementById('startBtn').addEventListener('click', () => this.start());
                document.getElementById('stopBtn').addEventListener('click', () => this.stop());
                document.getElementById('resetBtn').addEventListener('click', () => this.reset());
            }
            
            start() {
                if (this.isPlaying) return;
                
                this.isPlaying = true;
                this.updateControls();
                this.status.textContent = 'Поезд в пути...';
                
                this.animateTrain();
            }
            
            stop() {
                this.isPlaying = false;
                if (this.animationId) {
                    cancelAnimationFrame(this.animationId);
                }
                this.status.textContent = 'Поезд остановлен';
                this.updateControls();
            }
            
            reset() {
                this.stop();
                this.train.style.left = '0px';
                
                // Очищаем вагоны
                this.wagons.forEach(wagon => {
                    wagon.textContent = '';
                    wagon.classList.remove('has-data');
                    wagon.style.background = '#FFD700';
                });
                
                // Сбрасываем слоты
                document.getElementById('master-slot').textContent = '?';
                document.getElementById('master-slot').className = 'data-slot empty';
                
                this.status.textContent = 'Готов к отправке';
                this.updateControls();
            }
            
            updateControls() {
                document.getElementById('startBtn').disabled = this.isPlaying;
                document.getElementById('stopBtn').disabled = !this.isPlaying;
            }
            
            animateTrain() {
                if (!this.isPlaying) return;
                
                const networkWidth = document.querySelector('.network-line').offsetWidth;
                const trainWidth = this.train.offsetWidth;
                const currentPosition = parseInt(this.train.style.left) || 0;
                const maxPosition = networkWidth - trainWidth;
                
                if (currentPosition >= maxPosition) {
                    // Поезд доехал до конца - возвращаемся к Master
                    this.returnToMaster();
                    return;
                }
                
                // Двигаем поезд
                const newPosition = currentPosition + 2;
                this.train.style.left = newPosition + 'px';
                
                // Проверяем позиции для обмена данными
                this.checkDataExchange(newPosition);
                
                this.animationId = requestAnimationFrame(() => this.animateTrain());
            }
            
            checkDataExchange(trainPosition) {
                const slaves = [
                    { element: document.querySelector('[data-slave="1"]'), input: 'slave1-input', output: 'slave1-output' },
                    { element: document.querySelector('[data-slave="2"]'), input: 'slave2-input', output: 'slave2-output' },
                    { element: document.querySelector('[data-slave="3"]'), input: null, output: 'slave3-output' },
                    { element: document.querySelector('[data-slave="4"]'), input: 'slave4-input', output: 'slave4-output' }
                ];
                
                slaves.forEach((slave, index) => {
                    const slaveRect = slave.element.getBoundingClientRect();
                    const trainRect = this.train.getBoundingClientRect();
                    
                    // Если поезд рядом с Slave
                    if (Math.abs(slaveRect.left - trainRect.left) < 50) {
                        this.exchangeDataWithSlave(slave, index);
                    }
                });
            }
            
            exchangeDataWithSlave(slave, slaveIndex) {
                // Забираем выходные данные (OUT) у Slave
                if (slave.output) {
                    const outputSlot = document.getElementById(slave.output);
                    const wagonIndex = slaveIndex * 2;
                    
                    if (outputSlot.textContent === 'OUT' && this.wagons[wagonIndex].textContent === '') {
                        this.wagons[wagonIndex].textContent = 'OUT';
                        this.wagons[wagonIndex].classList.add('has-data');
                        outputSlot.textContent = '✓';
                        outputSlot.style.background = '#888';
                        this.showTransferAnimation(outputSlot, this.wagons[wagonIndex], '📤');
                    }
                }
                
                // Доставляем входные данные (IN) Slave
                if (slave.input) {
                    const inputSlot = document.getElementById(slave.input);
                    const wagonIndex = slaveIndex * 2 + 1;
                    
                    if (inputSlot.textContent === 'IN' && this.wagons[wagonIndex].textContent === '') {
                        this.wagons[wagonIndex].textContent = 'IN';
                        this.wagons[wagonIndex].classList.add('has-data');
                        inputSlot.textContent = '✓';
                        inputSlot.style.background = '#888';
                        this.showTransferAnimation(this.wagons[wagonIndex], inputSlot, '📥');
                    }
                }
            }
            
            showTransferAnimation(fromElement, toElement, symbol) {
                const fromRect = fromElement.getBoundingClientRect();
                const toRect = toElement.getBoundingClientRect();
                const networkRect = document.querySelector('.network-line').getBoundingClientRect();
                
                const transfer = document.createElement('div');
                transfer.className = 'data-transfer transfer-animation';
                transfer.textContent = symbol;
                transfer.style.left = (fromRect.left - networkRect.left + fromRect.width / 2) + 'px';
                transfer.style.top = (fromRect.top - networkRect.top + fromRect.height / 2) + 'px';
                
                document.querySelector('.network-line').appendChild(transfer);
                
                setTimeout(() => {
                    transfer.style.left = (toRect.left - networkRect.left + toRect.width / 2) + 'px';
                    transfer.style.top = (toRect.top - networkRect.top + toRect.height / 2) + 'px';
                }, 300);
                
                setTimeout(() => {
                    transfer.remove();
                }, 600);
            }
            
            returnToMaster() {
                this.status.textContent = 'Поезд возвращается к Master...';
                
                // Показываем собранные данные у Master
                const collectedData = this.wagons.filter(wagon => wagon.textContent !== '').length;
                const masterSlot = document.getElementById('master-slot');
                masterSlot.textContent = collectedData + ' данных';
                masterSlot.className = 'data-slot output';
                
                // Возвращаем поезд к началу
                this.train.style.transition = 'left 1s ease-in-out';
                this.train.style.left = '0px';
                
                setTimeout(() => {
                    this.train.style.transition = '';
                    this.status.textContent = 'Данные доставлены Master!';
                    setTimeout(() => this.reset(), 2000);
                }, 1000);
            }
        }
        
        // Инициализация
        document.addEventListener('DOMContentLoaded', function() {
            new EtherCATTrain();
        });
    </script>
</body>
</html>

В протоколе EtherCAT для обмена данными между master устройством и slave устройствами используются два основных механизма: PDO (Process Data Object) и SDO (Service Data Object), которые заимствованы из профиля CoE (CANopen over EtherCAT).

PDO предназначен для циклического, высокоскоростного обмена процессными данными в режиме реального времени. Перед началом работы система настраивается: master указывает, какие переменные из объектного словаря (Object Dictionary - OD) каждого устройства должны автоматически передаваться в каждом цикле EtherCAT. После этого данные передаются без запросов, без адресации и без подтверждений — в строго определённые временные окна, встроенные в цикл сети. PDO делятся на TxPDO ( Transmit PDO) — данные, отправляемые от slave к master, и RxPDO (Receive PDO) — данные, передаваемые от master к slave.

SDO предназначен для ацикличного обмена данными. С его помощью осуществляется чтение и запись параметров устройства, хранящихся в объектном словаре. В отличие от PDO, SDO работает по принципу «запрос-ответ»: master отправляет команду, slave её обрабатывает и возвращает результат.

## Условия эксплуатации

<table border="1" style="border-collapse: collapse; width: 100%;">
<thead>
<tr>
<th rowspan="2" style="text-align: center; vertical-align: middle; padding: 4px;">Воздействующие факторы</th>
<th rowspan="2" style="text-align: center; vertical-align: middle; padding: 4px;">Характеристики воздействующих факторов</th>
<th colspan="2" style="text-align: center; vertical-align: middle; padding: 4px;">Значение фактора</th>
</tr>
<tr>
<th style="text-align: center; padding: 4px;">Без лака</th>
<th style="text-align: center; padding: 4px;">С лаком</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="vertical-align: middle;" ><strong>1. Синусоидальная вибрация</strong></td>
<td>Амплитуда перемещения, мм</td>
<td colspan="2" style="text-align: center; vertical-align: middle; ">0,35</td>
</tr>
<tr>
<td>Диапазон частот, Гц</td>
<td colspan="2" style="text-align: center; vertical-align: middle;">от 10 до 55</td>
</tr>
<tr>
<td><strong>2. Повышенная температура среды</strong></td>
<td style="vertical-align: middle;">Рабочая, °С</td>
<td colspan="2" style="text-align: center; vertical-align: middle;">60</td>
</tr>
<tr>
<td><strong>3. Пониженная температура среды</strong></td>
<td style="vertical-align: middle;">Рабочая, °С</td>
<td colspan="2" style="text-align: center; vertical-align: middle;">минус 40</td>
</tr>
<tr>
<td><strong>4. Атмосферное давление</strong></td>
<td style="vertical-align: middle;">Рабочее, кПа (мм рт. ст.)</td>
<td colspan="2" style="text-align: center; vertical-align: middle;">от 84,0 до 106,7<br>(от 630 до 800)</td>
</tr>
<tr>
<td><strong>5. Повышенная влажность</strong></td>
<td>Относительная влажность воздуха при температуре 35°С, %</td>
<td style="text-align: center; vertical-align: middle;"> 70</td>
<td style="text-align: center; vertical-align: middle;">95</td>
</tr>
</tbody>
</table>

## Меры безопасности 

По способу защиты от поражения электрическим током модули контроллера соответствуют классу II по ГОСТ Р 58698-2019. 

Для обеспечения дополнительной защиты от поражения электрическим током  в модуле ввода питания предусмотрено заземление.

Во время эксплуатации и технического обслуживания прибора необходимо соблюдать требования
ГОСТ 12.3.019-80, «Правил эксплуатации электроустановок потребителей» и «Правил охраны труда
при эксплуатации электроустановок потребителей».

Не допускается попадание влаги на контакты выходного разъема и внутренние электроэлементы
прибора.

Любые подключения к прибору и работы по его техническому обслуживанию производить только при
отключенном питании прибора и подключенных к нему устройств.


## Техническое обслуживание 

Техническое обслуживание контроллера заключается в профилактическом осмотре модулей, состояния разъемов и периодической поверке аналоговых каналов преобразования и воспроизведения. 

Периодичность профилактических осмотров при техническом обслуживании - один раз в год. При осмотре контроллера производится: 

- проверка отсутствия внешних повреждений, влияющих на функциональные или технические характеристики контроллера; 
- проверка надежности контактов соединителей. При необходимости винтовые зажимы подтягиваются, удаляется пыль методом продувки сжатым воздухом. 

Аналоговые каналы контроллера подлежат периодической поверке для обеспечения единства измерения с требуемой точностью. Интервал между поверками – 5 лет. Записи о проведенной поверке заносятся в паспорт на модуль.

## Маркировка

На корпус каждого модуля контроллера наносится по 4 наклейки, на которых должна быть отображена следующая информация:

- товарный знак;
- наименование модуля;
- артикул изделия;
- заводской номер;
- QR Code по ГОСТ Р ИСО/МЭК 18004-2015 с заводским номером;
- страна-изготовитель;
- единый знак обращения продукции на рынке государств-членов Таможенного союза (ЕАС) – при наличии сертификата (декларации) Таможенного союза на изделие;
- знак средства измерения – при наличии сертификата типа средства измерения;
- потребляемая мощность;
- напряжение питания;
- год выпуска.

На упаковку изготовителя наносится наклейка, в которую должны входить:

- товарный знак или код изготовителя;
- наименование модуля;
- артикул изделия;
- заводской номер;
- QR Code по ГОСТ Р ИСО/МЭК 18004-2015 с заводским номером;
- единый знак обращения продукции на рынке государств-членов Таможенного союза (ЕАС) – при наличии сертификата (декларации) Таможенного союза на изделие;
- знак средства измерения – при наличии сертификата типа измерения на изделие; 
- сведения о местонахождении изготовителя (адрес, включая страну);
- дата упаковки.

## Упаковка

Каждый модуль контроллера упаковывается в отдельную потребительскую тару. В качестве упаковки изготовителя используются ящики или коробки из гофрированного картона. Первым, под ложемент, в коробку помещается паспорт. После паспорта размещается ложемент. Комплект монтажных частей помещается в коробку в отсеки ложемента. Модуль помещается горизонтально маркировочными наклейками вверх.

## Транспортирование и хранение

Транспортирование модулей контроллера производится в упаковке изготовителя в соответствии с разделом "Упаковка". Модули контроллера могут транспортироваться на любые расстояния всеми видами транспорта в крытых транспортных средствах в соответствии с правилами перевозки грузов, действующими на данном виде транспорта.

Модули контроллера хранить в упаковке изготовителя в соответствии с разделом "Упаковка", в крытых складских помещениях, защищённых от атмосферных осадков и почвенной влаги, на расстоянии не менее 1 метра от отопительных приборов в следующих условиях: при температурах от минус 14 °С до плюс 40 °С и относительной влажности воздуха от 25 % до 70 %.


