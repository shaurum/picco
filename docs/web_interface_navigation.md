# Web-интерфейс
## Настройка интерфейсов

![Image title](setup_preparation/web_2.png){ width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: pointer;" onclick="this.style.transform=this.style.transform=='scale(2)'?'scale(1)':'scale(2)';this.style.zIndex=this.style.zIndex=='1000'?'auto':'1000'" }

При переходе в веб-интерфейс на экране отображается раздел "Нстройка сети", где представлены текущие параметры всех сетевых интерфейсов. Каждый интерфейс сопоставлен с физическим портом на основном модуле и имеет кнопку "Настроить" для изменения параметров.  

![Image title](setup_preparation/settings.png){ width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: pointer;" onclick="this.style.transform=this.style.transform=='scale(2)'?'scale(1)':'scale(2)';this.style.zIndex=this.style.zIndex=='1000'?'auto':'1000'" }

Для настройки сетевого интерфейса можно выбрать как автоматический режим присвоения сетевых параметров с помощью DHCP, так и вводить их вручную. 

## Системное время

![Image title](setup_preparation/time.png){ width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: pointer;" onclick="this.style.transform=this.style.transform=='scale(2)'?'scale(1)':'scale(2)';this.style.zIndex=this.style.zIndex=='1000'?'auto':'1000'" }

В данном разделе Вы можете настроить системное время устройства: выбрать часовой пояс и включать автоматическую синхронизацию времени через NTP-сервер.

В поле "NTP-серверы" можно указать один или несколько адресов NTP-серверов.

!!! note "Примечание"
      Рекомендуется включить NTP-синхронизацию, чтобы обеспечить точность времени.
     
После завершения настройки времени сохраните изменения.

## Сброс до заводских настроек

??? example "Разработка"

    На текущий момент данный раздел находится в разработке.

Информацию 