# Организация питания
## "Горячая" замена модулей
Контроллер поддерживает функцию «горячей» замены всех модулей. При этом работа оставшихся модулей не нарушается.

Функция «горячей» замены модулей осуществляется при сборке контроллера по схеме [«Кольцо»](assembly.md#_2).

 При сборке контроллера с функцией «горячей» замены модулей, модули ввода питания устанавливаются таким образом, что суммарная потребляемая мощность модулей, расположенных справа от Модуля ввода питания SPPM до следующего Модуля ввода питания SPPM, и модулей, расположенных слева от Модуля ввода питания SPPM до следующего Модуля ввода питания SPPM, не превышает 48 Вт.

 При использовании данного режима все модули ввода питания в группе должны получать питание от одного внешнего блока питания. Это необходимо для предотвращения разности потенциалов и возможного повреждения оборудования.

 При замене неисправного модуля в Модуль ввода питания SPPM ставится перемычка, которая обеспечивает питание модулей, расположенных слева и справа от Модуля ввода питания SPPM, в который установлена перемычка.

 При сборке контроллера без функции горячей замены модулей потребляемая мощность всех модулей после Модуля ввода питания до следующего Модуля ввода питания не должна превышать 48 Вт.

 <table style="border-collapse: collapse; width: 100%; min-width: 100%; table-layout: fixed;">
  <colgroup>
    <col style="width: 250px;">   <!-- Фиксированная ширина для наименования модуля -->
    <col style="width: 150px;">   <!-- Фиксированная ширина для мощности -->
  </colgroup>
  <thead>
    <tr>
      <th style="text-align: center; padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Наименование модуля</th>
      <th style="text-align: center; padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">Максимальная потребляемая мощность, Вт</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">GMB</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">7,5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">DI</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">DO</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">3</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">AIC</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">4</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">AIV</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">2,5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">AITC</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">5,5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">AITR</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">2,5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">AO</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">7,5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">SPPC</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">3</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">SPPM</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">0,5</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">SPTM</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">0</td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">IF485/422</td>
      <td style="padding: 8px; border: 1px solid #ccc; word-wrap: break-word;">2,5</td>
    </tr>
  </tbody>
</table>

_Пример: после основного модуля необходимо поставить в группу 2 модуля DI, 5 модулей DO и 2 модуля AITC._ 

_2*P(DI)+5*Р(DO)+2*Р(AITC) = 2*5+ 5*3+2*5,5 = 36,_

_что меньше 48, а следовательно правила питания не нарушаются._

!!! note "Примечание"
    Контроллер рекомендуется собирать с поддержкой функции "горячей" замены модулей, что позволит извлекать и устанавливать модули в контроллере без отключения питания и остановки выполнения программы.

## Резервирование питания
Резервирование питания контроллера осуществляется за счет подключения двух независимых линий питания с напряжением 24 В постоянного тока к каждому из модулей ввода питания SPPM.

!!! note "Примечание"
    При сборке контроллера следует предусмотреть резервирование питания, что обеспечит непрерывную работу контроллера в случае отказа одного из блоков питания.
    