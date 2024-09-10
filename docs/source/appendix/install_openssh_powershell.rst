.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci la tua conoscenza di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e giveaway in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _openssh_powershell:

Installare OpenSSH tramite Powershell
========================================

Quando utilizzi il comando ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``) per connetterti al tuo Raspberry Pi, ma appare il seguente messaggio di errore.

    .. code-block::

        ssh: Il termine 'ssh' non è riconosciuto come il nome di un cmdlet, una funzione, un file di script o un programma eseguibile. Verifica
        l'ortografia del nome o, se è stato incluso un percorso, verifica che sia corretto e riprova.


Significa che il tuo sistema operativo è troppo vecchio e non ha `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstallato, e dovrai seguire il tutorial qui sotto per installarlo manualmente.

#. Digita ``powershell`` nella barra di ricerca del desktop di Windows, fai clic con il tasto destro su ``Windows PowerShell`` e seleziona ``Run as administrator`` dal menu che appare.

    .. image:: img/powershell_ssh.png
        :align: center

#. Usa il seguente comando per installare ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Dopo l'installazione, verrà restituito il seguente output.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica l'installazione usando il seguente comando.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ora ti dirà che ``OpenSSH.Client`` è stato installato con successo.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Se il prompt sopra non appare, significa che il tuo sistema Windows è ancora troppo vecchio, e ti consigliamo di installare un tool SSH di terze parti, come :ref:`login_windows`.

#. Ora riavvia PowerShell e continua a eseguirlo come amministratore. A questo punto potrai accedere al tuo Raspberry Pi utilizzando il comando ``ssh``, dove ti verrà richiesto di inserire la password che hai impostato in precedenza.

    .. image:: img/powershell_login.png
