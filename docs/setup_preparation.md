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

    ![Image title](setup_preparation/IP.png){ .fullscreen-image width="280" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

    <style>
    .fullscreen-image {
        cursor: zoom-in;
        transition: transform 0.2s;
    }

    .fullscreen-image:active {
        position: fixed;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999 !important;
        background: rgba(0, 0, 0, 0.95) !important;
        object-fit: contain !important;
        cursor: zoom-out !important;
        padding: 20px !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        transform: none !important;
    }
    </style>


    **Способ 2: Подключение через сетевую инфраструктуру**

    Подключите сетевой кабель к порту Eth1 или Eth2 контроллера, а другой конец - к коммутатору или роутеру в сети с настроенным DHCP-сервером.

4. Для входа в веб-интерфейс управления:

    - Откройте браузер и в адресной строке введите: `http://sa.local`
    - В открывшемся окне авторизации введите: **Логин** - `sa` и **Пароль** - `sa`

5. После первой авторизации смените пароль:

    - Нажмите на иконку профиля в правом верхнем углу.
    - В выпадающем меню выберите пункт «Профиль».

![Image title](setup_preparation/web.png){ .fullscreen-image width="700" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

   <ul style="margin-left: 45px;">
<li>В открывшемся окне введите текущий пароль, задайте и подтвердите новый пароль, затем нажмите кнопку «Сохранить изменения».</li>
</ul>

![Image title](setup_preparation/password.png){ .fullscreen-image width="300" style="display: block; margin-left: auto; margin-right: auto; cursor: zoom-in;" }

<style>
.fullscreen-image {
    cursor: zoom-in;
    margin: 20px auto;
}

.fullscreen-image.fullscreen-active {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    z-index: 9999 !important;
    background: rgba(0, 0, 0, 0.95) !important;
    object-fit: contain !important;
    cursor: zoom-out !important;
    padding: 20px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
}
</style>

<script>
document.querySelectorAll('.fullscreen-image').forEach(img => {
    img.addEventListener('click', function() {
        if (this.classList.contains('fullscreen-active')) {
            this.classList.remove('fullscreen-active');
            document.body.style.overflow = '';
        } else {
            this.classList.add('fullscreen-active');
            document.body.style.overflow = 'hidden';
        }
    });
});

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        const fullscreenImages = document.querySelectorAll('.fullscreen-active');
        fullscreenImages.forEach(img => {
            img.classList.remove('fullscreen-active');
            document.body.style.overflow = '';
        });
    }
});
</script>

